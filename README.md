# AÉRODYNAMIQUE HYPERSONIQUE
_Conception d’une interface de prédiction de comportement hypersonique (partie algorithme)_

## DESCRIPTION _CompressibleFlow.ipynb_

Ce fichier contient l'algorithme permettant de répondre à la problématique du projet. Dans un premier temps, vous y trouverez la définition de deux profils étudiés :
- profil simple : ogive
- profil complexe : ARIANE IV modifié

Ensuite, il est nécessaire de calculer les variables caractéristiques d'un écoulement à partir d'une altitude et d'une vitesse fournies par l'utilisateur. Les variables à déterminer sont les suivantes :
- Pression
- Température
- Densité
  
L'utilisateur devra donc spécifier une **altitude** _(z)_ et une **vitesse** _(v)_ pour la simulation.

### Classe _HypersonicObliqueShock_
La simulation se fait via la classe _HypersonicObliqueShock_, qui prend en compte cinq arguments :
- **Atmosphere** : dictionnaire contenant les propriétés thermophysiques au niveau de la mer et à l'altitude _z_
- **directory_path** : dictionnaire contenant les différents chemins d'accès au fichier **Docs**
- **altitude** : l'altitude choisie par l'utilisateur
- **profil_dictionary** : dictionnaire contenant le profil à étudier, le vecteur des dimensions des sections et un vecteur du profil total
- **FreeFlowVelocity** : vitesse choisie par l'utilisateur

L'ensemble des attributs et des méthodes permet de déterminer les propriétés de l'écoulement après le choc, de dimensionner la courbe de choc et les épaisseurs associées. Il permet également de suivre l'évolution des propriétés aux points de stagnation en amont et en aval du choc, ainsi que de calculer les coefficients de pression _C_p_, de traînée _C_x_ et de portance _C_z_. À l'instar d'_Ansys Fluent_, nous avons tenté de générer des contours de pression, de température et de densité.
