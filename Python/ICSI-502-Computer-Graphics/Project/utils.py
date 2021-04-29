import numpy as np
import cv2

def show_image(image, title, time=1.0):
  title = '{} | Press any key to continue'.format(title)
  cv2.namedWindow(title)
  cv2.moveWindow(title, 16, 16)
  cv2.imshow(title, image)
  cv2.waitKey(int(time * 1000))
  cv2.destroyAllWindows()

def _sample_bilinear(image, x, y):
  x1, y1 = int(x), int(y)
  x2, y2 = min(x1+1, image.shape[1]-1), min(y1+1, image.shape[0]-1)
  # denominators ignored as x2 - x1 = y2 - y1 = 1, at the edges 0
  fxy1 = (x2 - x)*image[y1, x1] + (x - x1)*image[y1, x2]
  fxy2 = (x2 - x)*image[y2, x1] + (x - x1)*image[y2, x2]
  return (y2 - y)*fxy1 + (y - y1)*fxy2

def _is_pixel_black(img, x, y, c=0):
  return img[y, x, 0] <= c and img[y, x, 1] <= c and img[y, x, 2] <= c

def _crop_hpinch(a, onlydim=False, bth=20):
  (h, w) = a.shape[:2]
  ct, cb = 0, h-1
  bw, ew = int(w*0.25), int(w*0.75)
  for x in range(bw, ew, 5):
    t, b = 0, h-1
    while (t < h and _is_pixel_black(a, x, t, bth)): t += 1
    ct = max(ct, t)
    while (b > 0 and _is_pixel_black(a, x, b, bth)): b -= 1
    cb = min(cb, b)
  vcrop = a[ct:cb, :]
  (h, w) = vcrop.shape[:2]
  cl, cr = 0, w-1
  for y in range(0, h, 5):
    l, r = 0, w-1
    while (l < w and _is_pixel_black(vcrop, l, y)): l += 1
    cl = max(cl, l)
    while (r > 0 and _is_pixel_black(vcrop, r, y)): r -= 1
    cr = min(cr, r)
  if (onlydim):
    return ct, cb, cl, cr
  return vcrop[:, cl:cr]

def _crop_hbubble(a, onlydim=False, bth=20):
  (h, w) = a.shape[:2]
  cl, cr = 0, w-1
  bh, eh = int(h*0.25), int(h*0.75)
  for y in range(bh, eh, 5):
    l, r = 0, w-1
    while (l < h and _is_pixel_black(a, l, y)): l += 1
    cl = max(cl, l)
    while (r > 0 and _is_pixel_black(a, r, y)): r -= 1
    cr = min(cr, r)
  hcrop = a[:, cl:cr]
  (h, w) = hcrop.shape[:2]
  ct, cb = 0, h-1
  for x in range(0, w, 5):
    t, b = 0, h-1
    while (t < h and _is_pixel_black(hcrop, x, t, bth)): t += 1
    ct = max(ct, t)
    while (b > 0 and _is_pixel_black(hcrop, x, b, bth)): b -= 1
    cb = min(cb, b)
  if (onlydim):
    return ct, cb, cl, cr
  return hcrop[ct:cb, :]

def panorama_crop_blackregions(a):
  (h, w) = a.shape[:2]
  cl, cr = 0, w-1
  for y in range(8, h-8, 5):
    l, r = 0, w-1
    while (l < h and _is_pixel_black(a, l, y)): l += 1
    cl = max(cl, l)
    while (r > 0 and _is_pixel_black(a, r, y)): r -= 1
    cr = min(cr, r)
  # assume if a left edge or right edge touching top and bottom
  # is within 1/4 of their respective side then panorama looks
  # like it is horizontally pinched
  if (cl<0.25*w or cr>0.75*w):
    return _crop_hpinch(a)
  # else panorama looks like a "bubble" likely due to cylindrical
  # warping of adjacent photos and/or minimal rotation in the input
  return _crop_hbubble(a)

def alpha_blending(a, b, factors=(0.5, 0.5)):
  assert sum(factors) == 1.0
  result = np.zeros(a.shape, dtype='uint8')
  for y, x, c in np.ndindex(result.shape):
    if (_is_pixel_black(a, x, y) or _is_pixel_black(b, x, y)):
      result[y, x, c] = a[y, x, c] + b[y, x, c]
    else:
      result[y, x, c] = int(a[y, x, c]*factors[0] + b[y, x, c]*factors[1])
  return result

###
### Source: https://github.com/HYPJUDY/panorama-image-stitching
### Converted from C++ to Python using OpenCV
###

def cylindrical_projection(image):
  result = np.zeros(image.shape, 'uint8')
  angle = 15.0
  (proj_h, proj_w) = image.shape[:2]
  cx, cy = proj_w/2, proj_h/2
  r = cx/np.tan(angle*np.pi/180.0)
  for i, j in np.ndindex(proj_w, proj_h):
    dst_x = i - cx
    dst_y = j - cy
    k = r/np.sqrt(r**2 + dst_x**2)
    src_x = dst_x/k + cx
    src_y = dst_y/k + cy
    if src_x >= 0 and src_x <= proj_w and src_y >= 0 and src_y <= proj_h:
      result[j, i] = _sample_bilinear(image, src_x, src_y)
  return result

def _get_warped_x(x, y, H):
  warped = np.matmul(H, [x, y, 1])
  return warped[0]/warped[2]

def _get_warped_y(x, y, H):
  warped = np.matmul(H, [x, y, 1])
  return warped[1]/warped[2]

def get_min_warped_x(input_img, H):
  (h, w) = input_img.shape[:2]
  min_x = min(_get_warped_x(0, 0, H), _get_warped_x(w-1, 0, H),
    _get_warped_x(0, h-1, H), _get_warped_x(w-1, h-1, H))
  return min_x if min_x < 0 else 0

def get_min_warped_y(input_img, H):
  (h, w) = input_img.shape[:2]
  min_y = min(_get_warped_y(0, 0, H), _get_warped_y(w-1, 0, H),
    _get_warped_y(0, h-1, H), _get_warped_y(w-1, h-1, H))
  return min_y if min_y < 0 else 0

def get_max_warped_x(input_img, H, stitched_img):
  (h, w) = input_img.shape[:2]
  max_x = max(_get_warped_x(0, 0, H), _get_warped_x(w-1, 0, H),
    _get_warped_x(0, h-1, H), _get_warped_x(w-1, h-1, H))
  w1 = stitched_img.shape[1]
  return max_x if max_x >= w1 else w1

def get_max_warped_y(input_img, H, stitched_img):
  (h, w) = input_img.shape[:2]
  max_y = max(_get_warped_y(0, 0, H), _get_warped_y(w-1, 0, H),
    _get_warped_y(0, h-1, H), _get_warped_y(w-1, h-1, H))
  h1 = stitched_img.shape[0]
  return max_y if max_y >= h1 else h1

def img_homography_warping(src, dst, H, offset_x, offset_y):
  for y, x in np.ndindex(dst.shape[:2]):
    warped_x = _get_warped_x(x + offset_x, y + offset_y, H)
    warped_y = _get_warped_y(x + offset_x, y + offset_y, H)
    if (warped_x >= 0 and warped_x < src.shape[1] and
      warped_y >= 0 and warped_y < src.shape[0]):
      # dst[y, x] = src[int(np.floor(warped_y)), int(np.floor(warped_x))]
      dst[y, x] = _sample_bilinear(src, warped_x, warped_y)

def img_shift(src, dst, offset_x, offset_y):
  for y, x in np.ndindex(dst.shape[:2]):
    x0 = int(x + offset_x)
    y0 = int(y + offset_y)
    if (x0 >= 0 and x0 < src.shape[1] and
      y0 >= 0 and y0 < src.shape[0]):
      dst[y, x] = src[y0, x0]

def multiband_blending(a, b):
  (h, w) = a.shape[:2]
  
  sum_a_x = width_mid_a = 0
  sum_overlap_x = width_mid_overlap = 0
  
  mid_y = int(h/2)
  x1 = 0

  while (x1<w and _is_pixel_black(a, x1, mid_y)): x1 += 1
  for x in range(x1, w):
    if (_is_pixel_black(a, x, mid_y) == False):
      sum_a_x += x
      width_mid_a += 1
      if (_is_pixel_black(b, x, mid_y) == False):
        sum_overlap_x += x
        width_mid_overlap += 1

  max_len = w if w >= h else h
  level_num = int(np.floor(np.log2(max_len)))

  mask = [np.zeros((h, w, 1), dtype='float')]
  assert width_mid_a > 0
  assert width_mid_overlap > 0
  ratio = 1.0 * sum_a_x / width_mid_a
  overlap_ratio = 1.0 * sum_overlap_x / width_mid_overlap
  if (ratio < overlap_ratio):
    for y, x in np.ndindex(h, int(overlap_ratio)):
      mask[0][y, x] = 1
  else:
    for x in range(int(overlap_ratio+1), w):
      for y in range(h):
        mask[0][y, x] = 1

  a_pyramid = [a.copy().astype(float)]
  b_pyramid = [b.copy().astype(float)]
  for i in range(1, level_num):
    a_pyramid.append(cv2.pyrDown(a_pyramid[i-1]))
    b_pyramid.append(cv2.pyrDown(b_pyramid[i-1]))
    mask.append(cv2.pyrDown(mask[i-1]))

  for i in range(level_num-1):
    (hp, wp) = a_pyramid[i].shape[:2]
    a_pyramid[i] = cv2.subtract(a_pyramid[i],
      cv2.pyrUp(a_pyramid[i+1], dstsize=(wp, hp)))
    b_pyramid[i] = cv2.subtract(b_pyramid[i],
      cv2.pyrUp(b_pyramid[i+1], dstsize=(wp, hp)))

  blend_pyramid = []
  for i in range(level_num):
    blend_pyramid.append(np.zeros(a_pyramid[i].shape, dtype='float'))
    # blend_pyramid.append(np.zeros(a_pyramid[i].shape, dtype='uint8'))
    for y, x, c in np.ndindex(blend_pyramid[i].shape):
      amasked = a_pyramid[i][y, x, c] * mask[i][y, x]
      bmasked = b_pyramid[i][y, x, c] * (1.0 - mask[i][y, x])
      blend_pyramid[i][y, x, c] = amasked + bmasked 
  
  expand = blend_pyramid[level_num-1].astype(dtype='uint8')
  for i in range(level_num-2, -1, -1):
    expand = cv2.pyrUp(expand, dstsize=blend_pyramid[i].shape[1::-1])
    for y, x, c in np.ndindex(blend_pyramid[i].shape):
      r = blend_pyramid[i][y, x, c] + float(expand[y, x, c])
      if (r > 255): r = 255
      elif (r < 0): r = 0
      expand[y, x, c] = r
  return expand

###
### Source: https://www.pyimagesearch.com/2016/01/11/opencv-panorama-stitching/
### Requires OpenCV 3.X below or at 3.4.2 for SIFT which is non-free
### 'conda install opencv' installed the required version but may not in the future
###

def detectAndDescribe(image):
  # convert the image to grayscale
  # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # check to see if we are using OpenCV 3.X
  # if self.isv3:
    # detect and extract features from the image
  descriptor = cv2.xfeatures2d.SIFT_create()
  (kps, features) = descriptor.detectAndCompute(image, None)

  # # otherwise, we are using OpenCV 2.4.X
  # else:
  #   # detect keypoints in the image
  #   detector = cv2.FeatureDetector_create("SIFT")
  #   kps = detector.detect(gray)

  #   # extract features from the image
  #   extractor = cv2.DescriptorExtractor_create("SIFT")
  #   (kps, features) = extractor.compute(gray, kps)

  # convert the keypoints from KeyPoint objects to NumPy
  # arrays
  kps = np.float32([kp.pt for kp in kps])

  # return a tuple of keypoints and features
  return (kps, features)

def matchKeypoints(kpsA, kpsB, featuresA, featuresB,
  ratio, reprojThresh):
  # compute the raw matches and initialize the list of actual
  # matches
  matcher = cv2.DescriptorMatcher_create("BruteForce")
  rawMatches = matcher.knnMatch(featuresA, featuresB, 2)
  matches = []

  # loop over the raw matches
  for m in rawMatches:
    # ensure the distance is within a certain ratio of each
    # other (i.e. Lowe's ratio test)
    if len(m) == 2 and m[0].distance < m[1].distance * ratio:
      matches.append((m[0].trainIdx, m[0].queryIdx))

  # computing a homography requires at least 4 matches
  if len(matches) > 4:
    # construct the two sets of points
    ptsA = np.float32([kpsA[i] for (_, i) in matches])
    ptsB = np.float32([kpsB[i] for (i, _) in matches])

    # compute the homography between the two sets of points
    (H, status) = cv2.findHomography(ptsA, ptsB, cv2.RANSAC,
      reprojThresh)

    # return the matches along with the homograpy matrix
    # and status of each matched point
    return (matches, H, status)

  # otherwise, no homograpy could be computed
  return None
