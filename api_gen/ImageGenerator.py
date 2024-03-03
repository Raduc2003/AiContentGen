import requests
import api_gen.Gen1 as Gen1
import api_gen.Gen2 as Gen2
prompt = "car"
def generate_image():
    response =Gen2.generator2(prompt)
    if response.status_code == 200:
        # Open a new file in binary write mode. The 'wb' parameter stands for 'write binary'.
        with open('image_from_api.jpg', 'wb') as file:
            file.write(response.content)
        print("Image saved successfully.")
    else:
        print("Failed to retrieve the image. Status code:", response.status_code)
generate_image()