def score_is_above_5_5(j):
    if j['imdb'] > 5.5:
        return True
    else:
        return False
    

def list_of_good_films(j):
    if j['imdb'] > 5.5:
            return True
    else:
        return False

def show_films_from_category(movies,your_category):
    films = []
    for j in movies:
        if j['category'] == your_category:
            films.append(j['name'])
    return films

def average_IMDB(movies):
    sum = 0
    for j in movies:
        sum += j['imdb']
    sum_av = sum / len(movies)
    return sum_av

def average_IMDB_fromCategory(movies,your_category):
    sum = 0
    num_of_films = 0
    for i in movies:
        if i['category'] == your_category:
            num_of_films += 1
            sum += i['imdb']
    av = sum / num_of_films
    return av
    

