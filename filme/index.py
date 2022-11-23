from bs4 import BeautifulSoup
import urllib.parse
from requests import Session
import json
session = Session()

url = 'https://topflix.io'

query = input('Nome do filme para pesquisar: ')
query = urllib.parse.quote(query)
response = session.get(f'{url}/pesquisar/{query}')

soup = BeautifulSoup(response.text, 'html.parser')
movie_div = soup.find('div', attrs={'class': 'generalMoviesList'})
movie_list = movie_div.find_all('a', attrs={'class': 'gPoster'})

dict_movie = dict()
dict_movie['Movies'] = []

for movie in movie_list:
    movie_dict_info = dict()
    link = movie['href']
    movie_dict_info['Link'] = f'{url}/{link}'
    movie_dict_info['Titulo'] = movie.find('div', attrs={'class': 'i'}).find('span').text.strip()
    print(movie_dict_info)
    dict_movie['Movies'].append(movie_dict_info)

with open('FILMES.json', 'w', encoding='utf8') as w:
    json.dump(dict_movie, w, indent=4, ensure_ascii=False)