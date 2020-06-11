from requests import get
from bs4 import BeautifulSoup

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

response = get(url)
# print(response.text[:500])

html_soup = BeautifulSoup(response.text, 'html.parser')

# use find_all() method to extract all the div containers that have class attribute of lister-item mode-advanced
movie_containers = html_soup.find_all('div', class_='lister-item mode-advanced')
print(type(movie_containers))
print(len(movie_containers))

first_name = first_movie.h3.a.text
