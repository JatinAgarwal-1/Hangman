import requests

URL = 'https://random-word-api.herokuapp.com/word?number=1'

r = requests.get(url = URL)

word = r.json()[0]

print(word)