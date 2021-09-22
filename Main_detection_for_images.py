import cv2
import cv2 as cv
fileName = "img/crowd.jpg"
haaName = "haarcascade_frontalface_default.xml"

def faceDetect(fileName):
    #读取分类器
    face_cascade = cv.CascadeClassifier(cv.haarcascades+haaName)
    #读取文件
    img = cv.imread(fileName)
    #图片转为灰度图
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    #进行人脸识别
    faces = face_cascade.detectMultiScale(img,1.3,5)
    #绘制矩形
    for(x,y,w,h) in faces:
        img = cv.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    #显示结果
    cv.imshow(fileName,img)
    cv2.waitKey(0)


if __name__ == '__main__':
    faceDetect(fileName)

