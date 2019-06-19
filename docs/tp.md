# Les travaux pratiques autour des capteurs

## Organisation générale des séances
### Items du programme abordables

Rappel de l'item du programme : "_Mesurer une grandeur physique à l’aide d’un capteur électrique résistif. Produire et utiliser une courbe d’étalonnage reliant la résistance d’un système avec une grandeur d’intérêt (température, pression, intensité lumineuse, etc.). Utiliser un dispositif avec microcontrôleur et capteur._"

On peut donc se concentrer ici sur l'établissement d'un modèle du capteur entre la valeur de la résistance et le paramètre physique extérieur mesuré (angle, température, luminosité).

En outre, il est également possible de réinvestir les parties du programme traitant de la loi d'ohm et des lois des circuits électriques ("_Exploiter la loi des mailles et la loi des nœuds dans un circuit électrique comportant au plus deux mailles. Mesurer une tension et une intensité. Utiliser la loi d’Ohm._") à travers l'intégration du capteur dans le circuit.

### Déroulement type d'une séance

* On utilise le capteur avec un ohmmètre pour réaliser plusieurs mesures et créer la courbe d'étalonnage. On obtient :
    * le graphique de l'étalonnage modélisable par : une droite, des segments de droite ou autre...
    * Une relation entre la valeur de la résistance et la grandeur intérêt.
* facultatif : On intègre le capteur dans le montage avec microcontrôleur par un pont de résistance : on obtient la relation par calcul (loi d'ohm et loi des mailles).
* On intègre les relations dans le code du microcontrôleur (ici sous forme de code python à compléter).
* On vérifie son travail par plusieurs mesures et un affichage direct sur l'écran du microcontrôleur.

## Propositions de travail
### Le capteur d'angle
__Objectif : Créer un capteur d'angle à l'aide d'un potentiomètre__

Il est utilisé comme capteur pour l'entrée d'air dans le carburateur de moteurs d'avion (plus de carburateurs dans les voitures à essence depuis 1993):

![capteur papillon](https://raw.githubusercontent.com/olivier-boesch/CircuitPython-au-lycee/master/TPs/angle/capteur_papillon.jpg)

ou dans un pédale de guitare "wahwah" pour contrôler l'effet:

![pedale wahwah](https://raw.githubusercontent.com/olivier-boesch/CircuitPython-au-lycee/master/TPs/angle/wahwah.jpg)

[la pédale en action](https://youtu.be/uB0I9mvXv2Q?t=701)

### Le thermomètre
__Objectif : Créer un thermomètre à l'aide d'une thermistance__

### Le luxmètre 
__Objectif : Créer un luxmètre à l'aide d'une photorésistance__