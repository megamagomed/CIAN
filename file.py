
import requests
from bs4 import BeautifulSoup
url = "https://www.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxmcad=30&maxprice=5000000&maxsite=15&minprice=1500000&minsite=6&object_type%5B0%5D=3&offer_type=suburban&p=1&region=-1"
response = requests.get(url).text
response_parser = BeautifulSoup(response, 'html.parser')
geo_group = response_parser.select('[data-name=LinkArea]')
list_of_adress = []


for element in geo_group:
    link = element.find('a')
    temporary_list = []
    geo_location = element.select('[data-name=SpecialGeo]')

    for location in geo_location:
        for div in location.find_all('div'):
            if div.text:
                temporary_list.append(div.text)
    if temporary_list:
        list_of_adress.append((temporary_list,link['href']))

def sort_list_of_adress(list_of_address):
    intermediate_list = []
    list_of_address_mod = []
    collection_of_address = {}
    for i in range(len(list_of_address)):
        for j in list_of_address[i][0]:
            intermediate_list.append(j)
        intermediate_list.append(list_of_address[i][1])
        list_of_address_mod.append(intermediate_list)
        intermediate_list = []    

    list_of_address_mod_sorted = sorted(list_of_address_mod, key=lambda el: int(el[len(el)-2][:2]))
    
    for distance in list_of_address_mod_sorted:
        station = distance[len(distance)-3]
        time = distance[len(distance)-2]
        collection_of_address[distance[len(distance)-1]] = time, station  
    return collection_of_address

# print(sort_list_of_adress(list_of_adress))
       



