longueur = 1.8; //mm
diametre_interieur = 3; //mm
jeu = 0.25; //mm
epaisseur = 1; //mm
$fn=200;
difference(){
    //exterieur
    cylinder(d=diametre_interieur + 2 * jeu + 2 * epaisseur, h=longueur);
    //trou
    translate([0,0,-jeu]) cylinder(d=diametre_interieur + 2 * jeu, h=longueur + 2 * jeu);
}
