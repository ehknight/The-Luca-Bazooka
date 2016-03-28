from __future__ import division
import cv2
import imageio
import sys
import os
from os.path import expanduser as eu
import numpy as np
from scipy import ndimage
from picamera.array import PiRGBArray
from picamera import PiCamera
import meme
import servo
#PARAMETERS
vidfeed=str(eu("~"))+'/classic.mp4' #0 usually corresponds to webcam feed
outputToFile=True
filename='output.avi'
confidenceLevel=125
debugStuff=True
rotate=True
showImage=True
cascadePath=str(eu("~"))+'/The-Luca-Bazooka/data/haarcascade_frontalface_default.xml'
trainingFolders=[str(eu("~"))+'/The-Luca-Bazooka/training/luca']
changeResolution=True
size=(.2,.2)
resolution = (640,480)
size = (640,480)
framerate = 32
visualizeLBP=True


class FaceDetectionError(Exception):
    pass


def extractFace(img, train=False):
    path = cascadePath
    cascade = cv2.CascadeClassifier(path)
    if train == True:
        faces = cascade.detectMultiScale(
            img, scaleFactor=1.1,
            minNeighbors=4,
            minSize=(50, 50),
            flags=cv2.CASCADE_SCALE_IMAGE)
    else:
        faces = cascade.detectMultiScale(
            img, scaleFactor=1.11,
            minNeighbors=5,
            minSize=(40, 40),
            flags=cv2.CASCADE_SCALE_IMAGE)
    return faces


def crop(img, c):
    x, y, w, h = c[0], c[1], c[2], c[3]
    return img[y:y+h, x:x+w]




def faceProcess(img):
    faces = extractFace(img, True)
    faces = sorted(faces, key=lambda x: x[2]*x[3], reverse=True)
    try:
        return crop(img, faces[0])
    except IndexError:
        cv2.imshow('Failed Detection',img)
        cv2.waitKey()
        #raise FaceDetectionError("No face was detected with img "+str(img))


def loadImagesFromFolder(folder):
    # based off of
    # http://stackoverflow.com/questions/30230592/loading-all-images-using-imread-from-a-given-folder
    images = []
    print(os.listdir(folder))
    for filename in os.listdir(folder):
        if debugStuff:
            print(os.path.join(folder, filename))
        img = cv2.imread(
            os.path.join(folder, filename), cv2.CV_LOAD_IMAGE_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images


def main(folders):
    servo = servo.Servo(8,10,53.5/640, 41.41/480,640,480,90,90)
    global recognizer
    trainAll(folders)
    if showImage:
        cv2.namedWindow("The Luca Bazooka", cv2.cv.CV_WINDOW_AUTOSIZE)
    camera=PiCamera()
    camera.resolution=resolution
    camera.framerate=framerate
    rawCapture=PiRGBArray(camera,size=size)
    video_writer=imageio.get_writer('~/The-Luca-Bazooka/'+filename,fps=24)
    for nonprocessed in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        frame=nonprocessed.array
        if rotate:
            frame=ndimage.rotate(frame,270)
        faces = extractFace(frame)
        for i in faces:
            (x, y, w, h) = i
            if showImage:
                cv2.imshow(
                'Detected Face', cv2.cvtColor(crop(frame, i), cv2.COLOR_RGB2GRAY))
            if showImage:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 191, 255), 2)
        if showImage:
            cv2.imshow("The Luca Bazooka", frame)
        if outputToFile==True:
            video_writer.append_data(frame)
        rawCapture.truncate(0)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    if outputToFile==True:
        video_writer.close()
    vidcap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main(trainingFolders)
