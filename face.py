import numpy as np
import cv2
import tensorflow as tf
import pandas as pd
from pandas import DataFrame

#f= open("predictions.txt", 'w')

face_detection = cv2.CascadeClassifier('haar_cascade_face_detection.xml')

camera = cv2.VideoCapture(0)#"C:\\Users\\ACER\\Downloads\DAKİKA DAKİKA GÜNEYDOĞU DEPREMİNDE NELER YAŞANDI_ CÜNEYT ÖZDEMİR CANLI BAĞLANTILARLA ANLATTI... (1080p_30fps_H264-128kbit_AAC).mp4"#)
camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1024)
camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)
settings = {
	'scaleFactor': 1.3, 
	'minNeighbors': 5, 
	'minSize': (50, 50)
}

labels = ['Surprise', 'Neutral', 'Anger', 'Happy', 'Sad']

model = tf.keras.models.load_model("network-5Labels.h5")
durumSet = {
	'Surprise' : [],
	'Neutral' : [],
	'Anger' : [],
	'Happy' : [],
	'Sad' : [],
}
durum = []
value = []
valueMax = []
while True:
	ret, img = camera.read()
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	detected = face_detection.detectMultiScale(gray, **settings)
    
	for x, y, w, h in detected:
		cv2.rectangle(img, (x, y), (x+w, y+h), (245, 135, 66), 2)
		cv2.rectangle(img, (x, y), (x+w//3, y+20), (245, 135, 66), -1)
		face = gray[y+5:y+h-5, x+20:x+w-20]
		face = cv2.resize(face, (48,48)) 
		face = face/255.0
		
		predict = model.predict(np.array([face.reshape((48,48,1))]))
		predictions = model.predict(np.array([face.reshape((48,48,1))])).argmax()
		##f.write(predictions.astype(str) + '\n')
		value.append(predict)
		valueMax.append(predict[0][predictions])
		state = labels[predictions]
		durumSet[state].append(predict[0][predictions])
		durum.append(state)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(img,state,(x+10,y+15), font, 0.5, (255,255,255), 2, cv2.LINE_AA)
		
	cv2.imshow('Facial Expression', img)

	if cv2.waitKey(5) != -1:
		break
for i in durumSet:
	durumSet[i] = [sum(durumSet[i])]
#durumSet['FrameState'] = durum
#durumSet['FrameVal'] = valueMax

#durumVal = durumSet.values
df1 = DataFrame.from_dict(durumSet)
df2 = DataFrame({'FrameState' : durum , 'FrameVal' : valueMax})
df = pd.concat([df1, df2])
df.to_excel('cikti.xlsx')

camera.release()
cv2.destroyAllWindows()