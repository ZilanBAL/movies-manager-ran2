from add import add_movie
from list_movie import list_movies
from search_movies import search_movies
from delete_movie import delete_movie
from mark_as_seen import mark_as_seen

print("Bienvenu dans le gestionnaire de film! \n")
while True:
    print("Choix disponible:")
    print("1. Ajouter un film")
    print("2. Lister des films")
    print("3. Supprimer un film")
    print("4. Rechercher un film")
    print("5. Marquer un film comme vu")
    print("6. Quitter")
    choice= input("votre choix?").__str__()

    match choice:
        case "1":
            add_movie()
        case "2":
            list_movies()
        case "3":
            delete_movie()
        case "4":
            search_movies()  
        case "5":
            mark_as_seen()
        case "6":
            print("Au revoir!")
            confirm=input("Voulez-vous vraiment quitter le programme? [o/N]").strip().lower()=="o"
            if confirm:
                print("Au revoir!")
                exit()
            else:
                print("Ok, retour au menu principal")
        case _:
            print("Mauvais choix")

        

