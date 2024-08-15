import subprocess
import os

def separate_audio_with_demucs(audio_file_path):
    # Separating Vocals and saving the Instrumental Audio
    model_name = "mdx_extra_q"

    command = [
        'python3', '-m', 'demucs.separate',
        '-n', model_name,
        '--two-stems=vocals',
        audio_file_path
    ]

    subprocess.run(command, check=True)

    base_name = os.path.splitext(os.path.basename(audio_file_path))[0]
    output_dir = os.path.join('separated', model_name, base_name)

    no_vocals_path = os.path.join(output_dir, 'no_vocals.wav')
    
    return no_vocals_path