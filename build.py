"""Tạo bản web đầy đủ trong docs/ để đăng lên GitHub Pages.

index.html ở thư mục gốc là bản nguồn (không có <!doctype>/<head>, vì claude.ai tự bọc).
Script này bọc nó thành trang HTML hoàn chỉnh và chép kèm âm thanh.
Chạy: python build.py
"""
import os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")

src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
title = re.search(r"<title>(.*?)</title>", src).group(1)
body = re.sub(r"<title>.*?</title>\s*", "", src, count=1)

page = f"""<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#74c26f">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="description" content="Game học Toán lớp 1: bé cùng các bạn thú giải toán để giải cứu muông thú.">
<title>{title}</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🐝</text></svg>">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);box-sizing:border-box}}</style>
</head>
<body>
{body}
</body>
</html>
"""

os.makedirs(DOCS, exist_ok=True)
open(os.path.join(DOCS, "index.html"), "w", encoding="utf-8", newline="\n").write(page)
open(os.path.join(DOCS, ".nojekyll"), "w").close()
dst = os.path.join(DOCS, "sounds")
os.makedirs(dst, exist_ok=True)
for f in os.listdir(os.path.join(ROOT, "sounds")):
    if f.endswith(".mp3"):
        shutil.copy2(os.path.join(ROOT, "sounds", f), dst)
print("docs/ ready")
