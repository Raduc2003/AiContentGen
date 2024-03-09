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
for file in files:
    image_clip = ImageClip(folder_path+file).set_duration(2).set_fps(24)  # 10 seconds, 24 fps
    clips.append(image_clip)
final_clip = concatenate_videoclips(clips, method="compose")
audio = AudioFileClip(audio_path+afile)

final_clip = final_clip.set_audio(audio)
final_clip.write_videofile("output.mp4", fps=24)  # Specify fps here
print(audio_path+afile)
os.startfile("C:/Users/carac/Documents/StableDiff/webUI/stable-diffusion-webui/AiContentGen/output.mp4")
