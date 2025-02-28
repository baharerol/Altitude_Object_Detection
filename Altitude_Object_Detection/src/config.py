class Config:
    # YOLO model ayarları
    YOLO_MODEL = "yolov8n.pt"  # veya başka bir YOLO modeli
    CONFIDENCE_THRESHOLD = 0.5
    
    # Video işleme ayarları
    FRAME_WIDTH = 640
    FRAME_HEIGHT = 480
    
    # Nesne takip ayarları
    ALTITUDE_FACTOR = 0.1  # metre başına ölçek faktörü 