import requests

try:
    r = requests.get('http://127.0.0.1:8000/api/info')
    result = r.json()
    for k,v in result.items():
        print(f'{k} : {v}')
except ConnectionError:
    print('erreur de connexion')
except Exception as err:
    print(err)
