# Notes de soutenance — révision du 16 novembre 2026

## Ouverture

« J’ai étudié les ventes parisiennes du fichier fourni entre 2017 et 2021. J’ai ensuite entraîné
une régression linéaire pour estimer la valeur foncière, valorisé le portefeuille au 31 décembre 2022,
puis appliqué K-means aux 40 opportunités de Louise. »

## Données et marché

« Le fichier contient 26 196 lignes : 24 353 appartements et 1 843 locaux industriels, commerciaux
ou assimilés. Les 16 répétitions exactes sont conservées pour décrire le fichier, mais retirées
pour la modélisation afin d’éviter leur présence dans l’apprentissage et le test. »

« Le prix moyen des appartements passe de 9 493 €/m² en 2017 à 10 675 €/m² en 2020,
puis à 10 456 €/m² en 2021. Cela représente +10,1 % entre 2017 et 2021 et -2,1 % sur la dernière année.
En 2021, la moyenne va d’environ 8 829 €/m² dans le 19e à 13 795 €/m² dans le 6e.
Ces moyennes ne corrigent pas l’inflation ni les caractéristiques des biens vendus. »

« Dans le 6e arrondissement, Pearson entre date et prix au m² vaut 0,904 sur 709 appartements.
Il s’agit d’une association, pas d’une preuve de causalité. La surface est fortement liée à la valeur totale,
ce qui doit être distingué de sa relation beaucoup plus faible avec le prix au m². »

## Régression

« La cible est directement la valeur foncière totale en euros. Les variables sont la surface réelle,
la date, le code postal et le type de bien. Le prix au m² observé n’entre pas dans les variables,
car il est calculé à partir de la cible. L’encodage des catégories est appris uniquement sur l’apprentissage. »

« Je réserve 33 % des observations pour le test demandé. La MAPE, moyenne des erreurs absolues
rapportées à chaque prix réel, est de 9,14 %. La MAE est d’environ 33 803 € et le R² de 0,980. »

« Pour vérifier l’usage dans le futur, j’apprends aussi sur 2017–2020 et teste sur 2021.
La MAPE atteint alors 13,62 % et le biais relatif moyen +12,81 %. La prévision temporelle
est moins précise que le test aléatoire ; le modèle surestime en moyenne les prix de 2021. »

## Portefeuille

« Après l’évaluation, le modèle final est réentraîné sur l’historique distinct de 2017 à 2021.
Il utilise la surface réelle bâtie du portefeuille, pas la surface Carrez.
Les 275 actifs atteignent une valeur estimée de 169,70 M€ au 31/12/2022 :
71,22 M€ pour les particuliers et 98,48 M€ pour le corporate. »

« Cette ventilation repose sur la convention appartements = particuliers et locaux = corporate,
à confirmer avec l’entreprise. Les deux répétitions exactes du portefeuille sont conservées et signalées.
La valorisation corporate est supérieure, mais cela ne prouve pas une meilleure rentabilité.
La date estimée dépasse l’historique et les prix réels 2022 ne sont pas fournis. »

## K-means

« K-means est ajusté sur les 40 opportunités de Louise, à partir du seul prix au m².
Il produit deux groupes de 20 biens, centrés vers 7 409 et 9 807 €/m². La silhouette de 0,909
montre une bonne séparation des prix ; ce n’est pas un taux de classification correcte. »

« Les numéros 0 et 1 sont arbitraires. Je propose le groupe bas comme appartements et le groupe haut
comme locaux en comparant l’ordre des centres aux prix historiques du même arrondissement en 2021.
Cependant, le centre du groupe bas est 16,1 % sous la moyenne de référence des appartements.
Le fichier ne contient ni date ni type réel ; il faut donc confirmer cette interprétation avec Louise. »

## Conclusion et suites

« L’analyse décrit le fichier historique, produit une première valorisation et un classement exploratoire.
Pour aller plus loin, je ferais confirmer les actifs répétés et les segments, demanderais les types réels
et les dates des opportunités, puis enrichirais les caractéristiques des biens avant une nouvelle
évaluation chronologique. »

Le PowerPoint d’octobre doit être mis à jour avant la soutenance pour reprendre ces chiffres et méthodes.
