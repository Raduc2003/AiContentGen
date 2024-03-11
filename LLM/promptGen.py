from LLM.factGen import factGenerate
import requests
def textToArray(text):
    text = text[1:-1]
    l =[x[1:-1] for x in text.split(",\n")]
    return l
def generate(text):
    
    url = "http://127.0.0.1:1337"
    header = {
      "Content-Type": "application/json"
    }
    prompt = "go"
    payload = {
      "messages": [
        {
         "content": "Convert each fact into an array of straightforward image prompts. Each prompt should include essential elements like subjects, actions, and environments, capturing the fact's core visually. Present the prompts in a JSON array, with each as a concise string. This format should be directly usable for image creation, aiding comprehension through visual representation. Ensure variety and uniqueness across the prompts to reflect the diverse nature of the facts.",
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
            print(resp)
            resp = textToArray(resp)
            print(resp)
        except KeyError:
            print("The expected keys were not found in the response.")
        
    else:
        print(f"Request failed with status code: {response.status_code}")
    return resp
# print(promptGen())
