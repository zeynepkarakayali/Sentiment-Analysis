import os
import cv2

path = '/Users/zeynep/Desktop/archive/neutral/' #to be changed
outputPath = '/Users/zeynep/Desktop/archive/' #to be changed
outputVideoName = 'neutral48x48.mp4'
outputVideoFullPath = outputPath + outputVideoName
#print(outputVideoFullPath)

preImgs = os.listdir(path)
img_paths = [os.path.join(path, img) for img in preImgs]
#print(preImgs)

"""
img = []

for i in preImgs:
    i = path + i
    #print(i)
    img.append(i)

print(img[0])
#print(img)"""

cv2_fourcc = cv2.VideoWriter_fourcc(*'avc1')  # for H.264 format

assert os.path.exists(img_paths[0])

frame = cv2.imread(img_paths[0])
size = (frame.shape[1], frame.shape[0]) 
#print(frame)
#size = list(frame.shape)
#del size[2]
#size.reverse()
#print(size)

video = cv2.VideoWriter(outputVideoFullPath, cv2_fourcc, 24, size) #output vid name, fourcc, fps, size

for img_path in img_paths:
    img_frame = cv2.imread(img_path)
    
    if img_frame is not None:
        resized_frame = cv2.resize(img_frame, size)
        for _ in range(int(1.5 * 24)):  # Display each image for 1.5 seconds
            video.write(resized_frame)
        print("Added", img_path, "to video")
    else:
        print("Failed to load image frame:", img_path)


video.release()

print("generated video to", outputPath)