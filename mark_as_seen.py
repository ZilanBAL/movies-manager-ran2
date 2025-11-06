from utilities.csvmanager import load_csv
from utilities.csvmanager import save_csv

def mark_as_seen():
    movies=load_csv()
    query=input("Quel film voulez-vous marquer comme vu ?").strip()

    for movie in movies:
        if query.lower()==movie["titre"].lower():
            movie["vu"]=True
            print(f"{movie["titre"]} marqué vu")
    save_csv(movies)