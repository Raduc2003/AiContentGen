import requests
import base64
import os
# Define the URL and the payload to send.
url = "http://127.0.0.1:7860"

# output folder is the folder where the image will be saved.
output_folder = "output_img/"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#prompts will be imported from gui in future
prompts = ["dog","cat","tiger","monkey"]

def generateUniqueNames(folderPath,fileName):
    counter= 1
    
    while os.path.exists(folderPath+fileName+'.png'):
        fileName =  f"{fileName[:-2]}_{counter}" if fileName != "output" else f"{fileName}_{counter}" 
        counter+=1
    return fileName

#generate all the prompts
fileName = "output"
for prompt in  prompts:
    payload = {
    "prompt": prompt,
    "steps": 10
    }
    # Send said payload to said URL through the API.
    response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
    r = response.json()
    # Decode and save the image.
    
    newName = generateUniqueNames(output_folder,fileName)
    fileName = newName
    print("saving in: " + newName)
    with open(output_folder+newName+'.png', 'wb') as f:
        f.write(base64.b64decode(r['images'][0]))