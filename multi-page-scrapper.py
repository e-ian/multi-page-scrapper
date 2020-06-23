from requests import get
from bs4 import BeautifulSoup
import pandas as pd

url = 'http://www.imdb.com/search/title?release_date=2017&sort=num_votes,desc&page=1'

response = get(url)

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
#first movie votes
first_votes = int(first_movie.find('span', attrs = {'name':'nv'})['data-value'])
print(first_votes)

# Lists to store the scraped data
names = []
years = []
imdb_ratings = []
metascores = []
votes = []

# Extract data from individual movie container
for container in movie_containers:
# If the metascore is not none, then extract
    if container.find('div', class_='ratings-metascore') is not None:
        name = container.h3.a.text
        names.append(name)

        year = container.h3.find('span', class_='lister-item-year').text
        years.append(year)

        imdb = float(container.strong.text)
        imdb_ratings.append(imdb)

        m_score = container.find('span', class_='metascore').text
        metascores.append(int(m_score))

        vote = container.find('span', attrs = {'name':'nv'})['data-value']
        votes.append(int(vote))

test_df = pd.DataFrame({
    'movie': names,
    'year': years,
    'imdb': imdb_ratings,
    'metascore': metascores,
    'votes': votes
})
print(test_df.info())

