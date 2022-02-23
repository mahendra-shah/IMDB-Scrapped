import json
def group_by_decade():
    with open("task1.json", "r") as f:
        content = json.load(f)
    
    years = [x['year'] for x in content]
    maxYear, minYear = max(years), min(years)
    
    if minYear % 10 !=0:
        minYear = minYear - minYear%10

    decades = [x for x in range(minYear, maxYear) if x%10 == 0]
    finalResult = {}

    for dec in decades:
        movieResult = []
        for detail in content:
            if detail['year'] >= dec and detail['year'] < dec + 10:
                movieResult.append(detail)
        finalResult[dec] = movieResult
    
    return finalResult

with open('task3.json', 'w') as f:
    json.dump(group_by_decade(), f, indent=4)