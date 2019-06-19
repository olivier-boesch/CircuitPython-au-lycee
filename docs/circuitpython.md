# CircuitPython (Guide de démarrage rapide...)

Il existe toute une famille de microcontrôleurs se programmant avec CircuitPython. On se concentrera ici sur le feather M4 express utilisé dans le projet.

![feather m4 express](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/m4express/featherm4express.jpg) 

## Python et CircuitPython

Premièrement, ce guide n'a pas pour fonction de vous apprendre à programmer en python. D'autres personnes le font et bien mieux que je pourrais le faire.

Pour apprendre python, un bon tutoriel : [Apprenez à programmer en Python](http://sdz.tdct.org/sdz/apprenez-a-programmer-en-python.html)

Néanmoins, par observation, essai et erreur, on peut presque s'en sortir.

### CircuitPython, c'est quoi ?

C'est une version modifiée et minimale de python version 3. Toutes les fonctions et modules ne sont pas présents. En effet, l'espace est très restreint sur un microcontrôleur.

Pour les anglophones, L'excellent guide de Adafruit : [https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials](https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials)

### Petit mot sur les microcontrôleurs

Par définition, d'après wikipedia : "Un microcontrôleur (en notation abrégée µc, ou uc ou encore MCU en anglais) est un circuit intégré qui rassemble les éléments essentiels d'un ordinateur : processeur, mémoires (mémoire morte et mémoire vive), unités périphériques et interfaces d'entrées-sorties. Les microcontrôleurs se caractérisent par un plus haut degré d'intégration, une plus faible consommation électrique, une vitesse de fonctionnement plus faible (de quelques mégahertz jusqu'à plus d'un gigahertz) et un coût réduit par rapport aux microprocesseurs polyvalents utilisés dans les ordinateurs personnels.

Par rapport à des systèmes électroniques à base de microprocesseurs et autres composants séparés, les microcontrôleurs permettent de diminuer la taille, la consommation électrique et le coût des produits. Ils ont ainsi permis de démocratiser l'utilisation de l'informatique dans un grand nombre de produits et de procédés.

Les microcontrôleurs sont fréquemment utilisés dans les systèmes embarqués, comme les contrôleurs des moteurs automobiles, les télécommandes, les appareils de bureau, l'électroménager, les jouets, la téléphonie mobile, etc."

En résumé, moins rapide, pas de clavier, souvent sans écran et peu de stockage mais il fait peu mais bien.

## le Feather m4 express

### Caractéristiques
Cette carte microcontrôleur fabriqué par adafruit regroupe:
* un microprocesseur ATSAMD51 cadencé à 120MHz
* un mémoire de 2Mo
* une led neopixel RGB
* plein d'autres choses dont un circuit de charge de batterie Lithium/Polymère.

### Fonction des broches (pinout)
[![feather m4 express pinout](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/m4express/m4expresspinout_s.png)](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/m4express/m4expresspinout.pdf) 

## Ecrire un programme : choix d'éditeur de code

Avant de commencer : FUYEZ NOTEPAD! Ce n'est pas un éditeur de code et vous finirez bien souvent avec des problèmes obscures et difficiles à résoudre.

Un bon choix possible est l'éditeur Mu ([https://codewith.mu/](https://codewith.mu/)). Simple, fonctionnel et il gère nativement CircuitPython.

Comme vous écrivez directement le programme sur la mémoire du microcontrôleur, il faut choisir un éditeur capable de travailler sans cache (difficile à trouver). un comparatif en anglais ici : [https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code](https://learn.adafruit.com/welcome-to-circuitpython/creating-and-editing-code)

A noter : il existe un editeur pour android (pratique pour les lycées posseseur de tablettes). voir sur [google play](https://play.google.com/store/apps/details?id=com.foamyguy.circuitpythoneditor). Vous aurez besoin d'un adaptateur usb hote (quelques €uros sur amazon)

## La structure habituelle d'un programme

Un programme classique se décompose en quatre parties :

* les imports de librairies (```import``` ...)
* les fonctions écrites pour modulariser le code (commençant par ```def``` ...)
* les initialisations
* la boucle d'éxécution (commençant par ```while True``` ...)

Exemple: Ce programme lit la valeur de l'entrée A0, traduit la valeur en tension électrique et l'envoie vers le port série (avec son unité).
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
### port série

### port i2C (two wires)

## Références en anglais

L'excellent guide de adafruit (les concepteurs de CircuitPython) : [https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials](https://learn.adafruit.com/circuitpython-essentials/circuitpython-essentials)