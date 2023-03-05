import cv2
cap = cv2.VideoCapture(0)
while True:
    photo = cap.read()[1]           # Storing the frame in a variable photo
    photo = cv2.flip(photo,1)       # Fliping the photo for mirror view
    width  = int(cap.get(3))  # float `width`
    height = int(cap.get(4))  # float `height
    
    leftWidth =int(width*0.33)
    rightWidth =int(width*0.75)
    upperHeight = int(height*0.75)
    lowerHeight = int(height*0.4)
    cropu1 = photo[lowerHeight:upperHeight,leftWidth:rightWidth]      # Middle part of the photo
    
    
    gray = cv2.cvtColor(cropu1, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 10, 70)
    ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)
    cv2.imshow('Video feed', mask)
    
    #cv2.imshow("cropu1",cropu1)     # It will show cropu1 part in a window     
    if cv2.waitKey(50) == 13 :      # Specifying (Enter) button to break the loop
        break
cap.release()
cv2.destroyAllWindows()
