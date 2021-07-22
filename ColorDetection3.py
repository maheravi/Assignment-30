import cv2
import numpy as np

my_video = cv2.VideoCapture(0, cv2.CAP_DSHOW)
validation, frame = my_video.read()

FrameSize = (frame.shape[1], frame.shape[0])
# out = cv2.VideoWriter('Video_output3.mp4', cv2.VideoWriter_fourcc(*'MJPG'), 20, FrameSize, 0)

while True:

    validation, frame = my_video.read()

    if validation is not True:
        break

    # white_mask = cv2.inRange(frame_gray, 190, 255)
    # gray_mask = cv2.inRange(frame_gray, 80, 189)
    # black_mask = cv2.inRange(frame_gray, 0, 79)

    x = 100
    y = 100
    w = 100
    h = 100

    detector = frame[x:x + w, y:y + h]
    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 8)
    frame = cv2.blur(frame, (49, 49))
    frame[x:x + w, y:y + h] = detector
    colorB, colorG, colorR = cv2.split(detector)
    colorG = np.average(colorG)
    colorB = np.average(colorB)
    colorR = np.average(colorR)
    print(colorB, colorG, colorR)

    if 40 < colorB < 192 and 40 < colorG < 190 and 40 < colorR < 192:
        cv2.putText(frame, "gray", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    elif 190 < colorB < 255 and 190 < colorG < 255 and 190 < colorR < 255:
        cv2.putText(frame, "white", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    elif colorB < 40 and 0 < colorG < 40 and 0 < colorR < 40:
        cv2.putText(frame, "black", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    elif 128 < colorB < 255 and 0 < colorG < 160 and 128 < colorR < 255:
        cv2.putText(frame, "magenta", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    elif 100 < colorB < 255 and 0 < colorG < 190 and 0 < colorR < 190:
        cv2.putText(frame, "blue", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    elif 0 < colorB < 130 and 0 < colorG < 160 and 128 < colorR < 255:
        cv2.putText(frame, "red", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    elif 0 < colorB < 120 and 100 < colorG < 255 and 100 < colorR < 255:
        cv2.putText(frame, "yellow", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    elif 0 < colorB < 160 and 128 < colorG < 255 and 0 < colorR < 160:
        cv2.putText(frame, "green", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    elif 128 < colorB < 255 and 128 < colorG < 255 and 0 < colorR < 160:
        cv2.putText(frame, "cyan", (10, 50), cv2.FONT_HERSHEY_COMPLEX, 1, 1)

    cv2.imshow('output', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

my_video.release()
# out.release()
cv2.destroyAllWindows()

print("The video was successfully saved")
