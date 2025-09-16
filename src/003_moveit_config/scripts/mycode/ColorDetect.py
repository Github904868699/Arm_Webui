import cv2
import numpy as np

from ShapeAnalysis import cv_show

cap = cv2.VideoCapture(7)

def color_detection(frame):

    lower_red = np.array([0, 43, 46])
    upper_red = np.array([15, 255, 255])

    lower_blue = np.array([100, 43, 46])
    upper_blue = np.array([124, 255, 255])

    lower_yellow = np.array([20, 40, 40])
    upper_yellow = np.array([40, 255, 255])

    lower_black = np.array([0, 0, 0])
    upper_black = np.array([180, 255, 50])

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    blue_mask = cv2.inRange(hsv_frame, lower_blue, upper_blue)
    black_mask = cv2.inRange(hsv_frame, lower_black, upper_black)
    yellow_mask = cv2.inRange(hsv_frame, lower_yellow, upper_yellow)

    kernel = np.ones((5, 5), np.uint8)
    red_mask = cv2.morphologyEx(red_mask, cv2.MORPH_OPEN, kernel)
    blue_mask = cv2.morphologyEx(blue_mask, cv2.MORPH_OPEN, kernel)
    black_mask = cv2.morphologyEx(black_mask, cv2.MORPH_OPEN, kernel)
    yellow_mask = cv2.morphologyEx(yellow_mask, cv2.MORPH_OPEN, kernel)

    color = ""
    contours, _ = cv2.findContours(red_mask + blue_mask + black_mask + yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        # if cv2.contourArea(contour) > 500:  
        if np.any(blue_mask[y:y + h, x:x + w]):
            color = "蓝色"
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        elif np.any(yellow_mask[y:y + h, x:x + w]):
            color = "黄色"
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        elif np.any(black_mask[y:y + h, x:x + w]):
            color = "黑色"
            # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 2)
        else :
            color = "红色"
                # cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # cv2.putText(frame, color, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    if color == "" :
        color = "红色"
        # print(color)

    return color

def cv_show(name, image):
    cv2.imshow(name, image)
    cv2.waitKey(0)


while True:

    ret, frame = cap.read()


    result = [0, 0, 0,0 ,0 ,0 ,0 ,0 ]
    man1 = frame[330:600, 340:640]
    man2 = frame[330:600, 630:970]
    man3 = frame[330:600, 970:1270]
    man4 = frame[330:600, 1270:1530]
    man5 = frame[600:850, 360:670]
    man6 = frame[600:850, 670:970]
    man7 = frame[600:850, 970:1270]
    man8 = frame[600:850, 1270:1500]
    # # print(man)
    man = frame[300:900, 300:1600]
    cv_show('man1', man)

    cv_show('man1', man1)
    cv_show('man2', man2)
    cv_show('man3', man3)
    cv_show('man4', man4)
    cv_show('man5', man5)
    cv_show('man6', man6)
    cv_show('man7', man7)
    cv_show('man8', man8)

    # result = color_detect180ion(frame)
    result[0] = color_detection(man1)
    result[1] = color_detection(man2)
    result[2] = color_detection(man3)
    result[3] = color_detection(man4)
    result[4] = color_detection(man5)
    result[5] = color_detection(man6)
    result[6] = color_detection(man7)
    result[7] = color_detection(man8)
    print(result)
    
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # break

cap.release()
cv2.destroyAllWindows()