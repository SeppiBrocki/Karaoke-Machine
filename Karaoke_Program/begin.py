import os

def get_file_path(prompt):
    """Prompts the user to enter a file path and checks if it exists."""
    while True:
        audio_file_path = input(prompt)
        if os.path.isfile(audio_file_path):
            return audio_file_path
        else:
            print("The file does not exist. Please enter a valid file path.")

def get_song_title(prompt):
    """Prompts the user to enter the song title."""
    while True:
        title = input(prompt)
        if title.strip():
            return title.strip()
        else:
            print("The song title cannot be empty. Please enter a valid song title.")