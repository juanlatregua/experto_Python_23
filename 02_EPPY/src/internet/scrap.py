import requests
from time import sleep
from random import randint

from bs4 import BeautifulSoup


years = [str(i) for i in range(2019,2021)]
start_movies = [str(i) for i in range(1,200,50)]

movie_titles = []
movie_years = []
movie_ratings = []
movie_votes = []
errors = []

for year in years:
    for start_movie in start_movies:
        url = f'https://www.imdb.com/search/title/?title_type=feature&release_date={year}&start={start_movie}&sort=user_rating,desc'

        print(f"{year} - {start_movie}")
        sleep(randint(1,3))

        content = requests.get(url)
        print(content.request.headers)
        page = content.text

        if content.status_code != 200:
            error = f'Request failed {url}, code = {content.status_code}'
            error.append(error)
            print(error)
            continue

        soup = BeautifulSoup(page, 'html.parser')
        main = soup.find(id = 'main')
        containers = main.find_all('div', class_ = 'lister-item mode-advanced')

        for movie in containers:
            header = movie.find('h3', class_ = 'lister-item-header')
            title = header.find('a').text.strip()
            year_movie = header.find('span', class_ = 'lister-item-year text-muted unbold').text.strip()
            ratings_bar = movie.find('div', class_ = 'ratings-bar')
            rating_str = ratings_bar.find('strong')

            if rating_str:
                rating = float(rating_str.text.strip())
            else:
                rating = 0.0

            span_votes = movie.find('p', class_ = 'sort-num_votes-visible')
            votes = 0

            if span_votes:
                n_votes = span_votes.find('span', attrs = {'name' : 'nv'})
                if n_votes:
                    votes = int(n_votes['data-value'])

            movie_titles.append(title)
            movie_years.append(year_movie)
            movie_ratings.append(rating)
            movie_votes.append(votes)

print(movie_titles)
print(movie_years)
print(movie_ratings)
print(movie_votes)
print(errors)