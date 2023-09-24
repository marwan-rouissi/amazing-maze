# amazing-maze

## Contexte

Inspiré du mythe du Minautore, ce projet consiste à concevoir deux programmes; l'un pour la génération de labyrinthes et le second pour la résolution.
Ces deux programmes; eux mêmes dotés de deux méthodes chacuns.

### Méthodes de génération: 
- [récursive backtrack](https://weblog.jamisbuck.org/2010/12/27/maze-generation-recursive-backtracking)
- [Kruskal](http://weblog.jamisbuck.org/2011/1/3/maze-generation-kruskal-s-algorithm)
### Méthodes de résolution:
- backtrack
- [A* (A Star)](https://www.techno-science.net/definition/6469.html)


## Installation 
Avant de lancer le projet, assurez vous d'avoir bien installé les prérequis nécessaires:
  ```sh
  pip install -r requirements.txt
  ```

## Le Projet
![image](https://github.com/marwan-rouissi/amazing-maze/assets/115158061/6e288f79-677e-4212-9667-6fa79e683ff1)


Le programme permet à l'utilisateur de générer dans un premier temps un labyrinthe en renseignant la dimension de ce dernier ainsi que la méthode désirée parmis les 2 proposés.

Il est demandé à l'utilisateur de rentrer la dimension n (soit n un entier) du labyrinthe souhaité. Une fois généré, il est proposé à l'utilisateur de renseigner un nom à ce dernier s'il souhaite le conserver. Il sera alors enregistré dans le dossier "mazes" en format .txt et .jpg.

Le même principe s'applique à la résolution, en entrant le nom du labyrinthe à résoudre (ce nom doit être valide et le fichier .txt auquel il fait référence doit se localiser dans le dossier "mazes").

Noter que la génération en récursive backtrack est limitée, en effet, elle rencontre des difficultées lorsqu'il s'agit de générer des labyrinthes de dimension n > 22.

Cela s'explique par la limite d'appel de la récursive, celle-ci étant limitée à 1000 par défaut.

## Problématiques
Pour l'observation, nous avons principalement utilisé le module cProfile.

La problématique majeure concerne le temps d'exécution du programme.

Plus celui-ci a une dimension n grande et plus l'exécution du programme prendra de temps:

| n  | génération - récursive | génération - kruskal | résolution - backtrack | résolution A* |
|----|------------------------|----------------------|------------------------|---------------|
| 10 | 0.002 seconds          | 0.005 seconds        | in 0.008 seconds       | 0.007 seconds |
| 50 | RecursionError         | 0.007 seconds        | RecursionError         | 0.398 seconds |
| 100| RecursionError         | 15.796 seconds       | RecursionError         | 2.566 seconds |
| 150| RecursionError         | 60.451 seconds       | RecursionError         | 14.239 seconds|

Celà s'explique par la complexité exponentielle (une boucle dans une boucle)
Plus la dimension n est grande et plus le programme devra faire d'itérations (n x n)

Je vois difficilement comment optimiser le programme de ce coté là.

Cependant nous avons réussi à optimiser la méthode A*.
## Optimisation
### Pour une résolution de labyrinthe de n = 100
- Avant optimisation :

![image-1](https://github.com/marwan-rouissi/amazing-maze/assets/115158061/5cbc8a86-8c0c-4232-9ea8-b4a1312d4f2a)

- Après optimisation :

![image-2](https://github.com/marwan-rouissi/amazing-maze/assets/115158061/0368aadb-a3ab-40ab-8007-553a86e381bf)


Nous constatons que dans le premier cas, il faut à notre programme environ 71 secondes pour reconstituer le path (chemin menant du point d'entrée vers la sortie) et environ 21 secondes dédiée à la méthode "append" de la liste permettant cette reconstitution.

En remplaçant cette méthode "append" par la méthode "expend", on constate le gain considérable en comparant les 2 images ..

On passe alors d'environ 96s à moins de 3s.

## Conclusion

Que ce soit pour la génération ou la résolution, nous avons pu constater les limites de la méthode backtrack.

Quelle soit récurcive ou itérative, celle-ci se voit limitée par la complexitée algorithmique indue par l'itération d'une matrice de dimension (Big O = n x n).

Plus cette matrice sera grande et plus le temps imparti à la parcourir sera conséquent.

Nous avons également compris l'importance de fragmenter et de tester un programme en observant le temps d'exécution de ce dernier ainsi que de ses composantes en vue d'identifier les goulots d'étranglement et d'en optimiser les algorithmes pour avoir un code plus rapide à l'exécution.

[Apprendre l'optimisation du code avec Python.](https://python-scientific-lecture-notes.developpez.com/tutoriels/note-cours/apprendre-python-optimisation-code/#)
