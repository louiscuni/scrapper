# scrapper
## HOW TO USE
### Installation
- Ce projet est réalisé avec python 3.9, il est nécessaire d'avoir une version égale ou supérieure.
- De plus, la donnée est stockée sur SQLite et utilise le package sqlite3 : pour installer ces composant : https://www.tutorialspoint.com/sqlite/sqlite_installation.htm
- Enfin, les autres librairies peuvent être installées par 
```pip install -r requirements.txt```
### Prise en main
La db est déjà pré remplie par une vingtaine d'articles pour quelque catégorie. Il est possible d'interagir avec celle-ci grace à une API. Pour la lancer :

```python run.py```

et suivre les instructions qui s'affichent.

Il est possible de reconstruire une DB. Pour ça :

```sqlite3 DatabaseName.db```

puis 

```python db_builder.py```

Pour remplir cette DB :

```python controller_db.py```

Dans ce fichier, se trouve un paramètre : DEEPNESS qui représente la profondeur du scrapping, eg, le nombre de fois que le programme va cliquer sur 'load more'

### Étapes suivantes
- ajouter des vérifications aux routes, eg vérifier les bonnes valeurs
- ajouter des routes d'écritures
- ajouter des catégories à scrapper
- vérifier les données scrappées
- monitorer les injections en db (nombre de lignes crées, pertes d'information, données non liées)
- multithreader le scrapping

### Commentaire
j'ai travaillé sur ce projet en imaginant qu'il serait utilisé à des fins pédagogiques. C'est pourquoi j'ai choisi SQLite qui permet d'avoir une DB par installation et donc de permettre aux élèves de pouvoir travailler sans modifier les DB des autres. De plus, les routes codées ont été pensées pour être un modèle très simple afin que les élèves puissent découvrir par eux même l'écriture de routes plus complexes. Toujours dans cette logique, je n'ai pas poussé le scrapping au-delà du nécessaire.

