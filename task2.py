import json
with open("task1.json","r") as f:
    c=json.load(f)

def group_by_year(movies):
    years=[]
    for i in movies:
        yr=i["year"]
        if yr not in years:
            years.append(yr)
    movie_dict = {i:[]for i in years}

    for j in movies:
        yy = j["year"]
        for x in movie_dict:
            if str(yy) == str(x):
                movie_dict[x].append(j)
    h = json.dumps(movie_dict,indent = 4)
    with open("task2.json","w") as f:
        f.write(h)

group_by_year(c)