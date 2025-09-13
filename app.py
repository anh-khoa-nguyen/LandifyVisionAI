# app.py

from fastapi import FastAPI, File, UploadFile, HTTPException
import uvicorn # Cần cho việc chạy local, nhưng HF Spaces sẽ tự xử lý
import time

# --- Tạm thời comment các import nặng để test deploy trước ---
# import cv2
# from vietocr.tool.predictor import Predictor
# from vietocr.tool.config import Cfg
# from deepface import DeepFace

app = FastAPI(
    title="Landify Vision AI API",
    description="API cho các tác vụ OCR và Xác minh khuôn mặt.",
    version="1.0.0"
)

# --- KHỞI TẠO MODEL (SẼ BỎ COMMENT SAU) ---
# print("Đang tải model VietOCR...")
# config = Cfg.load_config_from_name('vgg_transformer')
# config['weights'] = 'https://path/to/your/vietocr_weights.pth' # Thay bằng đường dẫn thật
# config['device'] = 'cpu' # BẮT BUỘC dùng CPU cho bậc miễn phí
# vietocr_predictor = Predictor(config)
# print("✅ Tải model VietOCR thành công.")


@app.get("/")
def read_root():
    """Endpoint gốc để kiểm tra service có hoạt động không."""
    return {"message": "Chào mừng đến với Landify Vision AI Service!"}


# Endpoint giả lập cho OCR CCCD
@app.post("/ocr/cccd")
async def ocr_id_card(image: UploadFile = File(...)):
    """
    Nhận một ảnh CCCD và (giả lập) trả về thông tin trích xuất.
    """
    if not image.content_type.startswith("image/"):
        raise HTTPException(status_code=400, detail="File tải lên phải là một hình ảnh.")

    # --- TÍCH HỢP LOGIC THẬT CỦA BẠN VÀO ĐÂY ---
    # 1. Đọc file ảnh: contents = await image.read()
    # 2. Dùng OpenCV để tiền xử lý
    # 3. Dùng VietOCR để nhận dạng
    # ---------------------------------------------

    # Giả lập thời gian xử lý trên CPU
    print("Bắt đầu xử lý OCR (giả lập)...")
    time.sleep(5) # Giả lập 5 giây xử lý
    print("...Xử lý OCR hoàn tất.")

    # Trả về dữ liệu giả lập
    return {
        "message": "Đọc thông tin CCCD thành công (dữ liệu giả lập).",
        "data": {
            "id": "012345678910",
            "name": "NGUYEN VAN A",
            "dob": "01/01/1990",
            "sex": "Nam",
            "nationality": "Việt Nam",
            "home": "Hà Nội",
            "address": "Số 1, Đường ABC, Phường XYZ, Quận 1, TP. HCM",
            "doe": "31/12/2030"
        }
    }

# Nếu bạn muốn chạy thử trên máy local:
# Mở terminal, gõ: uvicorn app:app --reload```

