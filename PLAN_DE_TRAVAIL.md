# Projet OC 1591 — plan et état d’avancement

## Fait
- Lecture des consignes fournies et des trois fichiers de référence (historique, portefeuille, modèle de slides) ainsi que du notebook étudiant.
- Étape 1 : profilage et analyses descriptives; prix moyen par année, arrondissement, transaction du 6e, corrélations et comparaison des types.
- Étape 2 : régression linéaire avec one-hot encoding et séparation temporelle manuelle. Apprentissage : 2017–2020 (21,128 lignes); test : 2021 (5,068 lignes). Erreur absolue relative moyenne mesurée : 7.87%.
- Étape 3 : prévision des 275 actifs au 31/12/2022 et export CSV; présentation client synthétique.
- K-means : clustering sur le prix au m², apprentissage 2017–2020; contrôle sur les ventes 2021 (précision locaux 23.3%, rappel 73.6%, exactitude 80.1%).
- Validation externe non terminée : l’échantillon `echantillon_a_classer2.xlsx` et les étiquettes de référence de Louise ne sont pas dans les fichiers disponibles; les fournir pour finaliser la comparaison officielle.

## Points à faire confirmer avec le mentor / le brief
1. Les 16 lignes strictement identiques sont conservées, car le fichier ne fournit pas d’identifiant de vente permettant de trancher.
2. L’algorithme apprend le logarithme du prix au m² puis reconstruit la valeur totale en multipliant par la surface réelle. La version brute sur la valeur totale n’a pas atteint la cible sous 10% avec le split strictement chronologique; la transformation du prix au m² atteint 7.87% sur le test 2021.
3. Le portefeuille n’indique pas de branche/segment d’entreprise : les montants sont présentés par type de bien comme ventilation descriptive.
4. La valorisation du 31/12/2022 est une extrapolation à partir des ventes 2017–2021, et non une estimation expertisée.

## Classification K-means
Le notebook inclut un test de clustering sur les transactions historiques 2021 mises à l’écart. La validation finale de l’échantillon Louise attend le classeur d’opportunités et les étiquettes réelles de l’équipe.

## Exécution
Depuis le dossier extrait : installer `requirements.txt`, démarrer Jupyter depuis la racine `Projet_OC1591`, puis exécuter `livrables/Bell_Steve_1_Notebook_102026.ipynb` du début à la fin. Le CSV présent a été produit par le notebook et contient une ligne par actif.
