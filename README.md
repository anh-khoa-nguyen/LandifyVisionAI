
### Bước 4: Cấu hình Space (`README.md`)

Đây là phần "ma thuật" của Hugging Face. Bạn sẽ thêm một vài dòng cấu hình ở đầu file `README.md`.

Tạo file `README.md`:

```yaml
---
title: Landify Vision AI
emoji: 👁️‍🗨️
colorFrom: blue
colorTo: green
sdk: docker
python_version: 3.9
app_file: app.py
---

# Landify Vision AI Service

Đây là dịch vụ backend xử lý các tác vụ Computer Vision cho dự án Landify.

- Endpoint `/ocr/cccd`: Nhận ảnh CCCD và trả về thông tin.
- Endpoint `/face/verify`: Sẽ được phát triển.

**Giải thích:**

*   `sdk: python`: Báo cho Hugging Face đây là một ứng dụng Python thuần.
*   `python_version: 3.9`: Chỉ định phiên bản Python.
*   `app_file: app.py`: Báo cho Hugging Face biết file nào là file chính để chạy.

### Bước 5: Tạo Space trên Hugging Face

1.  Đăng nhập vào [Hugging Face](https://huggingface.co/).
2.  Đi đến [huggingface.co/new-space](https://huggingface.co/new-space).
3.  **Owner:** Chọn tài khoản của bạn.
4.  **Space name:** Đặt tên, ví dụ: `landify-vision-ai`.
5.  **License:** Chọn `mit`.
6.  **Space SDK:** Chọn **Python**.
7.  **Space hardware:** Chọn **CPU basic • Free**.
8.  **Visibility:** Chọn **Public**.
9.  Nhấn **Create Space**.

### Bước 6: Đẩy Code lên (Sử dụng Git)

Sau khi tạo Space, Hugging Face sẽ cho bạn một trang với các lệnh Git. Hãy làm theo chúng:

1.  Mở terminal hoặc command prompt trên máy tính của bạn.
2.  Đi vào thư mục `LandifyVisionAI` bạn đã tạo ở Bước 1.
3.  Thực hiện các lệnh sau (thay `your-username` và `your-space-name` bằng thông tin của bạn):

    ```bash
    # Khởi tạo Git và kết nối với repo trên Hugging Face
    git init
    git remote add origin https://huggingface.co/spaces/your-username/your-space-name

    # Tải về các file cấu hình mà Hugging Face đã tạo sẵn (nếu có)
    git pull origin main

    # Thêm tất cả các file của bạn vào
    git add .

    # Commit thay đổi
    git commit -m "Initial commit for Vision AI service"

    # Đẩy code lên!
    git push origin main
    ```

**Xử lý file lớn (quan trọng!):** Các model AI thường rất nặng. GitHub/Hugging Face giới hạn kích thước file. Bạn cần dùng **Git LFS (Large File Storage)**.

```bash
# Cài đặt Git LFS (chỉ cần làm một lần)
git lfs install

# Báo cho Git LFS theo dõi các file model (ví dụ file .pth của VietOCR)
git lfs track "*.pth"
git lfs track "*.onnx"
git lfs track "*.h5"

# Đảm bảo file .gitattributes được thêm vào commit
git add .gitattributes

# Bây giờ bạn có thể commit và push như bình thường
git commit -m "Add model files with LFS"
git push origin main