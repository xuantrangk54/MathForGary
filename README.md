# Bé Cứu Muông Thú

Game học Toán lớp 1 (tiếng Việt) chơi trên điện thoại và máy tính. Bé điều khiển một cậu bé hoặc cô bé đi qua 20 màn để giải cứu muông thú. Mỗi lần trả lời đúng một bài toán, bạn thú của bé tấn công quái vật.

**Chơi ngay:** https://xuantrangk54.github.io/MathForGary/

## Nội dung
- Toán lớp 1: đếm, cộng trừ trong phạm vi 10, so sánh số, nhận biết hình, số còn thiếu, chục và đơn vị, cộng trừ không nhớ trong phạm vi 100. Độ khó tăng dần theo vùng.
- 21 bạn thú, mỗi con có hệ (Nước, Lửa, Sắt, Cây, Đất) theo luật tương khắc.
- Bạn thú phải được cho ăn bằng cách giải bài thì mới có lượt tấn công.
- Có đọc câu hỏi bằng giọng tiếng Việt (cần máy có giọng tiếng Việt) và góc phụ huynh xem thống kê.
- Tiến trình lưu trên trình duyệt của từng máy.

## Cấu trúc
- `index.html`: mã nguồn game, một file duy nhất.
- `sounds/`: âm thanh tấn công. `sounds/fetch_sounds.py` tải và cắt lại các file này (cần ffmpeg).
- `build.py`: tạo bản web hoàn chỉnh trong `docs/` cho GitHub Pages. Chạy lại mỗi khi sửa `index.html`.

## Âm thanh
- [Mixkit](https://mixkit.co/license/#sfxFree), giấy phép Sound Effects Free
- [BigSoundBank](https://bigsoundbank.com) của Joseph Sardin, giấy phép CC0
- [Wikimedia Commons](https://commons.wikimedia.org/wiki/File:Elephant_voice_-_trumpeting.ogg), giấy phép CC0
