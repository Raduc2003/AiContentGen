import os
from moviepy.editor import VideoFileClip, concatenate_videoclips, AudioFileClip, CompositeAudioClip
from moviepy.editor import ImageClip
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
clipLength = words/4
print(clipLength)
for file in files:
    image_clip = ImageClip(folder_path+file).set_duration(clipLength).set_fps(24)  # 10 seconds, 24 fps
    clips.append(image_clip)

final_clip = concatenate_videoclips(clips, method="compose")


from moviepy.editor import TextClip

# text_clip = TextClip('This is a test prompt with a long text to see how the text is displayed in the video', fontsize=70, color='white').set_position('center').set_duration(10)




audio = AudioFileClip(audio_path+afile)

final_clip = final_clip.set_audio(audio)
final_clip.write_videofile("output.mp4", fps=24)  # Specify fps here
print(audio_path+afile)
os.startfile("C:/Users/carac/Documents/StableDiff/webUI/stable-diffusion-webui/AiContentGen/output.mp4")

