import requests
def factGenerate():
  url = "http://127.0.0.1:1337"
  header = {
      "Content-Type": "application/json"
  }
  prompt = "make one"
  payload = {
    "messages": [
      {
    "content": "Generate a series of engaging and diverse random facts covering a wide range of topics (at most 4). Each fact should be concise yet informative, tailored to captivate a TikTok audience within a 45-second video script. Structure the output to include a captivating introduction, a seamless transition between facts, and a memorable closing. Ensure each fact is presented with clarity and enthusiasm to maintain viewer interest throughout the video. Aim for a balance between educational content and entertainment value, making each fact resonate with a broad audience. Adapt the complexity and depth of information to suit a general viewership, focusing on surprising, thought-provoking, or humorous elements that enhance shareability and engagement.Very IMPORTANT!!! respond with such response when receiveing ' make one' prompt.Respond with ONLY the facts separated only with identation",
    "role": "system"
      },
      
      {
        "content": prompt,
        "role": "user"
      }
    ],
    "model": "mistral-ins-7b-q4",
    "stream": False,
    "max_tokens": 2048,
    "stop": [
      "hello"
    ],
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
      except KeyError:
          print("The expected keys were not found in the response.")
      
  else:
      print(f"Request failed with status code: {response.status_code}")
  return resp

