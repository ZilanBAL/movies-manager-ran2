import csv
import os
# chemin vers le fichier CSV utlisié pour sauvegarder les films
CSV_FILES_PATH= "films.csv"
FILED_NAMES=["titre","année","genre","vu"]

def save_csv(data:dict):
    """cette fonction enregistre le dictionnaire `data` dans le csv configuré dans le `CSV_FILE_PATH`"""
    """attention: cette fonction écrase le contenu csv existant"""
    formatted_data=[]
    for movie in data:
        formatted_data.append({
                "titre":movie["titre"],
                "année":movie["année"],
                "genre":movie["genre"],
                "vu":"oui" if movie ["vu"] else "non"
                # possible d'écrire juste
                # *** movie,
                # "vu":"oui" if movie ["vu"] else "non"
            })

    with open(CSV_FILES_PATH,"w", newline='',encoding="utf-8") as file :
        writer=csv.DictWriter(file, fieldnames=FILED_NAMES)
        writer.writeheader()
        writer.writerows(formatted_data)

def load_csv()-> dict:
    """cette fonction va lire le fichier CSV et retourner son contenu sous forme d'une liste de dict"""
    if not os.path.exists(CSV_FILES_PATH):  
        return[]
    data=[]
    with open (CSV_FILES_PATH, "r",newline='', encoding="utf-8") as file:
        
        reader=csv.DictReader(file)
        for movie in reader:
            data.append({
                "titre":movie["titre"],
                "année":int(movie["année"]),
                "genre":movie["genre"],
                "vu":movie["vu"]== "oui"
            })
    return data


