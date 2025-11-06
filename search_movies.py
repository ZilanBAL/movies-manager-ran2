from utilities.csvmanager import load_csv
import Levenshtein

def search_movies():
    movies=load_csv
    query=input("Entrez le mot clé à rechercher:")
    
    for movie in movies:
        dst=Levenshtein.distance(movie["titre"], query)
        is_partial_match =query.lover().strip() in movie["titre"].lower()
        is_approx_match = dst <=5
        if is_approx_match or is_partial_match:
             print(f"-> {movie["titre"]} {movie["année"]} {movie["genre"]} {"VU" if movie["vu"]else ''}")