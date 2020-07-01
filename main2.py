import requests
import re

r = requests.get("https://httpstatuses.com/")
l = re.findall('<li><a href="/(.*?)"><span>(.*?)</span> (.*?)</a></li>', r.text)
print(l)

f = open('test.txt', 'w')
for i in l:
    f.write("{0} - {1}\n".format(i[1], i[2]))
f.close()
