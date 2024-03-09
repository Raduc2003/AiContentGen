import requests
import time

VOICE_SERVER_ADDR = "localhost"
VOICE_SERVER_PORT = 7332

# Define source and destination directories
SOURCE_DIR = "C:/Users/carac/OnlySpeakTTS/audio"
DESTINATION_DIR = "C:/Users/carac/Documents/StableDiff/webUI/stable-diffusion-webui/AiContentGen/output_sound"
def copy_file():
    import shutil
    import os
    time.sleep(3)
    # List all files in SOURCE_DIR that match the criteria
    files = [f for f in os.listdir(SOURCE_DIR) if f.endswith(".wav") ]
    print(files)
    
    # Sort files to get the last one alphabetically
    files.sort()
   
    if files:
        # The last file in sorted order
        file_name = files[-1]
        
        source_path = os.path.join(SOURCE_DIR, file_name)
        destination_path = os.path.join(DESTINATION_DIR, file_name)

        
        # Copy the file
        
        #waits for the file to be created
        shutil.copyfile(source_path, destination_path)

        
        print("Copied file.")
        
        print(f"Copied {file_name} from {SOURCE_DIR} to {DESTINATION_DIR}")
    else:
        print("No matching files found to copy.")
def generate_audio():
    message ="This is a test prompt with a long text to see how the text is displayed in the video"

    # Here you would collect additional details as per your requirement
    # For demonstration, using a fixed voice and clean text flag
    voice_name = "deniro"  # Example, replace with actual voice name
    data = {
        "VOICE": voice_name,
        "CLEAN_TEXT": True,
        "MESSAGE": message
    }

    headers = {"Content-Type": "application/json"}
    response = requests.post(f"http://{VOICE_SERVER_ADDR}:{VOICE_SERVER_PORT}", data=data)

    if response.ok:
        # Assuming the server responds with the name or relative path of the generated file
        # generated_file_name = response.json().get("file_name")

        print(response.text)
    else:
        print("Error: Request failed.")
