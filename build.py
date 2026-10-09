"""Tạo bản web cho GitHub Pages trong docs/.

  docs/index.html            trang chủ chọn game
  docs/muong-thu/            Bé Cứu Muông Thú (từ index.html + sounds/)
  docs/sudoku/               Sudoku Rừng Xanh (từ sudoku.html)

index.html và sudoku.html ở thư mục gốc là bản nguồn (không có <!doctype>/<head>,
vì claude.ai tự bọc). Script này bọc chúng thành trang HTML hoàn chỉnh.
Chạy: python build.py
"""
import os, re, shutil

ROOT = os.path.dirname(os.path.abspath(__file__))
DOCS = os.path.join(ROOT, "docs")

GAMES = [
    {"src": "index.html", "dir": "muong-thu", "icon": "🐝", "sounds": True,
     "desc": "Học Toán lớp 1: giải toán để cùng bạn thú đánh quái, giải cứu muông thú."},
    {"src": "sudoku.html", "dir": "sudoku", "icon": "🧩", "sounds": False,
     "desc": "Thử thách tư duy: Sudoku từ 4×4 hình con vật đến 9×9 cao thủ."},
]

HEAD = """<!doctype html>
<html lang="vi">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="theme-color" content="#74c26f">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="description" content="{desc}">
<title>{title}</title>
<link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>{icon}</text></svg>">
<style>:root{{padding-top:env(safe-area-inset-top,0px);padding-bottom:env(safe-area-inset-bottom,0px);box-sizing:border-box}}</style>
{extra}
</head>
<body>
"""


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def wrap(src, desc, icon, extra=""):
    title = re.search(r"<title>(.*?)</title>", src).group(1)
    body = re.sub(r"<title>.*?</title>\s*", "", src, count=1)
    return HEAD.format(title=title, desc=desc, icon=icon, extra=extra) + body + "\n</body>\n</html>\n", title


# bản cũ để game toán ngay ở docs/, dọn đi
for old in ("sounds",):
    shutil.rmtree(os.path.join(DOCS, old), ignore_errors=True)

cards = []
for g in GAMES:
    src = open(os.path.join(ROOT, g["src"]), encoding="utf-8").read()
    page, title = wrap(src, g["desc"], g["icon"], '<script>window.GAME_HUB = "../";</script>')
    write(os.path.join(DOCS, g["dir"], "index.html"), page)
    if g["sounds"]:
        dst = os.path.join(DOCS, g["dir"], "sounds")
        os.makedirs(dst, exist_ok=True)
        for f in os.listdir(os.path.join(ROOT, "sounds")):
            if f.endswith(".mp3"):
                shutil.copy2(os.path.join(ROOT, "sounds", f), dst)
    cards.append(f'<a class="game" href="{g["dir"]}/"><span class="ic">{g["icon"]}</span>'
                 f'<span><b>{title}</b><small>{g["desc"]}</small></span><span class="go">▶</span></a>')

hub_body = """<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Baloo+2:wght@800&family=Nunito:wght@600;800&display=swap">
<style>
:root { --sky:#b8e3f5; --sky-hi:#e6f6fc; --grass:#74c26f; --grass-dk:#3f9450; --wood:#7a4b23; --paper:#fffdf4; --ink:#22314a; --muted:#6c7a90; color-scheme: light; }
html, body { min-height: 100%; }
body { margin: 0; font-family: "Nunito", system-ui, sans-serif; color: var(--ink);
  background: linear-gradient(var(--sky-hi), var(--sky) 45%, var(--grass) 45%, var(--grass-dk)); background-attachment: fixed; }
main { max-width: 540px; margin: 0 auto; padding: 32px 16px 40px; display: flex; flex-direction: column; gap: 16px; }
h1 { font-family: "Baloo 2", system-ui, sans-serif; font-size: 44px; line-height: 1.05; margin: 0; text-align: center; color: var(--wood); text-shadow: 0 3px 0 var(--paper); }
.sub { text-align: center; margin: 0 0 10px; font-weight: 800; color: var(--grass-dk); }
.game { display: grid; grid-template-columns: 70px 1fr auto; gap: 12px; align-items: center; text-decoration: none; color: inherit;
  background: var(--paper); border: 4px solid var(--wood); border-radius: 24px; padding: 16px; box-shadow: 0 6px 0 var(--wood); }
.game:active { transform: translateY(3px); box-shadow: 0 3px 0 var(--wood); }
.game:focus-visible { outline: 4px solid #3a86ff; outline-offset: 3px; }
.ic { font-size: 54px; text-align: center; line-height: 1; }
.game b { display: block; font-family: "Baloo 2", system-ui, sans-serif; font-size: 25px; line-height: 1.1; }
.game small { color: var(--muted); font-weight: 600; font-size: 15px; line-height: 1.4; }
.go { font-size: 24px; color: var(--grass-dk); }
.foot { text-align: center; color: var(--paper); font-size: 13px; font-weight: 600; margin-top: 8px; }
</style>
<main>
  <h1>Góc Game của Gary</h1>
  <p class="sub">Chọn một trò để chơi nhé!</p>
  """ + "\n  ".join(cards) + """
  <p class="foot">Tiến trình chơi được lưu trên máy này.</p>
</main>"""
hub = HEAD.format(title="Góc Game của Gary", desc="Các game học tập cho bé: Toán lớp 1 và Sudoku.", icon="🎮", extra="") \
    + hub_body + "\n</body>\n</html>\n"
write(os.path.join(DOCS, "index.html"), hub)
open(os.path.join(DOCS, ".nojekyll"), "w").close()
print("docs/ ready:", ", ".join(g["dir"] for g in GAMES))
