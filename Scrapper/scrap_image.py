import requests
import pandas as pd
from bs4 import BeautifulSoup
page = requests.get('https://animemotivation.com/avatar-the-last-airbender-quotes')
soup = BeautifulSoup(page.content, 'html.parser')
print(page.status_code)
#print(soup.prettify())
characters = soup.find('div',class_='entry-content single-page')
#print(characters)
p1 = characters.p
p2 = characters.findAll('img')
c_l =[]
#print(p1)
#print(p2)
for x in p2:
    temp = x.get('src')
    if temp[:1]=="/":
        f = "https://animemotivation.com/avatar-the-last-airbender-quotes/" + temp
    else:
        f = temp
    filename = x.get('alt')
    imagefile = open(filename+'.jpeg','wb')
    r = requests.get(f)
    with open(filename+".jpeg","wb") as img_f:
        img_f.write(r.content)
    
#    c_l.append(x.text)
#df=pd.DataFrame(c_l,columns=['Character Name'])
#xc=df.head(20)
#print(xc)
#df.to_csv('Character_Names.csv')
