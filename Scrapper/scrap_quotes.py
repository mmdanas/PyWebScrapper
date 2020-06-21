import requests
import pandas as pd
from bs4 import BeautifulSoup
page = requests.get('https://animemotivation.com/avatar-the-last-airbender-quotes')
soup = BeautifulSoup(page.content, 'html.parser')
print(page.status_code)
#print(soup.prettify())
characters = soup.find('div',class_='entry-content single-page')
#print(characters)
p1 = characters.h3.text
p2 = characters.findAll('blockquote')
print(p1)
print(p2)
quote_list = []
for x in p2:
    print(x.text)
    quote_list.append(x.text)
df=pd.DataFrame(quote_list,columns=['Quotes'])
print(df)
df.to_csv('Quotes.csv')
