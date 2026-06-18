import os
import cv2
import numpy as np
from tqdm import tqdm
from retinaface import RetinaFace

# =========================
# CONFIG
# =========================

DATASET_PATH = r"D:\dataset"

OUTPUT_PATH = r"D:\processed_faces"

IMG_SIZE = 224

FRAMES_PER_VIDEO = 20

# =========================
# FACE EXTRACTION
# =========================

def extract_face(frame):

    try:

        detections = RetinaFace.detect_faces(frame)

        if not isinstance(detections, dict):
            return None

        largest_area = 0
        best_face = None

        for face_id in detections:

            facial_area = detections[face_id]["facial_area"]

            x1, y1, x2, y2 = facial_area

            area = (x2 - x1) * (y2 - y1)

            if area > largest_area:

                largest_area = area

                best_face = facial_area

        if best_face is None:
            return None

        x1, y1, x2, y2 = best_face

        x1 = max(0, x1)
        y1 = max(0, y1)

        face = frame[y1:y2, x1:x2]

        if face.size == 0:
            return None

        face = cv2.resize(
            face,
            (IMG_SIZE, IMG_SIZE)
        )

        return face

    except Exception:

        return None


# =========================
# PROCESS VIDEO
# =========================

def process_video(video_path, save_dir):

    cap = cv2.VideoCapture(video_path)

    total_frames = int(
        cap.get(cv2.CAP_PROP_FRAME_COUNT)
    )

    if total_frames <= 0:

        cap.release()
        return

    frame_indices = np.linspace(
        0,
        total_frames - 1,
        FRAMES_PER_VIDEO,
        dtype=int
    )

    saved_count = 0

    for idx in frame_indices:

        cap.set(
            cv2.CAP_PROP_POS_FRAMES,
            idx
        )

        success, frame = cap.read()

        if not success:
            continue

        face = extract_face(frame)

        if face is None:
            continue

        file_name = f"{saved_count:03d}.jpg"

        cv2.imwrite(
            os.path.join(
                save_dir,
                file_name
            ),
            face,
            [
                cv2.IMWRITE_JPEG_QUALITY,
                95
            ]
        )

        saved_count += 1

    cap.release()


# =========================
# MAIN
# =========================

def process_folder(label):

    input_folder = os.path.join(
        DATASET_PATH,
        label
    )

    output_folder = os.path.join(
        OUTPUT_PATH,
        label
    )

    os.makedirs(
        output_folder,
        exist_ok=True
    )

    videos = [

        f for f in os.listdir(input_folder)

        if f.lower().endswith(".mp4")
    ]

    for video in tqdm(
        videos,
        desc=f"Processing {label}"
    ):

        video_name = os.path.splitext(video)[0]

        save_dir = os.path.join(
            output_folder,
            video_name
        )

        if os.path.exists(save_dir):
            continue

        os.makedirs(
            save_dir,
            exist_ok=True
        )

        process_video(
            os.path.join(
                input_folder,
                video
            ),
            save_dir
        )


if __name__ == "__main__":

    process_folder("real")

    process_folder("fake")

    print("\nFace extraction completed!")