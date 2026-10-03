import requests

resposta = requests.get("https://api.github.com/users/santosluzia/repos") 
print(resposta.status_code)
print(resposta.json())
