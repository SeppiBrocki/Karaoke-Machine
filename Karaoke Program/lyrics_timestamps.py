import whisper

def transcribe_audio_with_detailed_timestamps(audio_file_path):
    # Loading Whisper-Modell
    model = whisper.load_model("base")
    
    # Transcribe Audio with detailed timestamps
    result = model.transcribe(audio_file_path, word_timestamps=True)
    return result
    
    