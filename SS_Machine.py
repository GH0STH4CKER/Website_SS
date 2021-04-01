import requests
from api import key
from colorama import Fore,init
init()
lg = Fore.LIGHTGREEN_EX
lr = Fore.LIGHTRED_EX
ly = Fore.LIGHTYELLOW_EX

banner = """
   █▀ █▀   █▀▄▀█ ▄▀█ █▀▀ █ █ █ █▄ █ █▀▀
   ▄█ ▄█   █ ▀ █ █▀█ █▄▄ █▀█ █ █ ▀█ ██▄ V 1.0\n-------------------------------------------------\n"""
tag = "[+] GH0STH4CK3R [+] API screenshotmachine.com "

print(lg+ banner,ly +tag)

print(lg+"")
web = input("Enter Website Address : ")
fname = input('Enter filename (*.png): ')

if fname == '' :
	fname = 'ssmachine_image.png'

url = 'https://api.screenshotmachine.com/?key='+key+'&url='+web+'&dimension=1024xfull&delay=3000'

res = requests.get(url)

if res.status_code == 200 :
	file = open(fname, "wb")
	file.write(res.content)
	file.close()
	print('\nfile download successful !\n\nSaved to current folder !')
else:
	print(lr+'\nSomething Went Wrong !')
	print('\nCause for this can be : \n\n   No Internet\n   Incorrect Url format\n   Invalid api key')
