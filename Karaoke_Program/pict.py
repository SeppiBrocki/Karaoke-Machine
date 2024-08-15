import os
import requests
import openai
import time

def extract_text_segments_from_result(result):
    # Generates List with saved Text Segments
    
    text_segments = []

    for segment in result['segments']:
        segment_text = segment['text']  
        text_segments.append(segment_text.strip())

    return text_segments


def get_images_urls(prompts):
    # Generates the URLs for each text segement
    image_urls = []
    
    for i, prompt in enumerate(prompts):
        # Anpassen des Prompts für jedes Segment
        custom_prompt = f"Generate a detailed and vibrant image for the following description: {prompt}"
        
        response = openai.Image.create(
            prompt=custom_prompt,
            n=1,
            size="1024x1024"
        )
        
        image_url = response['data'][0]['url']

        image_urls.append(image_url)

        time.sleep(12)

    return image_urls


def download_images(urls, song_name):
    # Loading and saving the generated Pictures
    
    base_dir = "generated_img"
    
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)
    
    song_dir = os.path.join(base_dir, song_name)
    if not os.path.exists(song_dir):
        os.makedirs(song_dir)
    
    for i, url in enumerate(urls):
        
        save_path = os.path.join(song_dir, f"image_{i + 1}.jpg")
        
        response = requests.get(url)
        with open(save_path, 'wb') as f:
            f.write(response.content)
    
    return song_dir