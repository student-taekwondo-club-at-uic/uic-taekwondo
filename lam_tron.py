from PIL import Image, ImageDraw

anh = Image.open("static/images/logo.png").convert("RGBA")

# Cắt phần vuông ở giữa ảnh
w, h = anh.size
canh = min(w, h)
anh = anh.crop(((w - canh) // 2, (h - canh) // 2, (w + canh) // 2, (h + canh) // 2))

# Làm tròn: phần ngoài hình tròn thành trong suốt
mask = Image.new("L", (canh, canh), 0)
ImageDraw.Draw(mask).ellipse((0, 0, canh, canh), fill=255)
anh.putalpha(mask)

anh.resize((256, 256), Image.LANCZOS).save("static/images/favicon.png")
print("Xong! Đã tạo static/images/favicon.png")