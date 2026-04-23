import begin
import os

@begin.start
def concat_with_fade(input_dir="media", output_name, fade_in_duration=0.5):
    """
    Concatenate audio files in a directory with a fade in and fade out effect.

    :param input_dir: Directory containing audio files to concatenate.
    :param output_name: Name of the output file.
    :param fade_in_duration: Duration of the fade in effect in seconds.
    """
    audio_files = [f for f in os.listdir(input_dir) if f.endswith('.mp3')]
    print(audio_files)

    # Create a list to hold the ffmpeg commands
    ffmpeg_commands = []

    # Process each audio file
    for file in audio_files:
        input_file = os.path.join(input_dir, file)
        output_file = os.path.join(output_name, file)