import requests
from bs4 import BeautifulSoup

url = 'http://example.webscraping.com/places/default/view/Yemen-250'
response = requests.get(url)
if response.ok:
    soup = BeautifulSoup(response.text, 'lxml')
    country = soup.find(attrs={'id' : 'places_country__row'}).find(attrs={'class': 'w2p_fw'})
    population = soup.find(attrs={'id': 'places_population__row'}).find(attrs={'class': 'w2p_fw'})
    print(f'Il y a {population.text} habitants au {country.text}.')
