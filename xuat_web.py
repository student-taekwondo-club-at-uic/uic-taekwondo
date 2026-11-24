"""Xuất web Flask thành file HTML tĩnh trong thư mục _site/ để đưa lên GitHub Pages.
Chạy: python3 xuat_web.py
"""
import json
import os
import shutil

from markupsafe import Markup

import app as web

THU_MUC_RA = "_site"

# Trên GitHub, web nằm ở ten.github.io/<tên repo>/ nên mọi link phải có thêm /<tên repo>
repo = os.environ.get("GITHUB_REPOSITORY", "").split("/")[-1]
GOC = "" if not repo or repo.endswith(".github.io") else "/" + repo
BASE_URL = f"http://localhost{GOC}/"

shutil.rmtree(THU_MUC_RA, ignore_errors=True)
shutil.copytree(web.app.static_folder, os.path.join(THU_MUC_RA, "static"))
client = web.app.test_client()


def ghi(duong_dan, html):
    thu_muc = os.path.join(THU_MUC_RA, duong_dan.strip("/"))
    os.makedirs(thu_muc, exist_ok=True)
    with open(os.path.join(thu_muc, "index.html"), "w", encoding="utf-8") as f:
        f.write(html)
    print("  ✓", duong_dan)


def chen_truoc_body(html, doan):
    return html.replace("</body>", doan + "\n</body>", 1)


# 1. Mọi trang bình thường (không cần dữ liệu gửi lên)
for rule in web.app.url_map.iter_rules():
    if rule.endpoint == "static" or rule.arguments or "GET" not in rule.methods:
        continue
    html = client.get(rule.rule, base_url=BASE_URL).get_data(as_text=True)

    # 2. Trang trắc nghiệm: chấm điểm bằng JavaScript thay cho Python
    if rule.endpoint == "trac_nghiem":
        diem = [[[dk, q] for _, dk, q in cau["lua_chon"]] for cau in web.CAU_HOI]
        html = chen_truoc_body(html, f"""<script>
  const DIEM = {json.dumps(diem)};
  document.querySelector("form.quiz").addEventListener("submit", e => {{
    e.preventDefault();
    let dk = 0, q = 0;
    for (let i = 0; i < DIEM.length; i++) {{
      const chon = document.querySelector(`input[name="cau${{i}}"]:checked`);
      if (!chon) {{ alert("Please answer every question!"); return; }}
      dk += DIEM[i][chon.value][0];
      q += DIEM[i][chon.value][1];
    }}
    const loai = dk - q >= 3 ? "dk" : q - dk >= 3 ? "q" : "ca_hai";
    location.href = "{GOC}/ket-qua/" + loai + "/?dk=" + dk + "&q=" + q;
  }});
</script>""")
    ghi(rule.rule, html)

# 3. Ba trang kết quả trắc nghiệm, điểm được điền vào bằng JavaScript
for loai, kq in web.KET_QUA.items():
    with web.app.test_request_context("/trac-nghiem", base_url=BASE_URL):
        html = web.render_template("ket_qua.html", kq=kq,
                                   dk=Markup('<span id="diem-dk">0</span>'),
                                   q=Markup('<span id="diem-q">0</span>'))
    html = chen_truoc_body(html, """<script>
  const p = new URLSearchParams(location.search);
  document.getElementById("diem-dk").textContent = p.get("dk") || 0;
  document.getElementById("diem-q").textContent = p.get("q") || 0;
</script>""")
    ghi(f"/ket-qua/{loai}/", html)

