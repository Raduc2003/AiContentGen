from factGen import factGen
import requests
def promptGen():
    text = factGen()
    url = "http://127.0.0.1:1337"
    header = {
      "Content-Type": "application/json"
    }
    prompt = "go"
    payload = {
      "messages": [
        {
         "content": "Transform each fact from the text block into a structured array of mini image generation prompts. Each element of the array should consist of a simplified prompt designed to visually represent the corresponding fact. The prompts must specify key elements such as objects, characters, actions, and settings, tailored to encapsulate the essence of the fact in a visually compelling manner. Format the output as a JSON array, where each prompt is encapsulated as a string within double quotes, ensuring easy parsing and consistent structure. This structured format should facilitate the direct use of these prompts for image generation, aiming to enhance understanding and engagement through visual storytelling. The array should be diverse, with each prompt uniquely tailored to the specific fact it represents.",
         "role": "system"
        }

        ,
      
        {
          "content": text,
          "role": "user"
        }  
      ],
      "model": "mistral-ins-7b-q4",
      "stream": False,
      "max_tokens": 2048,
      "stop": [
      "hello"
      ]  ,
      "frequency_penalty": 0,
      "presence_penalty": 0,
      "temperature": 0.7,
      "top_p": 0.95
    }
    # Send the POST request
    response = requests.post(url=f'{url}/v1/chat/completions', headers=header, json=payload)

    # Proceed with JSON decoding and handling
    if response.status_code == 200:
        try:
            result = response.json()

            resp = result['choices'][0]['message']['content']
            # print(resp)
        except KeyError:
            print("The expected keys were not found in the response.")
        
    else:
        print(f"Request failed with status code: {response.status_code}")
    return resp
print(promptGen())