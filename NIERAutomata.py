import ps.path as p
import cv2
import os
faces = [0 for _ in range (5000)]

def addNewPhoto(img,sid):
	cv2.imwrite("guaranteed_face\\" + str(sid) + "." + str(int(faces[sid] + 1)))
		return 0
def CleanUp():
	if p.exists("guaranteed_face"):
		os.system("rm guaranteed_face\\*")
	else:
		p.mkdir("guaranteed_face")


