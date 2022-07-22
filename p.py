import cv2
import numpy as np

video=cv2.VideoCapture("vid.mp4")
image=cv2.imread("img.jpg")

while True:
    ret,frame=video.read()
    if frame is None or image is None:
        break
    else:
        frame=cv2.resize(frame,(800,600))    
        image=cv2.resize(image,(800,600))
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        l_g=np.array([32,94,132])
        u_g=np.array([179,255,255])
        mask=cv2.inRange(hsv,l_g,u_g)
        res=cv2.bitwise_and(frame,frame,mask=mask)
        f=frame-res
        green_screen=np.where(f==0,image,f)        
        cv2.imshow("Final result",green_screen)
        k=cv2.waitKey(1)
        if k==ord('q'):
            break

video.release()
cv2.destroyAllWindows()
