import hashlib

VIDEO_PATH = r"D:\dataset\real\000.mp4"

sha256 = hashlib.sha256()

with open(VIDEO_PATH, "rb") as f:

    while True:

        chunk = f.read(4096)

        if not chunk:
            break

        sha256.update(chunk)

video_hash = sha256.hexdigest()

print(video_hash)