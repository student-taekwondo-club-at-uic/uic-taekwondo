import os
from PIL import Image, ImageOps

TOI_DA = 1600   # cạnh dài nhất của ảnh sau khi thu nhỏ (pixel)


def thu_nho(thu_muc="static/images"):
    """Thu nhỏ mọi ảnh to trong thu_muc. Ảnh đã nhỏ thì bỏ qua."""
    tong_truoc = tong_sau = so_anh = 0
    for goc, _, ds_file in os.walk(thu_muc):
        for ten in ds_file:
            if not ten.lower().endswith((".jpg", ".jpeg", ".png")):
                continue
            duong = os.path.join(goc, ten)
            try:
                truoc = os.path.getsize(duong)
                anh = Image.open(duong)
                if max(anh.size) <= TOI_DA:
                    continue                                  # ảnh đã nhỏ sẵn, bỏ qua
                anh = ImageOps.exif_transpose(anh)            # giữ đúng chiều ảnh chụp bằng điện thoại
                anh.thumbnail((TOI_DA, TOI_DA))
                if ten.lower().endswith(".png"):
                    anh.save(duong, optimize=True)
                else:
                    anh.convert("RGB").save(duong, quality=85, optimize=True)
            except Exception as loi:
                print(f"Bỏ qua {duong}: {loi}")              # ảnh lỗi thì bỏ qua, không làm sập web
                continue
            sau = os.path.getsize(duong)
            tong_truoc += truoc
            tong_sau += sau
            so_anh += 1
            print(f"{duong}: {truoc // 1024} KB -> {sau // 1024} KB")
    if so_anh:
        print(f"Đã thu nhỏ {so_anh} ảnh: {tong_truoc // 1048576} MB -> {tong_sau // 1048576} MB")


if __name__ == "__main__":
    thu_nho()