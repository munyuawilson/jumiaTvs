import requests
from bs4 import BeautifulSoup
import pandas as pd


import csv




list_names=[]
list_prices=[]
url=f"https://www.jumia.co.ke/smart-tvs-2282/?page=1#catalog-listing"
get=requests.get(url).text
soup=BeautifulSoup(get,'html.parser')
for items in soup.find_all('div',class_="crs row _no-g -fw-nw _6cl-4cm -pvxs"):
    name=items.find_all('div',class_='name')
    price=items.find_all('div',class_='prc')


    for n in name:
        list_names.append(n.text)
    for p in price:
        list_prices.append(p.text)

    
dict_={
    'names':list_names,
   'prices':list_prices,
   
}

pd_data=pd.DataFrame(dict_,index=[1,2,3,4,5,6,7,])
pd_data.to_csv('jumia.csv',index=False)
print(pd_data)





