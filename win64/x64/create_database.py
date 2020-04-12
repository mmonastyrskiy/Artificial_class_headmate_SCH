import cv2
import os
cam = cv2.VideoCapture(0)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
# Вводим id лица которое добавляется в имя и потом будет использовать в распознавание.
face_id = input('\n enter user id end press  ==>  ')
print("\n [INFO] Initializing face capture. Look the camera and wait …")
count = 0
while(True):
     ret, img = cam.read()  
     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
     faces = face_detector.detectMultiScale(gray, 1.3, 5)
     for (x,y,w,h) in faces:     
          cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
          count += 1     
          # Сохраняем лицо
          cv2.imwrite('face/user.' + str(face_id) + '.' + str(count) + '.jpg', gray[y:y+h,x:x+w])
     cv2.imshow('image', img)
     k = cv2.waitKey(100) & 0xff #  'ESC'  
     if k == 27:
         break 
     elif count >= 1000: # Если сохранили 100  изображений выход.
         break
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
os.system('pause')
