# Notes de soutenance — trame orale

## Ouverture

« J’ai étudié les ventes parisiennes du fichier fourni entre 2017 et 2021. J’ai ensuite évalué une régression linéaire sur l’année 2021, tenue à l’écart de l’apprentissage, avant d’estimer la valeur du portefeuille au 31 décembre 2022. »

## Marché

« Le prix moyen des appartements passe de 9 493 €/m² en 2017 à 10 675 €/m² en 2020, puis à 10 456 €/m² en 2021. En 2021, la moyenne va d’environ 8 829 €/m² dans le 19e à 13 795 €/m² dans le 6e. Ces écarts sont descriptifs : ils ne neutralisent ni les caractéristiques des biens vendus ni l’inflation. »

## Régression et portefeuille

« Le modèle utilise la date, la surface, le code postal et le type de bien. Les variables catégorielles sont transformées en indicatrices. L’apprentissage porte sur 2017–2020 et le test sur 2021. L’erreur absolue relative moyenne est de 7,87 %, sous l’objectif de 10 %, mais le biais moyen est de +7,86 % : les estimations surestiment en moyenne les ventes de test. Ce score passé ne garantit pas la précision sur le portefeuille. »

« Les 275 biens atteignent une valeur estimée totale de 180 358 088 € au 31/12/2022 : 74 566 947 € pour les appartements et 105 791 141 € pour les locaux. C’est une projection statistique, pas une expertise. Le fichier ne donne pas le DPE, l’état, l’étage ni le détail des locaux. »

## K-means et recommandation

« K-means regroupe les biens selon leur prix au mètre carré, sans utiliser le type pendant l’entraînement. Sur le test historique 2021, il identifie 73,6 % des locaux, mais seulement 23,3 % des biens signalés comme locaux en sont réellement. Son exactitude est de 80,1 %, sous les 92,6 % d’un classement systématique en appartement. »

« Les 40 biens de l’échantillon OpenClassrooms sont tous dans le 19e et sont classés appartements par le modèle. Nous n’avons pas les étiquettes réelles de l’équipe de Louise pour vérifier ce résultat. Je recommande de ne pas automatiser la décision d’achat. Avant tout usage opérationnel, il faut récupérer ces étiquettes et faire contrôler chaque résultat par un conseiller. »

## Points à rappeler

- Les 16 lignes historiques parfaitement identiques sont conservées, faute d’identifiant permettant de trancher.
- Les prix moyens dépendent de la composition des biens vendus; les corrélations ne décrivent pas de liens de cause à effet.
- La valeur estimée du portefeuille est extrapolée au-delà de l’historique disponible.
- La ventilation du portefeuille est faite par type de bien, car aucune branche d’entreprise n’est renseignée.
