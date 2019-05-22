from urllib.request import  urlopen
from bs4 import BeautifulSoup
import lxml
html = urlopen("http://www.mamicode.com/info-detail-2057171.html")
bsObj = BeautifulSoup(html,"html.parser")
namelist = bsObj.findAll("span",{"class":"green"})
for name in namelist:
    print(name.get_textx())