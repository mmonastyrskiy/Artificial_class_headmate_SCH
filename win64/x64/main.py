import cv2
import numpy as np
import os
import datetime
# Список имен для id
names = ['None', 'Max',"Uchitel"]

inSchool = [[False,None] for i in range(0,len(names))]
print(inSchool)

def getImagesAndLabels(path):
    # Создаем список файлов в папке patch
    imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
    face=[] # Тут храним масив картинок
    ids = [] # Храним id лица
    for imagePath in imagePaths:
        img = cv2.imread(imagePath)
        # Переводим изображение в серый, тренер понимает только одноканальное изображение
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        face.append(img)
        # Получаем id из названия
        id = int(os.path.split(imagePath)[-1].split(".")[1])
        ids.append(id)
    return face,ids 

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('face/face.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);
# Тип шрифта
font = cv2.FONT_HERSHEY_SIMPLEX

# iniciate id counter
id = 0

cam = cv2.VideoCapture(0)
cam.set(3, 640)  # set video width
cam.set(4, 480)  # set video height

while True:
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(10, 10),
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        id, confidence = recognizer.predict(gray[y:y + h, x:x + w])

        # Проверяем что лицо распознано
        if (confidence < 70):
            id = names[id]
            #print(names.index(id))
            inSchool[(names.index(id))][0] = True
            if inSchool[(names.index(id))] [1]== None:
            	inSchool[(names.index(id))][1] = str(datetime.datetime.now())
            print(inSchool)
            with open("log.log","w") as f:
                for student in range(0,len(inSchool)):
                    for status in range(0,2):
                        f.write(str(inSchool[student][status]))
                        f.write(" ")
                    f.write('\n')
            confidence = "  {0}%".format(round(100 - confidence))
        else:
            id = "unknown"
            confidence = "  {0}%".format(round(100 - confidence))

        cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)

    cv2.imshow('camera', img)

    k = cv2.waitKey(10) & 0xff  # 'ESC' для Выхода
    if k == 27:
        break

cam.release()
cv2.destroyAllWindows()
os.system("pause")
