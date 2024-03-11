from tts.audioGen import generate_audio
from StableDiffusion.imageGen import generateImages
from LLM.promptGen  import generate as promptGenerate
from LLM.factGen import factGenerate
from modelStart import startModels
from videoMaker import makeVideo

#set ouput folder for image generation
image_output_folder = "C:\\Users\\carac\\Documents\\StableDiff\\webUI\\stable-diffusion-webui\\AiContentGen\\output_img"
video_output_folder = "C:\\Users\\carac\\Documents\\StableDiff\\webUI\\stable-diffusion-webui\\AiContentGen\\output_video"
#start the ai models
startModels()
# Wait for the models to start
import time
while(time.sleep(40)):
    print("Waiting for the models to start...")

# Generate the facts
facts = factGenerate()
# Generate the prompts
prompts = promptGenerate(facts)
# Generate the images
generateImages(prompts,image_output_folder)
# Generate the audio
generate_audio(facts)
# Make the video
makeVideo(image_output_folder,facts,video_output_folder)
