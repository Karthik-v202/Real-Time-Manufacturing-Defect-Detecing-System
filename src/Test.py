import cv2
from ultralytics import YOLO

model = YOLO("C:/Users/HP/Desktop/datasets/Welding/Model/best.pt")

result = model.predict("C:\\Users\\HP\\Desktop\\datasets\\Welding\\Test\\IMG_20260211_1133533.jpg", conf=0.25)

img = result[0].plot()

cv2.imwrite("C:/Users/HP/Desktop/datasets/Welding/Test-Result/Result-10.jpg", img)
