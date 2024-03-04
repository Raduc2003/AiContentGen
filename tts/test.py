from tortoise.api import TextToSpeech

# Initialize the TTS engine
tts = TextToSpeech()

# Your input text
input_text = "Hello, world! This is a test of Tortoise TTS."

# Generate speech from text
# This will return a PCM audio in a numpy array
pcm_audio = tts.tts_with_preset(input_text, voice_samples=None, preset='fast')

# Save the audio to a file (assuming you have `soundfile` library installed)
import soundfile as sf
sf.write('output_audio.wav', pcm_audio, 22050)
