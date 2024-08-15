import os
from moviepy.editor import ImageSequenceClip, AudioFileClip, concatenate_videoclips, ImageClip


def extract_number(filename):
    # Extracting the number inside the file name in preparation for sorting
    base_name = os.path.basename(filename)
    return int(base_name.split('_')[1].split('.')[0])

def create_video_from_images_and_audio(image_folder, audio_file, transcription_result, song, fps=24):
    output_file = f"{song}.mp4"
    
    image_files = sorted(
        [os.path.join(image_folder, img) for img in os.listdir(image_folder) if img.endswith(('png', 'jpg', 'jpeg'))],
        key=extract_number
    )
    
    segments = transcription_result['segments']
    timestamps = [segment['start'] for segment in segments]
    
    timestamps[0] = 0.0
    
    if len(image_files) != len(timestamps):
        raise ValueError("Number of pictures and time stamps must be equal")
    
    audio_clip = AudioFileClip(audio_file)
    
    clips = []
    for i, (img, start_time) in enumerate(zip(image_files, timestamps)):
        if i < len(timestamps) - 1:
            duration = timestamps[i + 1] - start_time
        else:
            duration = audio_clip.duration - start_time
            
        img_clip = ImageClip(img).set_start(start_time).set_duration(duration)
        clips.append(img_clip)
    
    video_clip = concatenate_videoclips(clips, method="compose")
    
    video_clip = video_clip.set_duration(audio_clip.duration).set_fps(fps)
    
    video_clip = video_clip.set_audio(audio_clip)
    
    video_clip.write_videofile(output_file, codec="libx264", audio_codec="aac", fps=fps)
    
    return output_file