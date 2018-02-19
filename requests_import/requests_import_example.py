import requests as requests

req = requests.get('https://ya.ru')

print(req.content)