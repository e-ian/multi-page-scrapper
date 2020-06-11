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

# variable first_movie to return container of first movie in movie_containers
first_movie = html_soup.find(class_='lister-item mode-advanced')
# first movie name
first_name = first_movie.h3.a.text
print(first_name)
# first movie year
first_year = first_movie.h3.find('span', class_='lister-item-year text-muted unbold').text
print(first_year)
# first movie imdb
first_imdb = float(first_movie.strong.text)
print(first_imdb)
# first movie metascore
first_mscore = int(first_movie.find('span', class_='metascore favorable').text)
print(first_mscore)
