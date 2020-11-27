# Live WebCam Capture

import cv2


def main():
    window = "Live Video Feed"
    cv2.namedWindow(window)
    cap = cv2.VideoCapture(0)  # (0) means if there are multiple cams attach then it will select the 1st webcam

    # check and read the if the cam is works or no
    if cap.isOpened():
        ret, frame = cap.read()
        print(ret)  # returns True/False
        print(frame)  # returns some values
    else:
        ret = False
        print(ret)

    while ret:
        ret, frame = cap.read()

        cv2.imshow(window, frame)
        if cv2.waitKey(1) == 27:
            break

    cv2.destroyAllWindows()
    cap.release()  # Releases the associated webcam


if __name__ == '__main__':
    main()
