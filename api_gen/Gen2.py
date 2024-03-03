import requests
import time

def generator2(prompt):
    url = "https://omniinfer.p.rapidapi.com/v2/txt2img"

    payload = {
        "negative_prompt": "nsfw, watermark, facial distortion, lip deformity, redundant background, extra fingers, Abnormal eyesight, ((multiple faces)), ((Tongue protruding)), ((extra arm)), extra hands, extra fingers, deformity, missing legs, missing toes, missin hand, missin fingers, (painting by bad-artist-anime:0.9), (painting by bad-artist:0.9), watermark, text, error, blurry, jpeg artifacts, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, artist name, (worst quality, low quality:1.4), bad anatomy",
        "sampler_name": "Euler a",
        "batch_size": 1,
        "n_iter": 1,
        "steps": 20,
        "cfg_scale": 7,
        "seed": -1,
        "height": 1024,
        "width": 768,
        "model_name": "meinamix_meinaV9.safetensors",
        "prompt": "car"
    }
    headers = {
        "content-type": "application/json",
        "X-RapidAPI-Key": "75dc1c1e79mshb60c8d3cbe1e0d5p113e0djsnc29dc44790f1",
        "X-RapidAPI-Host": "omniinfer.p.rapidapi.com"
    }

    response = requests.post(url, json=payload, headers=headers)
        
    if response.status_code == 200:
        taskid = response.json()["data"]["task_id"]
        url_progress = "https://omniinfer.p.rapidapi.com/v2/progress"
        querystring = {"task_id": taskid}
        
        while True:
            # Refacem cererea pentru a verifica progresul
            resp = requests.get(url_progress, headers=headers, params=querystring)
            resp_data = resp.json()  # Convertim fiecare nou răspuns în JSON
            
            if resp.status_code == 200 and "imgs" in resp_data["data"] and resp_data["data"]["imgs"]:
                url_image = resp_data["data"]["imgs"][0]  # Obținem URL-ul primei imagini
                res = requests.get(url_image)  # Facem cererea GET pentru imagine
                return res
            else:
                print("Imaginea nu este încă gata. Verificăm din nou în curând.")
                time.sleep(5)  # Așteptăm 5 secunde înainte de a verifica din nou
    else:
        print(f"Eroare la trimiterea cererii inițiale: {response.status_code}")

# Nu uita să înlocuiești "YOUR_API_KEY_HERE" cu cheia ta API reală
