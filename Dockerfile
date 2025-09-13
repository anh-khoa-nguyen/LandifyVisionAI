# Bắt đầu từ một image Python 3.9 gọn nhẹ
FROM python:3.9-slim

# Đặt thư mục làm việc bên trong container
WORKDIR /code

# Sao chép file requirements.txt vào trước để tận dụng cache của Docker
COPY ./requirements.txt /code/requirements.txt

# Cài đặt các thư viện cần thiết
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Sao chép toàn bộ code của bạn (app.py, etc.) vào container
COPY . /code/

# Lệnh để chạy ứng dụng FastAPI khi container khởi động
# QUAN TRỌNG: Hugging Face Spaces yêu cầu chạy trên cổng 7860
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "7860"]

#FROM: Bắt đầu với một môi trường Python 3.9 sạch.
#WORKDIR: Tạo một thư mục tên là /code để chứa project.
#COPY và RUN pip install: Cài đặt tất cả các thư viện từ file requirements.txt của bạn.
#COPY . /code/: Chép toàn bộ project của bạn vào.
#CMD: Lệnh cuối cùng để khởi động server FastAPI. Hugging Face sẽ tự động expose cổng 7860 ra ngoài internet cho bạn.