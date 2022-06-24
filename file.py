from operator import ge
import requests
from bs4 import BeautifulSoup
url = "https://www.cian.ru/cat.php?currency=2&deal_type=sale&engine_version=2&maxmcad=30&maxprice=5000000&maxsite=15&minprice=1500000&minsite=6&object_type%5B0%5D=3&offer_type=suburban&p=1&region=-1"
response = requests.get(url).text
response_parser = BeautifulSoup(response, 'html.parser')
geo_group = response_parser.select('[data-name=LinkArea]')
# geo_group = response_parser.select('[data-name=SpecialGeo]')
list_of_adress = []

for element in geo_group:
    temporary_list = []
    geo_location = element.select('[data-name=SpecialGeo]')[0]
    for div in geo_location.find_all('div'):
        if div.text:
            temporary_list.append(div.text)
    if temporary_list:
        list_of_adress.append(temporary_list)
    
print(list_of_adress)


