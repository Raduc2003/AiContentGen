from tts.audioGen import generate_audio
from StableDiffusion.imageGen import generateImages
from LLM.promptGen  import generate as promptGenerate
from LLM.factGen import factGenerate
from modelStart import startModels
from videoMaker import makeVideo
import os
#set ouput folder for image generation
image_output_folder = "C:\\Users\\carac\\Documents\\StableDiff\\webUI\\stable-diffusion-webui\\AiContentGen\\output_img"
video_output_folder = "C:\\Users\\carac\\Documents\\StableDiff\\webUI\\stable-diffusion-webui\\AiContentGen\\output_video"
#start the ai models
ret = startModels()
# Wait for the models to start
import time
# make a loading until the models start


# Generate the facts
facts = factGenerate()
# make a loading until the facts are generated
while not facts:
    print("Loading facts...")
    time.sleep(1)
# Generate the prompts
prompts = promptGenerate(facts)
# make a loading until the prompts are generated
while not prompts:
    print("Loading prompts...")
    time.sleep(1)
# Generate the images
generateImages(prompts,image_output_folder)
# make a loading until the images are generated
while not os.listdir(image_output_folder):
    print("Loading images...")
    time.sleep(1)
# Generate the audio
generate_audio(facts)
# make a loading until the audio is generated

# Make the video
makeVideo(image_output_folder,facts,video_output_folder)
