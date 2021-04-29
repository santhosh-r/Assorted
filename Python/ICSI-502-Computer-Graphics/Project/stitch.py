import cv2
from panorama import panorama_stitich

# todo: proper handling of console arguments
INPUT = 'input2'
MULTIBAND_BLENDING = True
# more beneficial when rotation between photos is higher
CYLINDRICAL_WARPING = True

def main():
  stitch = panorama_stitich('input/{}'.format(INPUT), MULTIBAND_BLENDING,
    CYLINDRICAL_WARPING)  
  cv2.imwrite('output/{}_output.png'.format(INPUT), stitch)

if __name__ == '__main__':
  main()