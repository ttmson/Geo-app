from ultralytics import YOLO
import cv2

model = YOLO('best.pt')  # Thay bằng mô hình đã huấn luyện

def detect_shapes(img_array):
    results = model(img_array)
    boxes = results[0].boxes
    shapes = []
    for box in boxes:
        cls = int(box.cls[0])
        label = model.names[cls]
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        shapes.append({'label': label, 'bbox': [x1, y1, x2, y2]})
        cv2.rectangle(img_array, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(img_array, label, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    return img_array, shapes
