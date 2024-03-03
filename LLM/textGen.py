import requests
import json

url = "http://127.0.0.1:1337"
header = {
    "Content-Type": "application/json"
}
prompt = "Tell me a joke about monkeys"
payload = {
  "messages": [
    {
      "content": prompt,
      "role": "user"
    }
  ],
  "model": "tinyllama-1.1b",
  "stream": True,
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

# Print the raw response text
print(response.text)

# Proceed with JSON decoding and handling
if response.status_code == 200:
    try:
        result = response.json()
        # Adjust the key access based on the actual JSON structure
        resp = result['choices'][0]['message']['content']
        print(resp)
    except KeyError:
        print("The expected keys were not found in the response.")
    except json.JSONDecodeError:
        print("Error decoding JSON from response.")
else:
    print(f"Request failed with status code: {response.status_code}")
