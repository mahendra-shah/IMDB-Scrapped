import json, requests
from bs4 import BeautifulSoup

def scrape_movie_details(movie_url):
    main_url = "https://www.imdb.com"    ### main site url
    directors = []          # directors area
    languages = []          # languages area
    genres = []             # genres area

    data = requests.get(movie_url)
    soup = BeautifulSoup(data.text, "html.parser")

    #### movie title
    name = soup.find("div", class_="TitleBlock__TitleContainer-sc-1nlhx7j-1 jxsVNt")
    title = name.h1.text

    #### movie runtime
    runtimes = soup.find("li", attrs={"data-testid":"title-techspec_runtime"}).div.get_text()

    #### movie genre
    genre_li = soup.find("li", attrs={"data-testid":"storyline-genres"})
    genre_ul = genre_li.find("ul", class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content base")
    genre_li = genre_ul.find_all("li")
    for genre in genre_li:
        genres.append(genre.text)
    
    #### bio
    ubio = soup.find("span", attrs={"data-testid":"plot-xl"})
    summary = ubio.text

    #### directors
    director_writter_ul = soup.find("ul", class_="ipc-metadata-list ipc-metadata-list--dividers-all title-pc-list ipc-metadata-list--baseAlt")
    director_ul = director_writter_ul.find_all("li")[0].find("ul", class_="ipc-inline-list ipc-inline-list--show-dividers ipc-inline-list--inline ipc-metadata-list-item__list-content baseAlt")
    for director in director_ul.find_all("li"):
        directors.append(director.text)

    #### country
    origin_country = soup.find("li", attrs={"data-testid":"title-details-origin"}).a.get_text()

    #### Languages   
    language = soup.find("li", attrs={"data-testid":"title-details-languages"})
    lang = language.find_all("a")
    for lan in lang:
        languages.append(lan.text)

    #### poster url
    poster = soup.find("a", class_="ipc-lockup-overlay ipc-focusable")["href"]

    # data return here
    data = []
    details = { "name":title, "director":directors, "country":origin_country, "language": languages, "poster-image-url":main_url+poster, "bio":summary, "runtime":runtimes, "genre":genres }
    data.append(details)
    return data

llst = []
with open("task1.json",'r') as f:
    data = json.load(f)
for i in range(len(data)):
    llst.extend(scrape_movie_details(data[i]['url']))
    with open("task4.json",'w') as f:
        json.dump(llst, f, indent=4)
        print(i)
        