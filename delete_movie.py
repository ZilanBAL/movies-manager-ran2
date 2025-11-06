from utilities.csvmanager import load_csv
from utilities.csvmanager import save_csv

def delete_movie():
    movies=load_csv
    query= input("Entrez le titre du film à supprimer:").strip()

    for movie in movies.copy():
        if query.lower()== movie["titre"].lower():
            movies.remove(movie)
            print(f"{movie["titre"]} supprimé")

    save_csv(movies)
    