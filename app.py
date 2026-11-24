import os 
from datetime import datetime, date
from flask import Flask, render_template, request



app = Flask(__name__)
# every time launch the web: automatically shrink the new-added images in static/images
from thu_nho_anh import thu_nho
thu_nho(os.path.join(app.static_folder, "images"))

# ============================================================
#  FIX THE CLUB INFORMATION HERE
#  Ảnh: bỏ file vào static/images/ rồi ghi đúng tên file vào "anh"
# ============================================================

CLB = {
    "ten": "Student Taekwondo Club @ UIC",
    "slogan": "COME PRACTICE WITH US!",
    "instagram": "https://www.instagram.com/studenttkdclub_uic/",
    "email": "taekwondo.club.uic@gmail.com",
}

BAN_HOI_DONG = [
    {"ten": "Eunce Kim", "chuc_vu": "President", "dai": "3rd Degree Black Belt",
     "gioi_thieu": "Senior, Biology Pre-pharm track", "anh": "president.jpg"},
    {"ten": "Alara Randle", "chuc_vu": "Vice President", "dai": "1st Degree Black Belt",
     "gioi_thieu": "Sophomore, Psychology", "anh": "vice-president.jpg"},
    {"ten": "Deone Lesley", "chuc_vu": "Treasurer", "dai": "Light Blue Belt",
     "gioi_thieu": "Senior, Engineering Management", "anh": "treasurer.jpg"},
    {"ten": "Gabija Gricius", "chuc_vu": "Publicity Chair", "dai": "Dark Blue Belt",
     "gioi_thieu": "Junior, Architecture & Minor in Real Estate", "anh": "media.jpg"},
    {"ten": "Jonathan Newman", "chuc_vu": "Secretary", "dai": "1st Degree Black Belt",
     "gioi_thieu": "Sophomore, Biomedical Engineering", "anh": "secretary.jpg"},
    {"ten": "Kevin Jones", "chuc_vu": "Event Coordinator", "dai": "Light Blue Belt",
     "gioi_thieu": "Senior, Integrated Health Studies Pre-Med", "anh": "event-coordinator.jpg"},
    {"ten": "Miguel Mendoza", "chuc_vu": "Coach", "anh": "2025-coach.png"},
]
# Timeline: xếp từ cũ tới mới. Ảnh album bỏ vào static/images/timeline/<tên album>/
# Ảnh ban hội đồng cũ bỏ vào static/images/ rồi ghi đúng tên file vào "anh"
GIAI_DOAN = [
    {"nam": "2026", "ten": "2026",
     "mo_ta": "Growing stronger as a community, both on and off the mat.",
     "album": "2026",
     "ban_hoi_dong": BAN_HOI_DONG},
     # tự lấy ban hội đồng hiện tại ở trên

    {"nam": "2025", "ten": "2025",
     "mo_ta": "Building connections, strengthening our team, and making memories.",
     "album": "2025",
     "ban_hoi_dong": [
         {"ten": "Miguel Mendoza", "chuc_vu": "Coach", "anh": "2025-coach.png"},
         {"ten": "Jida Sulieman", "chuc_vu": "Co-president", "anh": "2025-president.png"},
         {"ten": "Jeanna Vasquez", "chuc_vu": "Co-president", "anh": "2025-co-president.png"},
         {"ten": "Eunice Kim", "chuc_vu": "Vice president", "anh": "2025-vice-president.png"},
         {"ten": "Jason Jardiel", "chuc_vu": "Secretary", "anh": "2025-secretary.png"},
         {"ten": "Deone Lesley", "chuc_vu": "Treasurer", "anh": "2025-treasurer.png"},
         {"ten": "Aaron Shimon Iosevich", "chuc_vu": "Social Media", "anh": "2025-social-media-manager.png"}

     ]},

    {"nam": "2024", "ten": "2024",
     "mo_ta": "Practices at the MAC Suite, competing in tournaments.",
     "album": "2024",
     "ban_hoi_dong": [
         {"ten": "Jeanna Vasquez", "chuc_vu": "President", "anh": "2022-co-president.png"},
         {"ten": "Uzair Abdullah", "chuc_vu": "Treasurer", "anh": "2022-event-coordinator.png"},
         {"ten": "Jason Jardie", "chuc_vu": "Secretary", "anh": "2025-secretary.png"},
         {"ten": "Eunice Kim", "chuc_vu": "Vice president", "anh": "2025-vice-president.png"},
         {"ten": "Zoe Mcclain", "chuc_vu": "Social media", "anh": "2024-social-media.png"},


     ]},

    {"nam": "2022-2023", "ten": "2022-2023",
     "mo_ta": "First practices at the MAC Suite with several members.",
     "album": "2022-2023",
     "ban_hoi_dong": [
         {"ten": "Monica Padilla", "chuc_vu": "Co-president", "anh": "2022-president.png"},
         {"ten": "Joshua Patino", "chuc_vu": "Vice president", "anh": "2022-vice-president.png"},
         {"ten": "Jida Sulieman", "chuc_vu": "Secretary", "anh": "2022-secretary.png"},
         {"ten": "Uzair Abdullah", "chuc_vu": "Event Coordinator", "anh": "2022-event-coordinator.png"},
         {"ten": "Mahum Anwel", "chuc_vu": "Treasurer", "anh": "2022-treasurer.png"},
         {"ten": "Ritu Barman", "chuc_vu": "Social Meadia Manager", "anh": "2022-social-media-manager.png"}

     ]},
]

SU_KIEN = [
    {"ten": "MCTC: Midwest Collegiate Taekwondo Conference", "ngay": "10/24/2026", "dia_diem": "Waulkegan",
     "mo_ta": "Taekwondo big tournaments for every universities in the MidWest!", "anh": "event-1.jpg", "album" : "mctc"},
    {"ten": "North Suburbs Tournament", "ngay": "11/21/2026", "dia_diem": "North Suburbs",
     "mo_ta": "A tournament at the North Suburbs.", "anh": "event-2.jpg", "album" : "northshore"},
    {"ten": "Belt testing at the end semester", "ngay": "12/04/2026", "dia_diem": "UIC Gym",
     "mo_ta": "Periodically belt testing.", "anh": "event-3.jpg", "album" : "belt_test"},
    {"ten": "Practices !!!", "ngay": "2022-2026", "dia_diem": "UIC Gym",
     "mo_ta": "Average day in practices!", "anh": "event-4.jpg", "album" : "practices"},
    {"ten": "Overlay Fundraising", "ngay": "11/16/2026", "dia_diem": "1411 W Taylor St, Chicago, IL 60607",
     "mo_ta": "Sip for a cause! Treat yourself while supporting the UIC Taekwondo Club. Select our club at the check out!", "anh": "overlay.jpg", "album": "overlay","fundraising": True},

]

# Mỗi lựa chọn cộng điểm cho "dk" (đối kháng) và "q" (quyền)
CAU_HOI = [
    {"hoi": "What do you do in your free time?", "lua_chon": [
        ("Play combat sports games", 2, 0),
        ("Dance, do yoga, create something beautiful", 0, 2),
        ("Anything fun is worth playing", 1, 1)]},
    {"hoi": "How do you see yourself?", "lua_chon": [
        ("Competitive, aggressive", 2, 0),
        ("Patient, meticulous, perfectionist", 0, 2),
        ("Flexible, adaptable", 1, 1)]},
    {"hoi": "When watching a martial arts movie, what scene do you love the most?", "lua_chon": [
        ("The intense fight scene between two skilled fighters", 2, 0),
        ("The beautiful solo performance of a martial arts form", 0, 2),
        ("Any scene is great", 1, 1)]},
    {"hoi": "Being hit once, you would...", "lua_chon": [
        ("Defense, counterattack", 2, 0),
        ("Forget it, let me practice alone", 0, 2),
        ("A bit painful but okay", 1, 1)]},
    {"hoi": "What do you want to receive when participating in a competition?", "lua_chon": [
        ("Medal for defeating opponents", 2, 0),
        ("High scores from judges for beauty and precision", 0, 2),
        ("Both, a bit greedy", 1, 1)]},
    {"hoi": "When learning a new technique, you will...", "lua_chon": [
        ("Want to try applying it with a partner right away", 2, 0),
        ("Repeat it a hundred times for accuracy", 0, 2),
        ("Practice it well before trying to apply", 1, 1)]},
]

KET_QUA = {
    "dk": {"ten": "SPARRING", "icon": "🥊",
           "mo_ta": "You have a fighting spirit, quick reflexes, and a love for challenges. "
                    "The sparring group will help you improve your endurance, reflexes, and composure in the ring!"},
    "q": {"ten": "POOMSAE", "icon": "🥋",
          "mo_ta": "You are patient, meticulous, and have an aesthetic sense. The forms group will help you refine "
                   "your precision, fluidity, and focus through each form."},
    "ca_hai": {"ten": "BOTH", "icon": "⚔️",
               "mo_ta": "You balance strength and technique. Training in both sparring and forms "
                        "will help you develop the most comprehensive skills!"},
}


@app.context_processor
def them_thong_tin_clb():
    return {"clb": CLB}


@app.route("/")
def trang_chu():
    return render_template("home.html")


@app.route("/ban-hoi-dong")
def ban_hoi_dong():
    return render_template("ban_hoi_dong.html", thanh_vien=BAN_HOI_DONG)


@app.route("/trac-nghiem", methods=["GET", "POST"])
def trac_nghiem():
    if request.method == "POST":
        dk = q = 0
        for i, cau in enumerate(CAU_HOI):
            chon = request.form.get(f"cau{i}")
            if chon is None:
                return render_template("trac_nghiem.html", cau_hoi=CAU_HOI,
                                       loi="Make sure you answer all the questions!")
            _, diem_dk, diem_q = cau["lua_chon"][int(chon)]
            dk += diem_dk
            q += diem_q
        if dk - q >= 3:
            loai = "dk"
        elif q - dk >= 3:
            loai = "q"
        else:
            loai = "ca_hai"
        return render_template("ket_qua.html", kq=KET_QUA[loai], dk=dk, q=q)
    return render_template("trac_nghiem.html", cau_hoi=CAU_HOI)


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/timeline")
def timeline():
    for gd in GIAI_DOAN:
        thu_muc = os.path.join(app.static_folder, "images", "timeline", gd.get("album", ""))
        if gd.get("album") and os.path.isdir(thu_muc):
            gd["ds_anh"] = sorted(f for f in os.listdir(thu_muc)
                                  if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp", ".gif")))
        else:
            gd["ds_anh"] = []
    return render_template("timeline.html", giai_doan=GIAI_DOAN)


DUOI_ANH = (".jpg", ".jpeg", ".png", ".webp", ".gif")


def lay_album(ten):
    """Lấy ảnh trong static/images/album/<ten>/, chia nhóm theo thư mục con (vd: theo năm)."""
    goc = os.path.join(app.static_folder, "images", "album", ten)
    if not ten or not os.path.isdir(goc):
        return []
    nhom = []
    anh_le = sorted(f for f in os.listdir(goc) if f.lower().endswith(DUOI_ANH))
    if anh_le:
        nhom.append(("", [f"images/album/{ten}/{f}" for f in anh_le]))
    for con in sorted(os.listdir(goc)):
        if os.path.isdir(os.path.join(goc, con)):
            ds = sorted(f for f in os.listdir(os.path.join(goc, con)) if f.lower().endswith(DUOI_ANH))
            if ds:
                nhom.append((con, [f"images/album/{ten}/{con}/{f}" for f in ds]))
    return nhom

def doc_ngay(chuoi):
    """Đổi "10/24/2026" (tháng/ngày/năm) thành ngày. Ghi sai kiểu thì bỏ qua."""
    try:
        return datetime.strptime(chuoi, "%m/%d/%Y").date()
    except ValueError:
        return None


@app.route("/get-involved")
def get_involved():
    hom_nay = date.today()
    gay_quy = [(doc_ngay(sk["ngay"]), sk) for sk in SU_KIEN if sk.get("fundraising")]
    gay_quy = [(ngay, sk) for ngay, sk in gay_quy if ngay]
    sap_toi = sorted([x for x in gay_quy if x[0] >= hom_nay], key=lambda x: x[0])
    da_qua = sorted([x for x in gay_quy if x[0] < hom_nay], key=lambda x: x[0], reverse=True)
    if sap_toi:
        sk_gq, nhan_gq = sap_toi[0][1], "Upcoming fundraiser"
    else:
        sk_gq, nhan_gq = None, None
    return render_template("get_involved.html", sk_gq=sk_gq, nhan_gq=nhan_gq)


@app.route("/su-kien")
def su_kien():
    ds = [sk for sk in SU_KIEN if not sk.get("fundraising")]   # bỏ sự kiện gây quỹ
    for sk in ds:
        sk["nhom_anh"] = lay_album(sk.get("album", ""))
    return render_template("su_kien.html", su_kien=ds)


if __name__ == "__main__":
    app.run(debug=True, port=5001)
