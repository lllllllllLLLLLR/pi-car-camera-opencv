# python控制摄像头
import cv2                                               # 导入 opencv-python

# Replace <raspberry-pi-ip> with the actual IP address printed by the Raspberry Pi
# (e.g. after `hostname -I` on the Pi, or from your router's device list).
stream_url = "http://<raspberry-pi-ip>:8080/?action=stream"
cap = cv2.VideoCapture(stream_url)                      # 获取视频的输入源，也就是这个网址

while True:
    ret, frame = cap.read()                             # 不停地从输入源读取一帧图像
    if not ret:                                         # 如果读取失败，结束循环
        break
    # 在这里进行图像处理
    processed_frame = frame                             # 我们这里先不对图像作操作
    # 显示图像
    cv2.imshow('Processed Frame', processed_frame)      # 显示获取到的图像
    # 按下 'q' 键退出
    if cv2.waitKey(1) & 0xFF == ord('q'):               # 检测 q 键有没有按下，按下就退出程序
        break

cap.release()                                           # 释放视频输入源
cv2.destroyAllWindows()                                 # 销毁所有的窗口
