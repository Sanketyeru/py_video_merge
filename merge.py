import cv2
import numpy as np

invid_1 = "/home/n200/Documents/codes/ITRI/edgematrix/out_EH_PIH_mbv2-c0.avi"  
invid_2 = "/home/n200/Documents/codes/ITRI/edgematrix/out_EH_PIH_mbv2-c10.avi"
invid_3 = "/home/n200/Documents/codes/ITRI/edgematrix/out_EH_PIH_mbv2-c20.avi"

cap1 = cv2.VideoCapture(invid_1)
cap2 = cv2.VideoCapture(invid_2)
cap3 = cv2.VideoCapture(invid_3)

frame_width_1 = int(cap1.get(3))
frame_height_1 = int(cap1.get(4))

out = cv2.VideoWriter(f"comb_video.avi",cv2.VideoWriter_fourcc('M','J','P','G'), 30, (640*2,480*2))

while True:
    
    ret,frame_1 = cap1.read()
    ret,frame_2 = cap2.read()
    ret,frame_3 = cap3.read()

    if not ret :
        break

    canvas = np.zeros_like(frame_1, np.uint8)
        
    img =np.concatenate((np.concatenate((frame_1, frame_2), axis=1), np.concatenate((frame_3, canvas), axis=1)), axis=0)

    cv2.imshow("",img)
    out.write(img)
    if cv2.waitKey(1) & 0xff ==ord('q'):
        break

cv2.destroyAllWindows()
      