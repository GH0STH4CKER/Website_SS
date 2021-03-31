import requests
from api import key

web = input("Enter Website Address : ")

url = 'https://api.screenshotmachine.com/?key='+key+'&url='+web+'&dimension=1024xfull&delay=3000'

res = requests.get(url)

file = open("sample_image.png", "wb")
file.write(res.content)
file.close()