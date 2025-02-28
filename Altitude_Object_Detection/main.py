import cv2
from src.detector import ObjectDetector
from src.config import Config

def main():
    # Video kaynağını başlat (0 için webcam, dosya yolu için video dosyası)
    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, Config.FRAME_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, Config.FRAME_HEIGHT)
    
    # Nesne detektörünü başlat
    detector = ObjectDetector()
    
    # Test için sabit yükseklik (gerçek uygulamada sensörden alınabilir)
    current_altitude = 10.0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Nesne tespiti yap
        annotated_frame, results = detector.detect_objects(frame, current_altitude)
        
        # Sonuçları göster
        cv2.imshow('Object Detection', annotated_frame)
        
        # 'q' tuşuna basılırsa çık
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main() 