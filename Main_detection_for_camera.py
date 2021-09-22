import cv2 as cv

# Load haarcascade
haaName = "haarcascade_frontalface_default.xml"

def faceDetectInit():
    # 读取分类器
    face_cascade = cv.CascadeClassifier(cv.haarcascades + haaName)
    cap = cv.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        exit()
    return face_cascade,cap

def faceDetect(fc,frame):
    # 图片转为灰度图
    imgGray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # 进行人脸识别
    faces = fc.detectMultiScale(frame, 1.3, 5)
    # 返回检测结果
    return faces

def showVideo(fc,cap):
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        # Face detection
        faces = faceDetect(fc,frame)
        # 绘制矩形
        for (x, y, w, h) in faces:
            frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        # Display the resulting frame
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    fc,cap = faceDetectInit()
    showVideo(fc,cap)
