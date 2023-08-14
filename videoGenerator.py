import os
import cv2

path = '/Users/zeynep/Desktop/archive/neutral/'
outputPath = '/Users/zeynep/Desktop/archive/'
outputVideoName = 'neutral144x144.mp4'
outputVideoFullPath = outputPath + outputVideoName
print(outputVideoFullPath)

preImgs = os.listdir(path)
#print(preImgs)

img = []

for i in preImgs:
    i = path + i
    #print(i)
    img.append(i)

print(img[0])
#print(img)

cv2_fourcc = cv2.VideoWriter_fourcc(*'mp4v')

assert os.path.exists(img[0])

frame = cv2.imread(img[0])
size = (frame.shape[1]*3, frame.shape[0]*3) #yeni
#print(frame)
#size = list(frame.shape)
#del size[2]
#size.reverse()
print(size)

video = cv2.VideoWriter(outputVideoFullPath, cv2_fourcc, 24, size) #output vid name, fourcc, fps, size

for i in range(len(img)):
    #video.write(cv2.imread(img[i]))
    #print("frame ", i+1, "of",len(img))
    img_frame = cv2.imread(img[i])   #yeni
    if img_frame is not None:  # Check if the image frame is loaded successfully
        resized_frame = cv2.resize(img_frame, size)  # Resize the image frame
        video.write(resized_frame)
        print("Frame", i + 1, "of", len(img))
    else:
        print("Failed to load image frame:", img[i])

video.release()

print("generated video to", outputPath)