# Projet OpenClassrooms 1591 — Les Plus Beaux Logis de Paris

Analyse des ventes parisiennes de 2017 à 2021, régression linéaire de la valeur foncière,
valorisation du portefeuille au 31 décembre 2022 et classement exploratoire des opportunités de Louise.

## Présentation et notebook révisés le 16 novembre 2026

Le notebook principal reprend les cinq étapes du modèle fourni, avec 32 cellules de code exécutées,
neuf graphiques, des interprétations et un tableau de couverture des consignes.

- [Notebook principal](livrables/Bell_Steve_1_Notebook_102026.ipynb)
- [Version HTML à télécharger pour une lecture sans Python](livrables/Bell_Steve_1_Notebook_102026.html)
- [Présentation PowerPoint — 18 diapositives](livrables/Bell_Steve_2_presentation_102026.pptx)
- [Présentation PDF](livrables/Bell_Steve_2_presentation_102026.pdf)
- [Valorisation des 275 actifs](livrables/predictions_valorisation_portefeuille_2022-12-31.csv)
- [Classement provisoire des 40 opportunités](livrables/classification_echantillon_louise_102026.csv)
- [Synthèse des segments](livrables/synthese_valorisation_segments.csv)
- [Métriques de régression](livrables/metriques_regression.csv)
- [Notes de soutenance actualisées](livrables/NOTES_SOUTENANCE.md)
- [Graphiques](livrables/figures/)

Les noms des fichiers sont conservés pour maintenir les liens existants ; leur contenu correspond
à la révision de novembre. La présentation a été entièrement recomposée : identité visuelle
vert profond et ivoire, photographie de Paris, neuf graphiques éditables, résultats actualisés
et notes de soutenance dans chacune des 18 diapositives. Le PDF permet de vérifier la mise en page.

## Résultats et limites

| Indicateur | Résultat |
|---|---:|
| Lignes historiques | 26 196 |
| MAPE — test aléatoire de 33 % | 9,14 % |
| MAPE — test chronologique 2021 | 13,62 % |
| Biais relatif moyen — test 2021 | +12,81 % |
| Portefeuille estimé au 31/12/2022 | 169,70 M€ |
| Particuliers, selon la convention de type | 71,22 M€ |
| Corporate, selon la convention de type | 98,48 M€ |
| Groupes K-means sur les 40 opportunités | 20 et 20 biens |
| Silhouette des deux groupes | 0,909 |

La régression prédit directement la valeur foncière totale. Les 16 répétitions exactes sont conservées
pour les statistiques descriptives et retirées de la base de modélisation pour éviter leur présence
dans l’apprentissage et le test. Le modèle final est réentraîné sur 2017–2021.

Les segments sont une convention : appartements = particuliers ; locaux = corporate.
Le fichier ne contient pas de branche commerciale. Les deux lignes répétées du portefeuille sont conservées et à vérifier.
La valorisation 2022 extrapole au-delà de l’historique ; les scores passés ne garantissent pas la précision future.

K-means est ajusté sur le prix au m² des 40 opportunités du 19e arrondissement.
Les groupes sont interprétés provisoirement comme appartements et locaux d’après l’ordre des prix de référence locaux.
Le centre du groupe bas est toutefois 16,1 % sous la moyenne des appartements du 19e en 2021.
Le classeur ne contient ni date ni type réel : la silhouette ne mesure pas l’exactitude du classement.
La section 4.5 attend les labels réels de Louise pour calculer les métriques de classification.

## Données

Les trois classeurs sont dans `data/raw/`, sans modification des sources :

- `historique_immobilier_paris_2017_2021.xlsx`
- `portefeuille_actifs.xlsx`
- `echantillon_a_classer2.xlsx`

L’échantillon provient des [ressources OpenClassrooms](https://s3.eu-west-1.amazonaws.com/course.oc-static.com/projects/Business+Intelligence+Analyst/BIA_project+8/echantillon_a_classer2.xlsx).
Les empreintes des sources et les versions des bibliothèques sont enregistrées dans `livrables/sources_sha256.csv`
et `livrables/environnement.json`.

Conserver cette arborescence après extraction du ZIP :

```text
p8_corrige/
  data/
    raw/                 # Les trois classeurs Excel
  livrables/
    Bell_Steve_1_Notebook_102026.ipynb
    Bell_Steve_1_Notebook_102026.html
    Bell_Steve_2_presentation_102026.pptx
    Bell_Steve_2_presentation_102026.pdf
    figures/             # Graphiques du notebook
    ...                  # CSV, versions, notes de soutenance
  requirements.txt
  README.md
```

## Installation et exécution

Python 3.12 a été utilisé pour vérifier le projet. Ouvrir la racine du dépôt dans PyCharm,
puis sélectionner l’environnement Python du projet comme interpréteur et noyau du notebook.

```powershell
python -m pip install -r requirements.txt
python -m nbconvert --execute --to notebook --inplace livrables/Bell_Steve_1_Notebook_102026.ipynb
```

Le notebook fonctionne depuis la racine ou depuis `livrables`. Laisser `DOSSIER_DONNEES = None`
pour qu’il retrouve automatiquement `data/raw/`. L’ancien emplacement `livrables/data/raw/`
reste reconnu. Les CSV et graphiques sont toujours écrits dans `livrables/`, sans créer
de dossier `livrables/livrables/`. Le paramètre `DOSSIER_DONNEES` permet de choisir un autre
emplacement ; un chemin relatif est interprété depuis le dossier de travail du noyau.
Un chemin explicite incomplet affiche les fichiers manquants et ne choisit pas silencieusement
un autre emplacement.
Dans l’éditeur, utiliser « Redémarrer le noyau et exécuter toutes les cellules ».

Sous Windows, en cas de `WinError 206`, créer l’environnement dans un chemin court :

```powershell
New-Item -ItemType Directory -Force C:\venvs | Out-Null
py -3.12 -m venv C:\venvs\p8
& C:\venvs\p8\Scripts\python.exe -m pip install -r requirements.txt
```

Choisir ensuite `C:\venvs\p8\Scripts\python.exe` dans PyCharm.

## Vérification

Les 32 cellules ont été exécutées intégralement deux fois avec `nbclient`, dans des noyaux
Jupyter neufs : depuis la racine, puis depuis `livrables`, avec `data/raw` à la racine.
Les deux exécutions ont réussi, avec neuf figures et aucune erreur. La détection de l’ancien
agencement et les messages d’erreur pour un chemin explicite incorrect ont aussi été vérifiés.
Le notebook exécuté et sa version HTML ont été enregistrés ; le rendu HTML a été inspecté.
Les principaux calculs ont été reproduits indépendamment à partir des trois classeurs.
Le PowerPoint a été ouvert par LibreOffice, exporté en PDF et ses 18 diapositives inspectées.

Les fichiers de départ ont été récupérés directement dans le dépôt
[`steve57000/p8`](https://github.com/steve57000/p8), branche `master`,
révision `f5ac63618ccaa14fe09c7652e4bccfe89be00ab2`. Les classeurs bruts sont inchangés.
La photographie de couverture provient d’Unsplash (identifiant `photo-1502602898657-3e91760cbb34`) ;
elle sert uniquement d’illustration.
