import requests 
from bs4 import BeautifulSoup
import lxml

url = 'https://examadmin.icaponline.net.pk:8888/ords/r/liveapp/100/files/static'

r = requests.get(url)

soup = BeautifulSoup(r.content)

print(soup.prettify)






