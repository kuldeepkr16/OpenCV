import cv2
import time

import ScreenControl
import ScreenLock
import StaticImpli


class Detector:

    def __init__(self):
        self.frontFist_cascade = cv2.CascadeClassifier('FistFront.xml')
        self.palm_cascade = cv2.CascadeClassifier('palm.xml')
        self.face_cascade = cv2.CascadeClassifier('frontalface_default.xml')
        self.cap = cv2.VideoCapture(0)

    def start_detecting(self):

        while True:
            ret, img = self.cap.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

            # tuples of coordinates where fist, palm and face detected
            fist = self.frontFist_cascade.detectMultiScale(gray, 1.3, 5)
            palm = self.palm_cascade.detectMultiScale(gray, 1.3, 5)
            face = self.face_cascade.detectMultiScale(gray, 1.3, 5)

            # detecting fist
            print(fist)
            # when fist is being detected
            if len(fist) != 0:
                c = StaticImpli.counter(0)
                print("waiting for 10 times to lock. Waited: ", c, " time(s)")
                if c == 10:
                    ScreenLock.screen_lock()
                    exit()

            # detecting face
            print(face)
            # when face is not detected
            if len(face) == 0:
                c = StaticImpli.counter(0)
                print("waiting for 10 times to not detect a face. Waited: ", c, " time(s)")
                if c == 10:
                    ScreenControl.screen_dim()
                    # time.sleep(10)
                    StaticImpli.counter(1)

            # when face is being detected
            if len(face) != 0:
                StaticImpli.counter(1)
                ScreenControl.screen_bright()
                # time.sleep(10)

            # detecting palm
            # print(palm)

            # draw rectangles around objects
            for (x, y, w, h) in fist:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

            for (x, y, w, h) in palm:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)

            for (x, y, w, h) in face:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)

            cv2.imshow('img', img)

            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
        self.cap.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    d = Detector()
    d.start_detecting()


