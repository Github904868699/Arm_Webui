import cv2

cap = cv2.VideoCapture(2)
i = 0
while True:
    print(i)
    if i >= 5:
        break
    ret, frame = cap.read() #读取一帧图像
    if not ret:

        break
    print(frame.shape)
    frame1 = cv2.resize(frame, (2560, 720))
    print(frame1.shape)
    # print(frame1.shape)
    cv2.imwrite('/home/arm003/snap/data/img/img.jpg', frame1) #保存为JPEG格式
    # break

    i += 1


cap.release() #释放摄像头资源
cv2.destroyAllWindows() #销毁所有窗口
