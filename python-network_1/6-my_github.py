"""Get GitHub id using github API along with Basic Authentication"""
#try:
#        r = get('https://api.github.com/user', auth=(argv[1], argv[2]))
#        j = r.json()
#        print(j.get('id'))
#except ValueError as e:
#        print(e)

from requests import get
from requests.auth import HTTPBasicAuth
from sys import argv

if __name__ == "__main__":
    url = 'https://api.github.com/user'
    username = argv[1]
    password = argv[2]
    response = get(url, auth=HTTPBasicAuth(username, password))
    try:
        obj = response.json()
        print(obj.get('id'))
    except ValueError:
        print(None)
