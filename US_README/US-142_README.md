# Ajout d'une fonction prenant le nom d'une Room en paramètre et retournant l'historique des messages mis en forme

### Etape 1 :
Création d'une fonction `test_reception_historique` dans le fichier `testServer.py` qui créer une nouvelle `Room`, un `User` et un `Message` associé à la room, et qui va comparer le retour de la fonction à tester avec un template de message mis en forme.

### Etape 2 : 
Création d'un fonction `getHistorique` dans le fichier `QuickChat_server.py` qui prend en paramètre le nom d'une room et qui retourne la liste des messages stockés dans la base de données, liés à cette room. La liste retournée est une liste de châine de caractères mis en forme selon le formatage suivant : '{date} - {user} : {message text}'.

### Etape 3 :
Execution des tests sur la fonction pour s'assurer du bon fonctionnement.

### Etape 4 :
Rédaction du readme.