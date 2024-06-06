import sys
import os
import cv2
import numpy as np
from PIL import Image, ImageSequence

class VideoGifConverter:
    def __init__(self, input_path, output_path=None):
        self.input_path = input_path
        self.output_path = output_path
        self.base_dir = os.path.dirname(input_path)
        self.base_name = os.path.splitext(os.path.basename(input_path))[0]

    def video_to_frames(self):
        vidcap = cv2.VideoCapture(self.input_path)
        success, image = vidcap.read()
        frames = []
        while success:
            frames.append(image)
            success, image = vidcap.read()
        vidcap.release()
        return frames

    def frames_to_gif(self, frames, output_path, duration=100):
        pil_images = [Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)) for frame in frames]
        pil_images[0].save(output_path, save_all=True, append_images=pil_images[1:], duration=duration, loop=0)

    def gif_to_frames(self):
        gif = Image.open(self.input_path)
        frames = [frame.copy() for frame in ImageSequence.Iterator(gif)]
        return frames

    def frames_to_video(self, frames, output_path, fps=10):
        if not frames:
            return False

        height, width, layers = frames[0].shape
        fourcc = cv2.VideoWriter_fourcc(*'MJPG')  # Use 'MJPG' for .avi videos
        video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

        if not video.isOpened():
            return False

        for i, frame in enumerate(frames):
            video.write(frame)
            if i % 10 == 0:  # Print progress every 10 frames
                print(f"Writing frame {i+1}/{len(frames)}")

        video.release()
        
        if not os.path.exists(output_path):

            return False

        return True

    def convert(self, convert_type):
        if convert_type == 'vid_gif':
            output_path = f"{self.output_path}.gif"  # Use .avi extension for MJPG
            frames = self.video_to_frames()
            self.frames_to_gif(frames, output_path)

        elif convert_type == 'gif_vid':
            output_path = f"{self.output_path}.avi"  # Use .avi extension for MJPG
            pil_frames = self.gif_to_frames()
            frames = [cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR) for frame in pil_frames]

        
        else:
            sys.exit(1)

def main():
    if len(sys.argv) != 3:
        print("Usage: python video_gif_converter.py <convert_type> <input_path> <output_path>")
        print("convert_type: 'video_to_gif' or 'gif_to_video'")
        sys.exit(1)
    
    convert_type = sys.argv[1]
    input_path = sys.argv[2]
    output_path = sys.argv[3]

    converter = VideoGifConverter(input_path)
    converter.convert(convert_type)

if __name__ == "__main__":
    main()
