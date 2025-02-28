import cv2
import numpy as np

def calculate_altitude_factor(altitude):
    """Yüksekliğe bağlı ölçek faktörünü hesaplar."""
    return 1 / altitude if altitude > 0 else 1

def draw_detections(frame, detections, altitude):
    """Tespit edilen nesneleri çerçeve üzerine çizer."""
    for detection in detections:
        x1, y1, x2, y2 = map(int, detection.boxes.xyxy[0])
        conf = float(detection.boxes.conf[0])
        class_id = int(detection.boxes.cls[0])
        class_name = detection.names[class_id]
        
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{class_name}: {conf:.2f}"
        cv2.putText(frame, label, (x1, y1 - 10), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    
    # Yükseklik bilgisini ekle
    cv2.putText(frame, f"Altitude: {altitude}m", (10, 30), 
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    
    return frame 