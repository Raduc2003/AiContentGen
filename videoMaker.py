import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip
from moviepy.editor import ImageClip
from moviepy.editor import TextClip
from moviepy.editor import VideoFileClip, CompositeVideoClip
from moviepy.config import change_settings
change_settings({"IMAGEMAGICK_BINARY": r"C:/Program Files/ImageMagick-7.1.1-Q16-HDRI/magick.exe"})
folder_path = "output_img/"
audio_path = "C:/Users/carac/OnlySpeakTTS/audio/"
afiles = [f for f in os.listdir(audio_path) if f.endswith(".wav") ]
afiles.sort()
afile=afiles[-1]
files = os.listdir(folder_path)
clips = []
prompt = "This is a test prompt with a long text to see how the text is displayed in the video"

wordsList = prompt.split()
words = len(wordsList)
audio = AudioFileClip(audio_path+afile)
duration = audio.duration
clipLength = duration/words*5 #average time for 5 words
photoLength =duration/4  #assuming 4 facts per prompt
subtitles = []
for file in files:
    image_clip = ImageClip(folder_path+file).set_duration(photoLength).set_fps(24)
    clips.append(image_clip)

fiveWordsList = []
for i in range(0, len(wordsList), 5):
    fiveWordsList.append(" ".join(wordsList[i:i + 5]))
for i in range(len(fiveWordsList)):
    text = TextClip(fiveWordsList[i], fontsize=24, color='white', bg_color='black').set_duration(clipLength).set_fps(24)
    subtitles.append(text)
    #text = TextClip(fiveWordsList[i], fontsize=70, color='white', bg_color='black').set_duration(clipLength).set_fps(24

subtitles = concatenate_videoclips(subtitles)
final_clip = concatenate_videoclips(clips, method="compose")
final_clip = final_clip.set_audio(audio)
final_clip = CompositeVideoClip([final_clip, subtitles.set_start(0)])


final_clip.write_videofile("output.mp4", fps=24)  # Specify fps here
print(audio_path+afile)
os.startfile("C:/Users/carac/Documents/StableDiff/webUI/stable-diffusion-webui/AiContentGen/output.mp4")

