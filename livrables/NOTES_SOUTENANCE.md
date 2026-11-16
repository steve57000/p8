# Notes de soutenance — présentation révisée du 16 novembre 2026

18 diapositives. Les chiffres et les limites suivent le notebook révisé.

## 01 — Du marché à la décision

Ouverture : j’ai analysé les fichiers pédagogiques des Plus Beaux Logis de Paris. L’historique couvre 2017–2021, la valorisation demandée est au 31/12/2022 et l’échantillon de Louise comprend 40 biens. Les résultats ne décrivent pas les prix actuels de Paris. Présentation révisée le 16 novembre 2026. Photographie de Paris : Unsplash, https://images.unsplash.com/photo-1502602898657-3e91760cbb34 (visuel décoratif).

## 02 — Synthèse

Le prix au m² moyen des appartements progresse de 10.142% entre 2017 et 2021, puis baisse de -2.054% entre 2020 et 2021. Le portefeuille est estimé à 169,701,260.65€ pour 275 lignes conservées. K-means produit deux groupes de 20 opportunités, sans labels réels pour valider les types. Sources : les trois classeurs data/raw et les CSV de livrables. Aucun de ces résultats ne justifie à lui seul une décision d’achat ou de vente.

## 03 — Périmètre et qualité

Historique : 26 196 lignes, dont 24 353 appartements et 1 843 locaux industriels, commerciaux ou assimilés ; aucune valeur manquante détectée. L’absence d’identifiant de mutation empêche de garantir un nombre de transactions distinctes. Les 16 répétitions exactes restent dans les statistiques descriptives mais sont retirées de la base de modélisation : 26 180 lignes distinctes. Portefeuille : 275 lignes dont deux répétitions exactes, conservées faute de confirmation métier. Échantillon : 40 biens du 19e, sans date et sans type réel. Les sources brutes sont inchangées.

## 04 — Évolution du marché

Appartements, moyenne du prix au m² par ligne, non ratio des valeurs totales et surfaces totales. Moyennes 2017–2021 : 2017 = 9492.86 €/m², 2018 = 10031.40 €/m², 2019 = 10562.71 €/m², 2020 = 10674.87 €/m², 2021 = 10455.60 €/m². Les médianes sont montrées pour compléter les moyennes. Les statistiques ne neutralisent ni l’inflation, ni la composition des biens vendus. L’axe du prix commence à 8 500 €/m² pour rendre l’évolution lisible ; il s’agit d’une courbe de tendance et non de barres de magnitude.

## 05 — Arrondissements

Classement des 20 arrondissements pour les appartements en 2021. Le 6e atteint 13 795,05 €/m², le 19e 8 828,59 €/m² ; écart relatif de 56.25% par rapport au 19e. Les barres partent de zéro. Chaque moyenne porte sur les biens vendus dans le fichier, sans correction de surface, d’état, de qualité ou de composition. Ce résultat justifie d’examiner la localisation comme variable explicative mais ne mesure pas un effet causal. Tableau complet dans le notebook, section 1.6.

## 06 — Corrélation dans le 6e

Pearson entre la date et le prix au m², sur 709 appartements du 6e : r=0.903845. Le périmètre est local, et ne doit pas être remplacé par une corrélation sur tout Paris. Tous les points sont affichés dans le graphique ; l’axe du prix est resserré de 11 000 à 15 000 €/m² pour montrer l’association temporelle. Sur les 26 196 lignes du fichier, r(surface, valeur foncière totale)=0.983560, tandis que r(surface, prix au m²)=0.103129. Il faut distinguer la valeur d’un bien et son prix unitaire. Ces associations ne prouvent pas la causalité et ne dispensent pas de l’évaluation du modèle.

## 07 — Types de biens

Le graphique présente les moyennes annuelles des prix au m², par type, sur le fichier complet. En 2021, locaux : 12 006,49 €/m² ; appartements : 10 455,60 €/m². Les locaux regroupent des usages industriels, commerciaux et assimilés. Cette moyenne supérieure ne suffit pas à conclure que tous les locaux valent plus, ni qu’ils sont plus rentables. La composition, la localisation et les caractéristiques des biens ne sont pas neutralisées. La catégorie de type est introduite dans le modèle de valeur totale.

## 08 — Régression linéaire

Le pipeline prédit directement la valeur foncière totale (euros). Variables : surface réelle, date exprimée depuis 2017, code postal et type de bien. Les catégories sont traitées par OneHotEncoder dans un ColumnTransformer appris sur l’entraînement. Le prix au m² observé est valeur foncière/surface : le réintroduire comme variable créerait une fuite de la cible. Les 16 répétitions historiques sont retirées avant séparation. Test aléatoire demandé : 33% (8 640 lignes), 17 540 à l’apprentissage, graine 42. Un second contrôle apprend sur 2017–2020 et teste sur 2021. Après évaluation, le modèle final est réentraîné sur les 26 180 lignes distinctes de 2017–2021.

## 09 — Évaluation du modèle

Test aléatoire de 33% : MAPE 9.141018%, MAE 33802.85€, RMSE 71188.30€, R² 0.980032. Test chronologique 2021 après apprentissage 2017–2020 : MAPE 13.617991%, MAE 51997.86€, biais relatif moyen 12.812944%. Le biais est la moyenne de (prédit-réel)/réel, distincte de la MAPE. Le graphique part de zéro. Ces erreurs moyennes ne sont ni une garantie de précision par bien, ni un intervalle de prédiction pour 2022.

## 10 — Valeur totale du portefeuille

Valeur totale estimée : 169701260.65€, soit 169,70 M€, au 31/12/2022. Le modèle final est réentraîné sur les données historiques distinctes 2017–2021. Il emploie la surface réelle bâtie, pas la surface Carrez. Le portefeuille contient 275 lignes, dont deux répétitions exactes maintenues et signalées. La date estimée est au-delà de l’historique disponible ; les prix réels de 2022 ne sont pas fournis, et aucun intervalle de prédiction n’a été calculé. Il s’agit d’une estimation indicative, pas d’une expertise immobilière ni d’une valeur actuelle. CSV : predictions_valorisation_portefeuille_2022-12-31.csv.

## 11 — Répartition du portefeuille

Particuliers : 154 lignes, 6 286 m², 71 221 764,00€, 41,97% du total, moyenne de 462 478,99€ par ligne. Corporate : 121 lignes, 7 696 m², 98 479 496,65€, 58,03%, moyenne de 813 880,14€. La ventilation est conventionnelle : code 2 appartement = particuliers, code 4 local = corporate. Le fichier ne contient pas de branche commerciale. La valeur supérieure du corporate ne signifie pas meilleure rentabilité ; les loyers, charges, coûts, revenus et prix d’acquisition ne sont pas fournis. Les répétitions du portefeuille sont conservées. Vérifier la segmentation avec l’entreprise.

## 12 — Échantillon de Louise

L’échantillon a 40 biens, tous situés dans le 19e arrondissement. On connaît la valeur foncière et la surface réelle ; le prix au m² est calculé. Ni date ni type réel ne sont fournis. Le sujet mentionne 2021, mais cela ne peut pas être vérifié dans le classeur. K-means est ajusté sur le seul prix au m² de ces 40 opportunités : deux groupes, graine 42 et 20 initialisations. Les types ne sont pas utilisés à l’ajustement. Cette approche est non supervisée et exploratoire.

## 13 — Résultat K-means

Centres K-means : groupe bas 7408.775030 €/m² et groupe haut 9806.924674 €/m², 20 biens chacun. Silhouette 0.908606. Le graphique montre tous les points, avec la surface en abscisse pour rendre les observations lisibles ; la surface n’entre pas dans l’ajustement de K-means, qui utilise seulement le prix au m². Les marqueurs distinguent aussi les groupes sans dépendre de la couleur. La silhouette mesure la séparation des groupes de prix, pas un taux de types correctement identifiés.

## 14 — Interprétation des groupes

Les références locales du 19e en 2021 ont un prix au m² moyen de 8828.586057€ pour les appartements et 9737.619986€ pour les locaux. L’ordre des moyennes suggère groupe bas = appartement et groupe haut = local. Mais le centre bas est -16.082% sous la moyenne des appartements : il ne coïncide pas avec le niveau de référence. Les deux groupes ne sont pas des types validés. Le classeur ne permet pas de vérifier sa date réelle, et les numéros de clusters sont arbitraires. Ne pas annoncer 20 appartements et 20 locaux comme un décompte réel : ce sont 20 et 20 types proposés.

## 15 — Validation métier manquante

Aucun type réel n’est fourni pour les 40 opportunités. Il est donc impossible de calculer une exactitude, une précision, un rappel ou une matrice de confusion sur cet échantillon. La silhouette de 0,909 n’est pas un taux de classification correcte. Le notebook attend un fichier data/raw/labels_reference_louise.csv comportant id_opportunite et code_type_reel (2 ou 4). Il vérifie une correspondance complète, unique et valide avant de calculer ces métriques. Les labels réels ne servent pas à ajuster les clusters ni à modifier a posteriori la correspondance proposée. Demander aussi la date réelle des opportunités.

## 16 — Priorités opérationnelles

Priorité 1 : confirmer les lignes répétées du portefeuille et la convention appartements/particuliers, locaux/corporate avant d’utiliser les agrégats. Priorité 2 : demander à Louise les types réels et la date des 40 opportunités, puis évaluer les propositions. Priorité 3 : enrichir les biens avec l’état, l’étage, le DPE et les caractéristiques d’usage des locaux, intégrer des transactions postérieures à 2021 et refaire une évaluation chronologique, avec analyse du biais. Ni le total estimé ni les groupes ne suffisent à décider d’un achat, d’une vente ou d’une allocation commerciale.

## 17 — Conclusion

L’analyse produit trois résultats utiles et distincts : une lecture descriptive des prix historiques, une première valorisation du portefeuille et un regroupement exploratoire des opportunités. Je retiens la progression de 10,1% des prix moyens des appartements entre 2017 et 2021, une valeur estimée de 169,70 M€ au 31/12/2022 et deux groupes de prix pour les 40 opportunités. Ces repères s’accompagnent de leurs conditions d’usage : composition non neutralisée, erreur chronologique et extrapolation, absence de labels réels. Transition vers les questions du jury.

## 18 — Sources et reproductibilité

Dépôt de départ : https://github.com/steve57000/p8, branche master, révision f5ac63618ccaa14fe09c7652e4bccfe89be00ab2 (arbre récupéré le 16 novembre 2026). Sources brutes sous data/raw/ dans le paquet corrigé ; l’ancien agencement livrables/data/raw/ est aussi reconnu par le notebook. Échantillon également accessible dans les ressources OpenClassrooms : https://s3.eu-west-1.amazonaws.com/course.oc-static.com/projects/Business+Intelligence+Analyst/BIA_project+8/echantillon_a_classer2.xlsx . Références : documentation scikit-learn pour LinearRegression, KMeans, mean_absolute_percentage_error et silhouette_score ; SciPy pour pearsonr. Les sources SHA-256 sont conservées dans livrables/sources_sha256.csv. Photographie de couverture : Unsplash, identifiant photo-1502602898657-3e91760cbb34, décorative. Textes et graphiques de cette présentation sont éditables ; leurs données sont embarquées dans le PPTX.
