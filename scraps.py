import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.com/s?k=SAMSUNG+MOBILE&crid=7YRE7CFW1JSA&sprefix=samsung+mobil%2Caps%2C314&ref=nb_sb_noss_2"
r=requests.get(url)
#print(r.text)


soup= BeautifulSoup(r.text,"lxml")
print(soup)