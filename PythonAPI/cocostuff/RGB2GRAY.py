import cv2
import numpy as np
import os    
 
IMAGE_DIR= '/data2/pd/sdc/shipdet/v1/coco/annotations/stuffthingmaps/train2017/'
out = '/data2/pd/sdc/shipdet/v1/coco/stuffthingmaps/train2017/'
 
file_names = next(os.walk(IMAGE_DIR))[2]
for x in range(len(file_names)):
    img = cv2.imread(os.path.join(IMAGE_DIR, file_names[x]))
    #img = cv2.imread(img_path)
    #获取图片的宽和高
    #width,height = img.shape[:2][::-1]
    # #将图片缩小便于显示观看
    # img_resize = cv2.resize(img,
    # (int(width*0.5),int(height*0.5)),interpolation=cv2.INTER_CUBIC)
    # cv2.imshow("img",img_resize)
    # print("img_reisze shape:{}".format(np.shape(img_resize)))
 
    #将图片转为灰度图
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    cv2.imwrite(out+str(file_names[x]),img_gray)
 
    #cv2.waitKey()