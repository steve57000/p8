# Projet OpenClassrooms 1591 — état et points à terminer

## Travail réalisé et vérifié

- Profilage des données historiques : 26 196 lignes, deux types de biens, aucune valeur manquante, période du 02/01/2017 au 31/12/2021. Seize lignes sont entièrement identiques; elles sont conservées faute d’identifiant de transaction.
- Analyses du marché : évolution du prix moyen au m² des appartements, comparaison par arrondissement, détail des mutations du 6e arrondissement, corrélations prix/date et prix/surface, comparaison appartements/locaux.
- Régression linéaire évaluée avec une séparation manuelle chronologique : apprentissage 2017–2020 (21 128 lignes), test 2021 (5 068 lignes). L’erreur absolue relative moyenne du prix total est de 7,87 %; le biais moyen est de +7,86 %, donc les prédictions surestiment en moyenne les valeurs du test.
- Valorisation estimée au 31/12/2022 et export des 275 biens dans `livrables/predictions_valorisation_portefeuille_2022-12-31.csv`.
- Échantillon OpenClassrooms de 40 opportunités ajouté dans `data/raw/echantillon_a_classer2.xlsx`; le notebook produit leur classement K-means dans un CSV.
- Support de présentation de 9 diapositives, dans le modèle fourni et sous la limite de 20 diapositives.

## Résultats K-means et limites

- K-means est ajusté sur le prix au m² des transactions 2017–2020; les libellés des transactions d’apprentissage servent uniquement à donner un nom interprétable aux deux groupes.
- Sur les ventes tenues à l’écart en 2021 : précision « local » 23,3 %, rappel 73,6 %, exactitude globale 80,1 %. Un classement systématique en appartement atteint 92,6 % d’exactitude sur ce jeu déséquilibré. Ce K-means n’est donc pas assez fiable pour automatiser une décision d’achat.
- Les 40 opportunités de l’échantillon sont dans le 19e arrondissement et sont toutes estimées « appartement ». Ce résultat est provisoire et n’est pas validé par une étiquette de référence.

## À obtenir pour terminer la validation officielle

Récupérer auprès de l’équipe de Louise les étiquettes réelles correspondant aux 40 biens, puis comparer ces étiquettes aux résultats K-means dans le notebook et mettre à jour la présentation. Sans ce fichier, la précision de classement sur les opportunités réelles ne peut pas être calculée.

## Hypothèses à signaler

1. Les lignes historiques sont comptées comme transactions; les 16 lignes identiques ne peuvent pas être distinguées sans identifiant dédié.
2. Le modèle prédit le logarithme du prix au m², puis reconstruit la valeur totale par multiplication par la surface réelle.
3. Le test sur 2021 est rétrospectif. Le biais moyen positif doit être mentionné; le résultat ne garantit pas la précision sur le portefeuille en 2022.
4. La valorisation du portefeuille est ventilée par type de bien, faute de colonne de branche dans le fichier.
5. Les fichiers ne décrivent pas l’état, l’étage, le DPE ni la nature détaillée des locaux.

## Exécution

Depuis la racine du dépôt, installer les dépendances de `requirements.txt`, puis exécuter `livrables/Bell_Steve_1_Notebook_102026.ipynb`. Le notebook sait résoudre ses chemins depuis la racine du dépôt ou depuis le dossier `livrables`.
