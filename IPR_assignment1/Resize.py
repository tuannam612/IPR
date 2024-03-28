import cv2

def image_resize(desired_height, desired_width, path_from_user):
    path = path_from_user

    img = cv2.imread(path)
    resized_img= cv2.resize(img, (desired_height, desired_width), fx = 0.1, fy = 0.1)
    
    cv2.imshow("After Resize",resized_img)
    cv2.waitKey()
    