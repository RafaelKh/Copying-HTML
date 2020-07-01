import requests

r = requests.get("https://httpstatuses.com/")
f = open('index.html', 'w')
f.write(r.text)
f.close()
