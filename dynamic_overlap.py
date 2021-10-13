import math
from PIL import Image


# The following function, given an image and a target size (img_h, img_w), returns the total number of crops of size (img_h, img_w) 
# in which the image can be divided. Moreover, it computes the overlapping value of each crop with the adjacent ones in order to 
# split the original image in an integer number of crops of size (img_h, img_w).

def dynamic_overlap(img, img_h, img_w):
    crops_x = img.size[0] / img_w
    crops_y = img.size[1] / img_h

    num_crops = crops_x * crops_y

    overlap_x = math.ceil((math.modf(crops_x)[0] * img_w)/crops_x)
    overlap_y = math.ceil((math.modf(crops_y)[0] * img_w)/crops_y)

    return {"num_crops": num_crops, "overlap_x": overlap_x, "overlap_y": overlap_y}

