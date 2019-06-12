# Design
## Platine de microcontrôleur avec breaboard
### Platine
Le design de la plaque est fait de façon à n'exposer qu'une partie des broches du microcontrôleur pour éviter les mauvaises manipulations.
En effet, comme sa tension de fonstionnement est de 3,3V, les broches pouvant proposer du 5V ne sont pas accessibles. 
Le design de la plaque a été fait avec [inkscape](https://inkscape.org/fr/). 
La platine est fabriquée à partir de plexiglass (ou altuglass). La forme est obtenue par découpe laser. 

![plan de la platine](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/Platine%20d'exp%C3%A9rimentation/plaque_exp%C3%A9rimentation_pc.png "Plan platine")

### Circuit imprimé
Le circuit imprimé a été conçu à l'aide de [fritzing](http://fritzing.org/home/) et fabriqué par [JLCPCB](https://jlcpcb.com/).

![plan pcb](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/pcb/m4v06-2019_pcb.png "Plan pcb")

![photo pcb face](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/pcb/pcb_front_s.jpg "photo pcb face")
![photo pcb dos](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/pcb/pcb_back_s.jpg "photo pcb dos")



## Capteur d'angle
Le boitier du capteur d'angle est en plexiglass et le design a été fait avec [inkscape](https://inkscape.org/fr/) et découpé au laser. 

![plan capteur face](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/Platine%20capteur%20angle/plaque_pot_dessus.svg.png "Plan capteur face")
![plan capteur dos](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/Platine%20capteur%20angle/plaque_pot_dessous.svg.png "Plan capteur dos")


## Pièces d'assemblage
Le design des entretoises a été fait avec [openscad](https://www.openscad.org/). 
Les entretoises sont fabriquées par imprimante 3D en pla transparent. L'impression est faite en couches de 0,2mm

Le montage nécessite un peu de visserie :
* boulons m3 de 10mm de long pour la platine
* boulon m3 de 30mm de long pour le boitier de capteur

![boulon m3 10mm](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/assemblage/boulon_m3-10mm.jpg "boulon m3 10mm")

### Entroises pour la platine
Les entretoises font 1,8mm de hauteur, 3,5mm de diamètre intérieur et 5,5mm de diamètre extérieur.
 
![entrtoise platine plan](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/assemblage/entretoise_plaque_ex.png "entrtoise platine plan")


### Entretoises pour le capteur d'angle
Les entretoises font 20mm de hauteur, 3,5mm de diamètre intérieur et 5,5mm de diamètre extérieur.

![entrtoise capteur plan](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/assemblage/entretoise_capteur_angle.png "entrtoise capteur plan")
![entrtoise capteur](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/Mat%C3%A9riel/assemblage/entretoise_capteur_angle_3d.jpg "entrtoise capteur")


## La platine et le boitier de capteur terminés

## Coût et fournisseurs
Les composants électroniques ont été achetés chez Semageek. Le plexiglass peut être acheté chez polydis. Les circuits imprimés ont été fabriqués par JLCPCB. Les entretoises d'assemblage ont été fabriquées à la maison par imprimante 3D.

Coûts (pour 10 cartes) :
* circuits imprimés : 20€
* Plexiglass : environ 15€
* Composants : 
* pièces d'assemblage : env. 10€