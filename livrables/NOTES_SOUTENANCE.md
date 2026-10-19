# Notes de soutenance — trame orale

## Ouverture
« J’ai analysé les ventes parisiennes du fichier fourni sur la période 2017–2021 pour décrire l’évolution des appartements et des locaux. J’ai ensuite évalué un modèle sur l’année 2021, non utilisée pour son apprentissage, avant de l’appliquer au portefeuille à la date demandée du 31 décembre 2022. »

## Marché
« Le prix moyen au mètre carré des appartements augmente de 9,493 € en 2017 à 10,675 € en 2020, puis baisse à 10,456 € en 2021. Les prix varient fortement selon l’arrondissement. Ces moyennes reflètent les biens effectivement vendus et ne corrigent ni l’inflation ni les caractéristiques détaillées des logements. »

## Modèle
« J’ai transformé le code postal et le type de bien en variables indicatrices. La date, le type, la localisation et la surface réelle sont les variables d’entrée. J’ai entraîné sur 2017–2020, puis évalué sur 2021. Le modèle prédit le prix au mètre carré en échelle logarithmique; je le reconvertis ensuite en euros et le multiplie par la surface. L’erreur absolue relative moyenne observée en 2021 est 7.87%. »

## Portefeuille
« Le portefeuille contient 275 biens. La somme des estimations atteint 180,358,088 €, ventilée entre appartements (74,566,947 €) et locaux (105,791,141 €). Le fichier ne précise pas de branches de l’entreprise, donc je ne présente pas cette ventilation comme telle. »

## Limites et ouverture
« Le test 2021 donne un indicateur de performance passé; il ne garantit pas la précision en 2022. L’historique ne décrit pas l’état, l’étage, le DPE, la qualité, les conditions de vente ni toutes les caractéristiques des locaux. Pour rendre l’estimation plus fiable, il faudrait enrichir les données, contrôler les doublons avec un identifiant de transaction et confronter les estimations à des références de marché ou expertises indépendantes. »
