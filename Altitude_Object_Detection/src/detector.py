from ultralytics import YOLO
import cv2
from .config import Config
from .utils import calculate_altitude_factor, draw_detections

class ObjectDetector:
    def __init__(self):
        self.model = YOLO(Config.YOLO_MODEL)
        self.conf_threshold = Config.CONFIDENCE_THRESHOLD
    
    def detect_objects(self, frame, altitude):
        """
        Verilen kare üzerinde nesne tespiti yapar
        """
        # YOLO ile tespit
        results = self.model(frame, conf=self.conf_threshold)
        
        # Yükseklik faktörünü hesapla
        altitude_factor = calculate_altitude_factor(altitude)
        
        # Sonuçları görselleştir
        annotated_frame = draw_detections(frame, results, altitude)
        
        return annotated_frame, results 