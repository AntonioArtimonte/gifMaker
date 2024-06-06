# Video-GIF Converter

This repository contains scripts for converting videos to GIFs and GIFs to videos. The conversion functionality is encapsulated in a Python class, and a command-line interface (CLI) is provided for ease of use.

## Requirements

Make sure you have the following packages installed:

- `opencv-python`
- `Pillow`
- `numpy`
- `typer`
- `rich`

You can install them using pip:

```bash
pip install -r requirements.txt
```

## Files

### video_gif_converter.py

This file contains the `VideoGifConverter` class, which handles the conversion between videos and GIFs.

#### Methods
- **video_to_frames(video_path):** Extracts frames from a video file.
- **frames_to_gif(frames, output_path, duration=100):** Converts frames to a GIF file.
- **gif_to_frames(gif_path):** Extracts frames from a GIF file.
- **frames_to_video(frames, output_path, fps=10):** Converts frames to a video file.
- **convert(convert_type):** Main method to handle conversion based on the provided type.

### cli.py

This file provides a command-line interface (CLI) for the conversion functionality using `Typer`  and `Rich`.

## Commands

`convert <convert_type> <input_path> [output_path]:` Convert between video and GIF.

## Usage

### Converting Video to GIF

To convert a video to a GIF, use the following command:

```bash
python cli.py convert vid_gif input_video.mp4
```

### Converting GIF to Video

To convert a GIF to a video, use the following command:

```bash
python cli.py convert gif_vid input_gif.gif
```

### Specifying Output Path

If you want to specify the output path, you can do so by adding the output_path argument:

```bash
python cli.py convert vid_gif input_video.mp4 output.gif
```

```bash
python cli.py convert gif_vid input.gif output_video.avi
```

## Example Output

```bash
> python cli.py convert video_to_gif video.webm
[!] Output file not specified. Saving to video.gif.
[?] Are you sure you want to convert video.webm to video.gif? (y/n): y
Processing video.webm...
✔ Conversion complete! video.gif has been saved.
```

## Error Handling

If an error occurs during the conversion process, an appropriate error message will be displayed:

```bash
[x] An error occurred: [error message]
```