import numpy as np
import os
import cv2
import imutils
from utils import *

###
### Source: https://github.com/HYPJUDY/panorama-image-stitching (C++)
### Converted from C++ to Python using OpenCV with some modifications
### and additions.
###

def panorama_stitich(input_dir, multiblend=False, cyl_warp=False, output_width=400):
  threshold = 30

  # load images
  input_imgs = []
  for file in os.listdir(input_dir):
    image = imutils.resize(cv2.imread('{}/{}'.format(input_dir, file)), output_width)
    # perform cylinderical warping before loading
    if (cyl_warp is True):
      image = cylindrical_projection(imutils.resize(image))
    input_imgs.append(image)
  img_num = len(input_imgs)

  # extract SIFT features
  kps = []
  features = []
  for image in input_imgs:
    (k, f) = detectAndDescribe(image)
    kps.append(k)
    features.append(f)

  # find adjacent relations
  adjacent = []
  adjacent_flag = []
  for i in range(img_num):
    adjacent.append([])
    adjacent_flag.append([])
    for j in range(img_num):
      adjacent_flag[i].append(False)
  for i in range(img_num):
    for j in range(i + 1, img_num):
      pairs, _, _ = matchKeypoints(kps[i], kps[j], features[i],
        features[j], 0.75, 4.0)
      if (len(pairs) >= threshold):
        if j not in adjacent[i]:
          adjacent[i].append(j)
        if i not in adjacent[j]:
          adjacent[j].append(i)
        adjacent_flag[i][j] = adjacent_flag[j][i] = True
  
  # assume middle file is the center image
  last_idx = int(np.floor(img_num/2))
  to_stitch_idxs = [last_idx]
  stitched_idxs = [last_idx]
  stitched_img = input_imgs[last_idx].copy()
  n = 0
  while (len(to_stitch_idxs) != 0):
    to_stitch_idx = to_stitch_idxs.pop(0)
    for i in range(len(adjacent[to_stitch_idx]) - 1, -1, -1):
      # manage adjacency list and boolean table
      adjacent_idx = adjacent[to_stitch_idx][i]
      if (adjacent_flag[to_stitch_idx][adjacent_idx] == False):
        continue
      adjacent_flag[to_stitch_idx][adjacent_idx] = False
      adjacent_flag[adjacent_idx][to_stitch_idx] = False
      to_stitch_idxs.append(adjacent_idx)
      if (adjacent_idx in stitched_idxs):
        continue
      stitched_idxs.append(adjacent_idx)
      
      # calculate SIFT for previously stitched image
      # then calculate Homography matrix between it and
      # image to be stitched
      (k, f) = detectAndDescribe(stitched_img)
      _, H, _ = matchKeypoints(k, kps[adjacent_idx],
        f, features[adjacent_idx], 0.75, 4.0)
      # this works better for this version than simply changing
      # order of input
      H_inv = np.linalg.inv(H)

      # calculate using inverse H the output dimensions after stitching
      adjacent_img = input_imgs[adjacent_idx].copy()
      min_x = get_min_warped_x(adjacent_img, H_inv)
      min_y = get_min_warped_y(adjacent_img, H_inv)
      max_x = get_max_warped_x(adjacent_img, H_inv, stitched_img)
      max_y = get_max_warped_y(adjacent_img, H_inv, stitched_img)
      out_w, out_h = int(np.floor(max_x - min_x)), int(np.floor(max_y - min_y))
      out_shape = (out_h, out_w) + adjacent_img.shape[2:]
      last_stitch = np.zeros(out_shape, dtype='uint8')
      next_stitch = np.zeros(out_shape, dtype='uint8')
      
      n += 1
      # place the two images using H in position for blending
      img_shift(stitched_img, last_stitch, min_x, min_y)
      show_image(last_stitch, "Last Stitch {}".format(n))
      img_homography_warping(adjacent_img, next_stitch, H, min_x, min_y)
      show_image(next_stitch, "Next Stitch {}".format(n))
      # not necessary to apply Homography matrix to features as
      # it is recalculated in every loop

      # blend the previous stich and warped adjacent image
      if (multiblend):
        stitched_img = multiband_blending(last_stitch, next_stitch)
      else:
        stitched_img = alpha_blending(last_stitch, next_stitch)
      show_image(stitched_img, "Stitched {}".format(n))
  # crop the black regions so that output is filled
  stitched_img = panorama_crop_blackregions(stitched_img)
  show_image(stitched_img, "Final Stitched Image", 0)
  return stitched_img