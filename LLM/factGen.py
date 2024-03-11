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
    "content": "Generate four distinct and captivating facts, each under 20 words, spanning various subjects. Aim for brevity and intrigue, suitable for quick social media engagement. Focus on ensuring each fact stands alone for impact, with clear, attention-grabbing content that sparks curiosity or amusement. Prioritize simplicity and shareability, appealing to a broad audience's interests.Very IMPORTANT!!! respond with such response when receiveing ' make one' prompt.Respond with ONLY the facts separated only with identation",
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

