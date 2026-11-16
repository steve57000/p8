# Projet OpenClassrooms 1591 — état au 16 novembre 2026

## Révision du notebook terminée

- Les cinq étapes du modèle fourni sont complétées et organisées ; neuf graphiques sont présents.
- Profil historique : 26 196 lignes, deux types de biens, aucune valeur manquante ; période du 02/01/2017 au 31/12/2021.
- Les 16 répétitions exactes sont conservées dans la description et exclues de la base de modélisation.
- Pearson prix au m²/date porte sur les 709 appartements du 6e arrondissement : r = 0,904.
- La relation valeur foncière/surface est distinguée de la relation prix au m²/surface.
- La régression prédit directement la valeur foncière et respecte le test de 33 % demandé : MAPE 9,14 %.
- Un contrôle chronologique apprend sur 2017–2020 et teste 2021 : MAPE 13,62 %, biais relatif moyen +12,81 %.
- Le modèle final est réentraîné sur l’ensemble de l’historique distinct 2017–2021.
- Les 275 actifs sont estimés au 31/12/2022 avec leur surface réelle bâtie : 169,70 M€ au total.
- Sous la convention appartements = particuliers et locaux = corporate, les valorisations sont 71,22 M€ et 98,48 M€.
- K-means est ajusté sur les 40 opportunités de Louise, avec le seul prix au m² : deux groupes de 20 biens, silhouette 0,909.
- Les CSV, figures, notes de soutenance et README sont synchronisés avec ces résultats.

## Validation réalisée

Les 32 cellules de code ont été exécutées dans l’ordre sous IPython sans erreur.
Le format du notebook, les totaux, les exports, les graphiques et les principaux calculs ont été contrôlés.
Les fichiers sources restent inchangés.

## Points restant à confirmer

1. Obtenir les types réels de Louise et les dates des 40 opportunités. Sans labels réels,
   l’exactitude du classement ne peut pas être mesurée. La section 4.5 est prête à les recevoir.
2. Expliquer le décalage du groupe de prix bas, dont le centre est 16,1 % sous la moyenne
   historique des appartements du 19e arrondissement en 2021.
3. Confirmer les segments de l’entreprise et vérifier les deux répétitions exactes du portefeuille.
4. Actualiser le PowerPoint d’octobre avant la soutenance : il contient encore les anciens résultats.

## Limites à présenter

- Comptage de lignes sans identifiant de mutation ; corrélations descriptives, sans interprétation causale.
- Prévision 2022 au-delà de l’historique, avec un biais déjà observé au test chronologique.
- Absence d’état du bien, d’étage, de DPE et de nature détaillée des locaux.
- Les numéros des clusters ne sont pas des types de biens. Les labels proposés sont des hypothèses.
- La silhouette décrit la séparation des groupes ; elle ne mesure pas leur justesse métier.

## Exécution

Depuis la racine, installer `requirements.txt`, puis exécuter toutes les cellules de
`livrables/Bell_Steve_1_Notebook_102026.ipynb`. Les exports sont écrits dans `livrables/`.
