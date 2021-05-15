import cv2,time

video=cv2.VideoCapture(0)
first_frame=None
while True:
    check,frame=video.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)

    if first_frame is None:
    	first_frame=gray
    	continue

    delta_frame=cv2.absdiff(first_frame,gray)
    thresh_frame=cv2.threshold(delta_frame,50,255,cv2.THRESH_BINARY)[1]
    thresh_frame=cv2.dilate(thresh_frame,None,iterations=2)

    (cnts,_)=cv2.findContours(thresh_frame.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

    for contor in cnts:
    	if cv2.contourArea(contor) < 10000:
    		continue

    	(x,y,w,h)=cv2.boundingRect(contor)
    	cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)
    
    cv2.imshow('delta_frames',delta_frame)
    
    cv2.imshow('color_frames',frame)
    key=cv2.waitKey(1)
    
    if key==ord('q'):
        break
print(delta_frame)
print(thresh_frame)
video.release()
cv2.destroyAllWindows()