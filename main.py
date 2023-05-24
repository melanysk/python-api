import requests
from PIL import Image
import datetime

# Šeit veicam API pieprasijumu no 'thecatapi' lai iegūtu kaķa attēlu linku, kas katru reizi mainās. Izmantosim iegūto linku lai varētu to izvadīt kā attēlu.
image_response = requests.get("https://api.thecatapi.com/v1/images/search");

# Pārbaudam vai pieprasijums ir veiksmīgs
if image_response.status_code == 200:
  # Pārveidojam atbildi kā JSON
  data = image_response.json()

  # Izvēlamies 'image'
  image_url = data[0]["url"]
  print("Attēla saite: ", image_url)

  # Iegūstam attēlu no saites
  image = Image.open(requests.get(image_url, stream=True).raw)
  image.show()
else:
  print("Kļūde ar attēla API. Statuss: ", image_response.status_code)

# Šeit veicam API pieprasijumu no 'cat-fact' lai iegūtu kaķa faktu tekstu un pievienošanas datumu, kas katru reizi mainās. Izmantosim iegūto faktu un datumu lai to izvadītu.
fact_response = requests.get("https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount=1")

# Pārbaudam vai pieprasijums ir veiksmīgs
if fact_response.status_code == 200:
  # Pārveidojam atbildi kā JSON
  fact_data = fact_response.json()

  # Izvēlamies 'text' aili no API
  fact_text = fact_data['text']
  fact_date = fact_data['createdAt']
  datetime_o = datetime.datetime.fromisoformat(fact_date.replace("Z", "+00:00"))
  date = datetime_o.strftime("%Y.%m.%d")
  print("Kaķa fakts: ", fact_text)
  print("Fakts pievienots: ", date)
else:
  print("Kļūde ar faktu API. Statuss: ", fact_response.status_code)