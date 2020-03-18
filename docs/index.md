# The project

## why this project
This project is all about teaching physics and chemistry with microcontrollers.

As a physics and chemistry teacher, I have to also teach my students to create/use models and sensors applied to microcontrollers.

## the Adafruit feather M4 express 

Not satisfied with arduino board, i searched for a microtroller that suits my needs :
* Can be programmed with python (and C if I need more performance)
* Can output a true analog signal (not just pwm).
* a screen already integrated or can fit easily on top
* some integrated buttons are always useful 

And the winner is...

After some trial/errors, my best candidate is the Adafruit feather M4 express :
* lots of power and two DACs to play audio
* an oled featherwing on top for the screen and buttons
* can add a battery

## A step further

After that, I some more handy ports to make my students have a better experience with that board:
* Add an arduino like port to connect cables and teach them electricity
* Add some grove port when we are using sensors/actuators
* Add a 3.5mm jack plug to output audio easily to speakers/headphones
* Add breadboard to make circuity
* Put everything together to move it easily

## the result

The first proto looks like this :

![Board](https://github.com/olivier-boesch/CircuitPython-au-lycee/raw/master/docs/assets/pythonmcu_500.jpg "Board")

## Many thanks to :
Un grand merci à Antony Meunier, Professeur de STI2D Itec au lycée Saint éxupéry, pour l'aide au design et la maîtrise de la découpe laser.

A Mmes Ourida Smahi, Sylvie Ségui et Chantal Le Nivet, technicienne et adjointes de laboratoire, pour l'aide au montage et l'enthousiasme (1140 soudures à 2! sans compter le montage...).

A Damien Muti, professeur de physique chimie en section arts appliqués et générale, pour m'avoir soufflée l'idée du tutoriel sur CircuitPython. 
