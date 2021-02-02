# Ajout de la récupération des messages en fonction de l'ID d'une room

### Etape 1 :
Détermination du cahier des charges des tests et de la fonction à réaliser.

### Etape 2 : 
 - Developpement du test `test_getMessagesByRoomId` qui insert à la main une `Room`, et un `Message`, puis qui effectue une requête SQL pour récupérer les messages en fonction de l'id d'un `Room`. C'est le résultat de cette requête qui sera comparé au retour de la fonction.
 - En paralèle, l'autre élément du binôme développe la fonction `getMessagesByRoomId` qui récupère les messages liés à une `Room` dans la BDD en fonction de l'ID de cette-dernière.

### Etape 3 :
Execution des tests sur la fonction pour s'assurer du bon fonctionnement.

### Etape 4 :
Rédaction du readme.
