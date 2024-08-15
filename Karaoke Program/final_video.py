import os
from moviepy.editor import VideoFileClip, CompositeVideoClip
from PIL import Image, ImageDraw, ImageFont
import numpy as np


def wrap_text(draw, text, font, max_width):
    # Wrapping the Text
    
    lines = []
    words = text.split()

    while words:
        line = ''
        while words and draw.textsize(line + words[0], font=font)[0] <= max_width:
            line = line + (words.pop(0) + ' ')
        lines.append(line.strip())

    return lines

def create_video_with_highlighted_text(background_video_path, song_title, result, fps=24):
    # Create final Karaoke Video
    
    frame_size = (1920, 1080)
    font = ImageFont.truetype("Arial.ttf", 40)
    background_video = VideoFileClip(background_video_path).resize(frame_size)

    segments = []
    for segment in result['segments']:
        segment_start = segment['start']
        segment_end = segment['end']
        words = [(word['start'], word['end'], word['word']) for word in segment['words']]
        segments.append({'start': segment_start, 'end': segment_end, 'words': words})

    def make_frame(t):
        # Generating Single Frames
        frame = background_video.get_frame(t)
        image = Image.fromarray(frame)
        draw = ImageDraw.Draw(image)

        for segment in segments:
            if segment['start'] <= t <= segment['end']:
               
                max_text_width = frame_size[0] - 100

                full_text = ' '.join([text for _, _, text in segment['words']])
                wrapped_lines = wrap_text(draw, full_text, font, max_width=max_text_width)

                total_text_height = sum(draw.textsize(line, font=font)[1] for line in wrapped_lines) + (len(wrapped_lines) - 1) * 5

                y_position = (frame_size[1] * 3 // 4) - (total_text_height // 2)

                for line in wrapped_lines:
                    x_position = frame_size[0] // 2 - draw.textsize(line, font=font)[0] // 2
                    for word_info in segment['words']:
                        word_start, word_end, word_text = word_info

                        word_width, word_height = draw.textsize(word_text, font=font)
                        
                        draw.rectangle(
                            [(x_position - 5, y_position - 5),
                             (x_position + word_width + 5, y_position + word_height + 5)],
                            fill="black"
                        )
                        
                        color = 'red' if word_start <= t < word_end else 'white'
                        
                        draw.text((x_position, y_position), word_text, font=font, fill=color)
                        
                        x_position += word_width + draw.textsize(' ', font=font)[0]
                    y_position += word_height + 5

        return np.array(image)

    video = background_video.fl(lambda gf, t: make_frame(t)).set_duration(background_video.duration)

    final_clip = CompositeVideoClip([video])

    final_video_path = os.path.join(os.getcwd(), f"{song_title}_final.mp4")

    final_clip.write_videofile(final_video_path, codec="libx264", fps=fps, audio_codec='aac')

    return os.path.abspath(final_video_path)