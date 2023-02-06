from my_func_for_films import *

movies = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

print("Choose what you want to tkonw:")
print("1.a single movie and returns True if its IMDB score is above 5.5")
print("2.a sublist of movies with an IMDB score above 5.5.")
print("3.a category name and returns just those movies under that category.")
print("4.compute the average IMDB score")
print("5.a category and compute the average IMDB score")

print("Choose the number")
n = int(input())
if n == 1:
    print('I will show you a single movie with its high IMDB score')  
    for j in movies:
        print(j['name'], score_is_above_5_5(j))
elif n == 2:
    print("List of films with the score more than 5.5")
    good_films = []
    for j in movies:
        if (list_of_good_films(j)):
            good_films.append(j['name'])
    print(good_films)            
elif n == 3:
    print("Choose the category")
    your_category = input()
    print(show_films_from_category(movies,your_category))
elif n == 4:
    print(average_IMDB(movies))
else:
    print("Choose the category")
    your_category = input()
    print(average_IMDB_fromCategory(movies,your_category))