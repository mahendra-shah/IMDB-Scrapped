import json, os
import requests
from bs4 import BeautifulSoup


def scrap_movie_details():
    positions = []      # all in integer
    movie_names = []    # all in string
    years = []          # all in integer
    ratings = []        # all in float
    urls = []           # all urls of movies
    main_url = "https://www.imdb.com"
    URL = "https://www.imdb.com/india/top-rated-indian-movies/"
    sample = requests.get(URL)
    soup = BeautifulSoup(sample.text,"html.parser")

    divs = soup.find("div", class_="lister")
    tbody = divs.find("tbody", "lister-list")
    trs = tbody.findAll("tr")
    position_count = 1
    for tr in trs:
        position = position_count     
        name = tr.find("td", class_="titleColumn").a.get_text()       
        year = tr.find("td", class_="titleColumn").span.get_text()
        rating = tr.find("td", class_="ratingColumn imdbRating").get_text()
        url = tr.find("td", class_="titleColumn").a["href"]

        positions.append(position)
        movie_names.append(name)
        years.append(int(year[1:-1]))
        ratings.append(float(rating[1:4]))
        urls.append(main_url+url)
        position_count+=1

    allMovies = []
    details = { "position": "", "name":"" ,"year":"", "rating":"", "url": "" }
    for i in range(len(positions)):
        details["position"] = positions[i]
        details["name"] = movie_names[i]
        details["year"] = years[i]
        details["rating"] = ratings[i]
        details["url"] = urls[i]
        allMovies.append(details.copy())

    if os.path.exists("task1.json"):
        # with open("Marvel_Movies.json", "r") as f:
            print("data already exists")
    else:
        with open("task1.json", "w") as f:
            json.dump(allMovies, f, indent=4)
    return "Done!"
    
scrap_movie_details()