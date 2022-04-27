import requests
from bs4 import BeautifulSoup
import pandas as pd


import csv
page=1
list_names=[]
list_prices=[]



while page !=49:   
    url=f"https://www.jumia.co.ke/smart-tvs-2282/?page={page}#catalog-listing"

    get=requests.get(url).text
    soup=BeautifulSoup(get,'html.parser')
    for items in soup.find('div',class_="-pvs col12"):
        name=items.find_all('h3',class_='name')
        price=items.find_all('div',class_='prc')


    for n in name:
        list_names.append(n.text)
        
    for p in price:
        list_prices.append(p.text)
    page+=1


range_=[]
for r in range(len(list_names)):
    range_.append(r)

   
dict_={
    'names':list_names,
   'prices':list_prices,
   
}



pd_data=pd.DataFrame(dict_,index=range_)
print(pd_data)
pd_data.to_csv('jumia.csv',index=False)









