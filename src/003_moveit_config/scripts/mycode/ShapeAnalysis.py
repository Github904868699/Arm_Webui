
import cv2 as cv
import numpy as np


class ShapeAnalysis:
  
    def analysis(frame):

        h, w, ch = frame.shape
        result = np.zeros((h, w, ch), dtype=np.uint8)

        # 二值化图像
        print("start to detect lines...\n")

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY_INV | cv.THRESH_OTSU)
        # cv.imshow("input image", frame)

        contours, hierarchy = cv.findContours(binary, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

        for cnt in range(len(contours)):

            # 轮廓逼近
            epsilon = 0.01 * cv.arcLength(contours[cnt], True)
            approx = cv.approxPolyDP(contours[cnt], epsilon, True)

            # 分析几何形状
            corners = len(approx)
            shape_type = ""


            if corners == 4:
                shape_type = "矩形"

            elif corners >= 10:
                shape_type = "圆形"

            elif 4 < corners < 10:
                shape_type = "多边形"

            else :
                shape_type = "三角形"

            # shape_type = "圆形"
            # 求解中心位置
            # mm = cv.moments(contours[cnt])
            # cx = int(mm['m10'] / mm['m00'])
            # cy = int(mm['m01'] / mm['m00'])
            # cv.circle(result, (cx, cy), 3, (0, 0, 255), -1)

            # # 颜色分析
            # color = frame[cy][cx]
            # color_str = "(" + str(color[0]) + ", " + str(color[1]) + ", " + str(color[2]) + ")"

            # # 计算面积与周长
            # p = cv.arcLength(contours[cnt], True)
            # area = cv.contourArea(contours[cnt])

        print("识别到物体形状为", shape_type)

        return shape_type


def cv_show(name, image):
    cv.imshow(name, image)
    cv.waitKey(0)



if __name__ == "__main__":

    cap = cv.VideoCapture(2)
    # k = cv.waitKey(1) & 0xFF
    while (1):
        print(1)
        ret, frame = cap.read()
        # print(frame)
        # man = frame[500:900, 580:950]
        man = frame[400:800,600:1000]

        cv_show('man', man)
        shape = ShapeAnalysis.analysis(man)
        print(shape)
        # if k == ord('s'):  # ����s������������ı���ͼƬ����
        #     # src = cv.imread("D:/img/5.jpg")
        #     ld = ShapeAnalysis()
        #     shape = ld.analysis(frame)
        #     print(shape)
        #     cv.waitKey(0)
        #     cv.destroyAllWindows()