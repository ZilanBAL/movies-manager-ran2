Consignes
1. Créez un fichier films.csv s’il n'existe pas déjà. Il contiendra les colonnes suivantes :

titre,année,genre,vu
Exemple de contenu :

Inception,2010,SF,oui
Titanic,1997,Romance,non
2. Identifiez, puis créez une fonction pour chaque action nécessaire :

ajouter_film() : demande les infos, ajoute une ligne au fichier.
afficher_films() : lit le CSV et affiche joliment la liste.
rechercher_film() : cherche un titre (insensible à la casse).
supprimer_film() : supprime une entrée du CSV.
marquer_comme_vu() : modifie le champ vu à "oui".
menu() : affiche le menu principal et redirige vers les fonctions.
3. Le fichier est mis à jour en direct après chaque modification.

4. Vous devez utiliser le module csv (lecture/écriture avec DictReader / DictWriter).

5. Extra, si vous avez terminé : exporter la liste au format JSON (films.json) ou afficher quelques statistiques :

Nombre total de films
Nombre de films vus / non vus
Genres les plus représentés
Note : vous pouvez réaliser l'exercice dans la zone de code ci-dessous ou dans VSCode (pensez à utiliser Git pour sauvegarder votre code).