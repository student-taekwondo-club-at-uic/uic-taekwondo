# Web CLB Võ

## Chạy web
    pip install -r requirements.txt
    python app.py
Mở trình duyệt: http://127.0.0.1:5001

## Sửa nội dung
- Tên CLB, thành viên, sự kiện, câu hỏi trắc nghiệm: sửa trong `app.py` (phần đầu file)
- Nội dung About us: `templates/about.html`
- Màu chủ đạo: dòng `--chinh` trong `static/css/style.css`

## Thêm ảnh (bỏ vào static/images/)
- logo.png       -> logo trên menu
- banner.jpg     -> ảnh nền trang chủ
- about.jpg      -> ảnh trang About us
- Ảnh thành viên / sự kiện: đặt tên đúng như trường "anh" trong app.py
Chưa có ảnh thì web tự hiện khung "Chưa có ảnh".
