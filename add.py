from utilities.csvmanager import load_csv
from utilities.csvmanager import save_csv


def add_movie():
    title= input("Entrez le titre du film: ").strip().capitalize()
    year = input("Entrez l'année : ")
    genre = input("Entrez le genre : ")
    seen = input("L'avez-vous vu (oui/non) : ").strip().lower()=="o"
    
    if year and year.isdigit():
        year=int(year)
    else:
        year=0
    
    existing_movie= load_csv()
    existing_movie.append({
        "titre":title,
        "genre" :genre,
        "année":year,
        "vu" : seen
    })
    save_csv(existing_movie)
    print(f"Votre filmothèque a été sauvegardeé ! {title} a été ajouté.")

    