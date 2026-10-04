"""Tải và xử lý âm thanh tấn công cho game.

Nguồn (đều dùng miễn phí, không bắt buộc ghi công):
  - Mixkit Sound Effects Free License: https://mixkit.co/license/#sfxFree
  - BigSoundBank (CC0 / public domain): https://bigsoundbank.com/licence.html
  - Wikimedia Commons, file CC0
Chạy lại: python sounds/fetch_sounds.py  (cần ffmpeg)
"""
import os, subprocess, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
RAW = os.path.join(HERE, "raw")
MIX = "https://assets.mixkit.co/active_storage/sfx/{0}/{0}-preview.mp3"
BSB = "https://bigsoundbank.com/UPLOAD/mp3/{0}.mp3"

# tên file: (url, số giây giữ lại)
SOUNDS = {
    "bark":    (MIX.format(741), 1.4),   # Happy puppy barks
    "hiss":    (MIX.format(1964), 1.3),  # Monster hiss
    "squirt":  (MIX.format(327), 1.0),   # Snake poison squirt
    "croak":   (BSB.format("0819"), 1.4),  # One frog
    "buzz":    (MIX.format(1926), 1.4),  # Bee buzz
    "whine":   (MIX.format(331), 1.3),   # Cartoon mosquito flying buzz
    "roar":    (MIX.format(6), 1.8),     # Wild lion animal roar
    "catroar": (MIX.format(89), 1.6),    # Angry wild cat roar
    "hoot":    (BSB.format("1764"), 1.8),  # Tawny owl
    "squeak":  (MIX.format(1010), 1.2),  # Cartoon panic squeak
    "chirp":   (MIX.format(23), 1.2),    # Little bird calling chirp
    "parrot":  (MIX.format(27), 1.2),    # Tropical bird squeak
    "meow":    (MIX.format(91), 1.4),    # Cartoon little cat meow
    "splash":  (MIX.format(1311), 1.3),  # Water splash
    "stomp":   (MIX.format(1974), 1.4),  # Giant monster footstep
    "scratch": (MIX.format(2146), 0.9),  # Quick ninja strike
    "whoosh":  (MIX.format(1489), 0.9),  # Air woosh
    "slide":   (MIX.format(2888), 1.2),  # Funny video game slide
    "chomp":   (MIX.format(117), 1.0),   # Bites a juicy sausage
    "kick":    (MIX.format(2163), 0.9),  # Martial arts kick
    "magic":   (MIX.format(871), 1.6),   # Fairy magic sparkle
    "fire":    (MIX.format(1345), 1.4),  # Short fire whoosh
    "ghost":   (MIX.format(2623), 1.8),  # Ghostly whoosh passing
    "devil":   (MIX.format(413), 1.8),   # Little devil laughing
    "trumpet": ("https://upload.wikimedia.org/wikipedia/commons/4/40/Elephant_voice_-_trumpeting.ogg", 1.8),  # CC0
    "growl":   (MIX.format(53), 1.5),    # Angry dog growling
    "grunt":   (MIX.format(3), 1.4),     # Pig grunting
    "screech": (MIX.format(70), 1.6),    # Big wild eagle calling
    "howl":    (MIX.format(1775), 2.2),  # Wolf howling
    "honk":    (MIX.format(20), 1.4),    # Flock of wild geese
    "chatter": (MIX.format(108), 1.6),   # Cartoon monkey mocking and giggling
    "dragon":  (MIX.format(309), 1.8),   # Angry dragon growl
    "dino":    (MIX.format(1976), 1.8),  # Dinosaur monster roar
    "fart":    (MIX.format(2891), 1.2),  # Cartoon fart sound
    "hit":     (MIX.format(2072), 0.6),  # Small hit in a game
}

def main():
    os.makedirs(RAW, exist_ok=True)
    for name, (url, dur) in SOUNDS.items():
        ext = ".ogg" if url.endswith(".ogg") else ".mp3"
        raw = os.path.join(RAW, name + ext)
        if not os.path.exists(raw):
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (MathGame kid project)"})
            with urllib.request.urlopen(req, timeout=60) as r, open(raw, "wb") as f:
                f.write(r.read())
        out = os.path.join(HERE, name + ".mp3")
        fade = min(0.3, dur / 3)
        af = (f"silenceremove=start_periods=1:start_threshold=-40dB,atrim=0:{dur},"
              f"afade=t=out:st={dur - fade:.2f}:d={fade:.2f},loudnorm=I=-16:TP=-1.5:LRA=11")
        subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", raw, "-af", af,
                        "-ac", "1", "-ar", "44100", "-b:a", "64k", out], check=True)
        print(f"{name:8s} {os.path.getsize(out) // 1024:3d} KB")

if __name__ == "__main__":
    main()
