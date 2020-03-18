# Le projet

Ceci est la version 2 du projet

## Pourquoi ce projet
Ce projet a été fait pour enseigner les sciences avec un microcontrôleur.

Comme enseignant en sciences physiques, Je dois également apprendre à mes élèves à utiliser des modèles et des capteurs autour de microcontrôleurs.

## Le feather M4 Express de Adafruit 
Pas vraiment satisfait avec les arduino, Je me suis mis en recherche d'un microcontrôleur qui convenait à mes attentes :
* Peut être programmé avec python (ou C si je recherche plus de performance)
* Peut emettre un vrai signal analogique (et pas juste du pwm)
* un écran intégré ou facilement intégrable
* des boutons intégrés (toujours utile)

Et le gagnant est ...

Après quelques essais erreurs, Mon meilleur candidat est le feather m4 express de Adafruit :

* beacoup de puissance et deux DACs pour jouer de l'audio
* un featherwing oled par dessus qui fournit l'écran et les boutons
* On peut ajouter une batterie (le circuit de charge est déjà intégré) pour avoir de l'indépendance

## Un peu plus loin

Après ça, J'avais besoin de connectique qui s'adapte aux besoins des élèves :

* Une connectique semblable aux arduino pour connecter fils, résistances, leds...
* des ports grove pour ajouter facilement des capteurs, modules bluetooth, ... 
* une prise jack 3.5mm pour connecter un casque ou des enceintes
* Une plaque de prototypage pour faire des circuits (et travailler l'électricité)
* Mettre tout cela ensemble pour être pratique à transporter

## Le résultat

Le premier prototype ressemble à ceci

![Board](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/docs/assets/pythonmcu_500.jpg "Board")

## Vous voulez en construire une vous même

Tout est sur le repo de github (voir en haut de page)

## Vous voulez en acheter une toute faite

Contactez la société qui a accepté des les fabriquer!
```
Maison des Enseignants de Provence (MEP)
https://www.la-mep.com/
268 avevue de la capelette
Bat H
13010 Marseille
France

Tel : +33 4 91 78 02 01
email : commande@la-mep.com
```

## Un grand merci (ils ont participé à la version 1) :
Antony Meunier, Professeur de STI2D Itec au lycée Saint éxupéry (Marseille), Pour son aide dans le design de la v1 et sa maitrise de la découpe laser.
A Mmes Ourida Smahi, Sylvie Ségui et Chantal Le Nivet, technicienne et adjointes de laboratoire, pour leur aide dans l'assemblage de la version 1. 
