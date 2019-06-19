# CircuitPython

## Python et CircuitPython



## Ecrire un programme : choix d'éditeur de code

Avant de commencer : FUYEZ NOTEPAD! Ce n'est pas un éditeur de code et vous finirez bien souvent avec des problèmes obscures et difficiles à résoudre.

Un bon choix possible est l'éditeur Mu ([https://codewith.mu/](https://codewith.mu/)). Simple fonctionnel et il gère nativement CircuitPython.

Comme vous écrivez directement le programme sur la mémoire du microcontrôleur, il faut choisir un éditeur capable de travailler sans cache (difficile à trouver).

## La structure habituelle d'un programme

Un programme classique se décompose en quatre parties :

* les imports de librairies (```import``` ...)
* les fonctions écrites pour modulariser le code (commençant par ```def``` ...)
* les initialisations
* la boucle d'éxécution (commençant par ```while True``` ...)

Exemple:
```python
# imports
import board
from analogio import AnalogIn

# fonctions
def calcul_tension(val_entree):
    return val_entree * 3.3 / 65535

# initialisations
entree = AnalogIn(board.A0)

# Boucle d'évécution
while True:
    tension = calcul_tension(entree.value)
    print(tension, "V")
```

## Entrées et sorties analogiques

## Entrées et sorties digitales

## Fonctions spéciales

## Références en anglais

L'excellent guide de adafruit (les concepteurs de CircuitPython) : [https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials](https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials)