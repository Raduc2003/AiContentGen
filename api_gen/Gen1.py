import requests
def generator1(prompt):
    url1 = "https://arimagesynthesizer.p.rapidapi.com/generate"
    payload = {
        "prompt":prompt,
        "id": "12345",
        "width": "768",
        "height": "768",
        "inferenceSteps": "50",
        "guidanceScale": "7.5",
        "img2img_strength": "0.75"
    }
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "X-RapidAPI-Key": "75dc1c1e79mshb60c8d3cbe1e0d5p113e0djsnc29dc44790f1",
        "X-RapidAPI-Host": "arimagesynthesizer.p.rapidapi.com"
    }

    response1 = requests.post(url1, data=payload, headers=headers)
    hashstr = response1.json()['hash']
    if response1.status_code == 200:
        url = "https://arimagesynthesizer.p.rapidapi.com/get"

        querystring = {"hash":hashstr,"returnType":"image"}

        headers = {
            "X-RapidAPI-Key": "75dc1c1e79mshb60c8d3cbe1e0d5p113e0djsnc29dc44790f1",
            "X-RapidAPI-Host": "arimagesynthesizer.p.rapidapi.com"
        }

        response = requests.get(url, headers=headers, params=querystring)
    return response

