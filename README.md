# Projet OpenClassrooms 1591 — Les Plus Beaux Logis de Paris

Ce dépôt contient les analyses du marché parisien, le modèle de valorisation du portefeuille et un premier essai de classement automatique des opportunités.

## Livrables

- `livrables/Bell_Steve_1_Notebook_102026.ipynb` — analyses, régression linéaire, estimation du portefeuille et test K-means.
- `livrables/predictions_valorisation_portefeuille_2022-12-31.csv` — estimation de la valeur de chacun des 275 biens.
- `livrables/classification_echantillon_louise_102026.csv` — résultats provisoires sur les 40 opportunités de l’échantillon.
- `livrables/Bell_Steve_2_presentation_102026.pptx` — support de présentation, 9 diapositives.
- `livrables/NOTES_SOUTENANCE.md` — trame orale et limites à expliquer.
- `livrables/figures/` — graphiques produits par le notebook.

## Données

Les classeurs d’historique et de portefeuille sont dans `data/raw/`. L’échantillon `echantillon_a_classer2.xlsx` provient du [fichier transmis par OpenClassrooms](https://s3.eu-west-1.amazonaws.com/course.oc-static.com/projects/Business+Intelligence+Analyst/BIA_project+8/echantillon_a_classer2.xlsx). Il contient 40 biens, tous situés dans le 19e arrondissement. Le modèle estime actuellement les 40 comme appartements. Le classement de référence de l’équipe de Louise n’est pas fourni : la comparaison officielle reste à effectuer dès réception de ces étiquettes.

## Installation et exécution

Python 3.12 a été utilisé pour vérifier le projet. Dans PyCharm, ouvrir la racine du dépôt et choisir l’interpréteur de l’environnement virtuel créé pour le projet.

Sous Windows, si l’installation des bibliothèques échoue avec `WinError 206`, conserver le dépôt où il est et créer l’environnement dans un chemin court, par exemple `C:\venvs\p8` :

```powershell
New-Item -ItemType Directory -Force C:\venvs | Out-Null
py -3.12 -m venv C:\venvs\p8
& C:\venvs\p8\Scripts\python.exe -m pip install --upgrade pip
& C:\venvs\p8\Scripts\python.exe -m pip install -r requirements.txt
```

Dans PyCharm, sélectionner ensuite `C:\venvs\p8\Scripts\python.exe` comme interpréteur et comme noyau du notebook. Le notebook repère les dossiers `data/raw` et `livrables` depuis la racine du dépôt ou depuis `livrables`.

Pour recalculer tous les résultats depuis la racine :

```powershell
python -m nbconvert --execute --to notebook --inplace livrables/Bell_Steve_1_Notebook_102026.ipynb
```

Les résultats K-means ne doivent pas servir à décider seuls d’un achat. Sur le test historique 2021, le modèle génère beaucoup de fausses alertes « local » et fait moins bien que le classement systématique en appartement en exactitude globale. Les étiquettes de Louise sont nécessaires pour mesurer la performance sur ses opportunités.

La valorisation au 31/12/2022 est une extrapolation pédagogique à partir des ventes 2017–2021. Elle n’est pas une expertise immobilière.
