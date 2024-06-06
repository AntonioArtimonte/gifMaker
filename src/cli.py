import typer
from rich.console import Console
from videoTransformer import VideoGifConverter
import os

app = typer.Typer()
console = Console()

@app.command()
def convert(convert_type: str, input_path: str, output_path: str = None):
    """
    Convert between video and gif.

    Args:
        convert_type (str): Type of conversion ('video_to_gif' or 'gif_to_video').
        input_path (str): Path to the input file.
        output_path (str): Path to the output file (optional).
    """
    base_dir = os.path.dirname(input_path)
    base_name = os.path.splitext(os.path.basename(input_path))[0]

    if not output_path:
        output_path = os.path.join(base_dir, f"{base_name}.gif" if convert_type == 'vid_gif' else f"{base_name}.avi")
        console.print(f"[red][!] Output file not specified. Saving to {output_path}.[/red]")

    confirmation = typer.confirm(f"[?] Are you sure you want to convert {input_path} to {output_path}? (y/n)")
    if not confirmation:
        console.print("[bold yellow]:warning: Operation cancelled.[/bold yellow]")
        raise typer.Exit()
    
    converter = VideoGifConverter(input_path)
    
    with console.status(f"[bold green]:hourglass_flowing_sand: Processing {input_path}...") as status:
        try:
            if convert_type == 'vid_gif':
                frames = converter.video_to_frames()
                converter.frames_to_gif(frames, output_path)
            elif convert_type == 'gif_vid':
                pil_frames = converter.gif_to_frames()
                frames = [cv2.cvtColor(np.array(frame), cv2.COLOR_RGB2BGR) for frame in pil_frames]
                converter.frames_to_video(frames, output_path)
            else:
                console.print("[bold red]:x: Invalid convert_type. Use 'video_to_gif' or 'gif_to_video'.[/bold red]")
                raise typer.Exit()

            console.print(f"[bold green]:white_check_mark: Conversion complete! {output_path} has been saved.[/bold green]")
        except Exception as e:
            console.print(f"[bold red]:x: An error occurred: {e}[/bold red]")

if __name__ == "__main__":
    app()
