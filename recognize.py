import cv2
import sys
import os
import numpy as np


class FaceDetectionError(Exception):
    pass


def extractFace(img, train=False):
    path = '/Users/ethknig/haarcascade_frontalface_default.xml'
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


def predict(img):
    return recognizer.predict(img)


def faceProcess(img):
    faces = extractFace(img, True)
    faces = sorted(faces, key=lambda x: x[2]*x[3], reverse=True)
    try:
        return crop(img, faces[0])
    except IndexError:
        raise FaceDetectionError("No face was detected")


def loadImagesFromFolder(folder):
    # based off of
    # http://stackoverflow.com/questions/30230592/loading-all-images-using-imread-from-a-given-folder
    images = []
    print(os.listdir(folder))
    for filename in os.listdir(folder):
        print(os.path.join(folder, filename))
        img = cv2.imread(
            os.path.join(folder, filename), cv2.CV_LOAD_IMAGE_GRAYSCALE)
        if img is not None:
            images.append(img)
    return images


def trainStep(folder, label):
    label = np.array(label)
    imgs = loadImagesFromFolder(folder)
    print(len(imgs))
    return [[faceProcess(i) for i in imgs], np.array([label for x in imgs])]


def trainAll(folders):
    totalFaces = []
    totalLabels = []
    for i in enumerate(folders):
        working = trainStep(i[1], i[0])
        totalFaces.extend(working[0])
        totalLabels.extend(working[1])
        print(totalLabels)
    recognizer.train(totalFaces, np.array(totalLabels))


def ri(img):
    # stands for read image but is abreviated because I use it so much
    return cv2.imread(img, cv2.CV_LOAD_IMAGE_GRAYSCALE)


def main(folders):
    global recognizer
    recognizer = cv2.createLBPHFaceRecognizer()
    trainAll(folders)
    vidcap = cv2.VideoCapture('/Users/ethknig/shaqisback.mp4')
    cv2.namedWindow("The Luca Bazooka", cv2.cv.CV_WINDOW_AUTOSIZE)
    w = int(vidcap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH))
    h = int(vidcap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT))
    fourcc = cv2.cv.CV_FOURCC(*'XVID')
    video_writer = cv2.VideoWriter("output3.avi", fourcc, 25, (w, h))
    while True:
        ret, frame = vidcap.read()
        faces = extractFace(frame)
        for i in faces:
            (x, y, w, h) = i
            predicted = predict(
                cv2.cvtColor(crop(frame, i), cv2.COLOR_RGB2GRAY))
            cv2.imshow(
                'test', cv2.cvtColor(crop(frame, i), cv2.COLOR_RGB2GRAY))
            print(predicted)
            if predicted[1] <= 150:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (227, 45, 45), 2)
                cv2.putText(
                    frame, folders[predicted[0]], (x, y), cv2.FONT_HERSHEY_SIMPLEX, 3, (255, 255, 255))
            else:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 191, 255), 2)
        cv2.imshow("The Luca Bazooka", frame)
        video_writer.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vidwrite.release()
    video_capture.release()
    cv2.destroyAllWindows()