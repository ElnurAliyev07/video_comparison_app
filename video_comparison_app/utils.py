import cv2
import numpy as np
import tempfile
import os

def compare_videos(video1, video2):
    try:
        with tempfile.NamedTemporaryFile(delete=False) as temp_file1:
            temp_file1.write(video1.read())
            temp_file1_path = temp_file1.name

        with tempfile.NamedTemporaryFile(delete=False) as temp_file2:
            temp_file2.write(video2.read())
            temp_file2_path = temp_file2.name

        cap1 = cv2.VideoCapture(temp_file1_path)
        cap2 = cv2.VideoCapture(temp_file2_path)

        duration1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT) / cap1.get(cv2.CAP_PROP_FPS))
        duration2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT) / cap2.get(cv2.CAP_PROP_FPS))

        if duration1 != duration2:
            return "Video durations do not match. These videos are not the same"

        width1 = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
        height1 = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
        width2 = int(cap2.get(cv2.CAP_PROP_FRAME_WIDTH))
        height2 = int(cap2.get(cv2.CAP_PROP_FRAME_HEIGHT))

        if width1 != width2 or height1 != height2:
            return "Video resolutions do not match. These videos are not the same"

        for _ in range(duration1):
            ret1, frame1 = cap1.read()
            ret2, frame2 = cap2.read()

            if not ret1 or not ret2:
                return "Error reading frames."

            if not np.array_equal(frame1, frame2):
                return "Pixel values do not match. These videos are not the same"

        return "Videos match: These videos are the same"

    except Exception as e:
        return f"An error occurred: {str(e)}"

    finally:
        if cap1:
            cap1.release()
        if cap2:
            cap2.release()

        if temp_file1_path:
            os.remove(temp_file1_path)
        if temp_file2_path:
            os.remove(temp_file2_path)
