# Projet OpenClassrooms 1591 — Les Plus Beaux Logis de Paris

Analyse des ventes parisiennes de 2017 à 2021, régression linéaire de la valeur foncière,
valorisation du portefeuille au 31 décembre 2022 et classement exploratoire des opportunités de Louise.

## Présentation et notebook révisés le 16 novembre 2026

Le notebook principal reprend les cinq étapes du modèle fourni, avec 32 cellules de code exécutées,
quinze graphiques lisibles, des interprétations et un tableau de couverture des consignes.

- [Notebook principal](livrables/Bell_Steve_1_Notebook_102026.ipynb)
- [Version HTML à télécharger pour une lecture sans Python](livrables/Bell_Steve_1_Notebook_102026.html)
- [Présentation PowerPoint — 18 diapositives](livrables/Bell_Steve_2_presentation_102026.pptx)
- [Présentation PDF](livrables/Bell_Steve_2_presentation_102026.pdf)
- [Valorisation des 275 actifs](livrables/predictions_valorisation_portefeuille_2022-12-31.csv)
- [Classement provisoire des 40 opportunités](livrables/classification_echantillon_louise_102026.csv)
- [Synthèse des segments](livrables/synthese_valorisation_segments.csv)
- [Métriques de régression](livrables/metriques_regression.csv)
- [Comparaison des 20 arrondissements](livrables/comparaison_arrondissements.csv)
- [Notes de soutenance actualisées](livrables/NOTES_SOUTENANCE.md)
- [Graphiques](livrables/figures/)

Les noms des fichiers sont conservés pour maintenir les liens existants ; leur contenu correspond
à la révision de novembre. La présentation a été entièrement recomposée : identité visuelle
vert profond et ivoire, photographie de Paris, neuf graphiques éditables, résultats actualisés
et notes de soutenance dans chacune des 18 diapositives. Le PDF permet de vérifier la mise en page.

La section 1.6 du notebook distingue les trajectoires 2017–2021 et les niveaux de prix en 2021 :
un tableau complet, quatre figures successives de cinq arrondissements sur une échelle commune,
puis un classement des 20 moyennes de 2021 avec les valeurs affichées.
Tous les graphiques utilisent un fond clair explicite, y compris dans PyCharm en thème sombre.
Les légendes ont une police de 12 points et une place réservée hors des courbes.
Les nuages de points et diagnostics auparavant côte à côte sont présentés séparément.

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

Laisser `DOSSIER_PROJET = None` et `DOSSIER_DONNEES = None` pour la détection automatique.
Le notebook fonctionne depuis la racine ou depuis `livrables`, et peut aussi retrouver
le projet lorsque le noyau démarre ailleurs, grâce à l’interpréteur installé dans son `.venv`.
La racine est vérifiée par la présence du notebook. Les variables d’environnement de terminal
ne sont consultées qu’en dernier recours, car elles peuvent être périmées.

Les données sont lues dans `data/raw/` ; l’ancien emplacement `livrables/data/raw/` reste reconnu.
Les CSV et graphiques sont toujours écrits dans le `livrables/` du projet validé.
Le paramètre `DOSSIER_DONNEES` permet de choisir un autre emplacement. Les chemins relatifs
`data/raw` et `../data/raw` sont vérifiés depuis la racine et le dossier du notebook,
puis depuis le dossier de travail du noyau. En cas d’ambiguïté, un chemin absolu est demandé.
Un chemin explicite incomplet affiche les fichiers manquants sans choisir un autre emplacement.
Dans l’éditeur, utiliser « Redémarrer le noyau et exécuter toutes les cellules ».

### PyCharm : le noyau démarre dans `C:\Windows\System32`

Le dossier de travail du noyau n’est pas nécessairement celui du notebook.
L’interpréteur du `.venv` placé dans le projet permet maintenant de retrouver la racine
même dans ce cas. Si aucune piste ne permet de retrouver le projet, une fenêtre Windows
demande de sélectionner **le dossier qui contient `data/` et `livrables/`**.

Si la fenêtre ne s’ouvre pas, est annulée, ou si plusieurs projets sont détectés :

1. Dans PyCharm, clic droit sur le dossier racine du projet → **Copy Path/Reference → Absolute Path**.
2. Coller ce chemin dans la cellule de paramètres, par exemple :

   ```python
   DOSSIER_PROJET = r"C:/MesProjets/p8"  # Remplacer par le chemin copié dans PyCharm.
   DOSSIER_DONNEES = None
   ```

3. Redémarrer le noyau et exécuter toutes les cellules.

Le sélecteur utilise `tkinter`, inclus dans l’installation Python Windows classique.
Sur un serveur ou sans interface graphique, renseigner directement `DOSSIER_PROJET`.
Aucun dossier de sortie n’est créé tant que le projet et les trois sources ne sont pas validés.

Sous Windows, en cas de `WinError 206`, créer l’environnement dans un chemin court :

```powershell
New-Item -ItemType Directory -Force C:\venvs | Out-Null
py -3.12 -m venv C:\venvs\p8
& C:\venvs\p8\Scripts\python.exe -m pip install -r requirements.txt
```

Choisir ensuite `C:\venvs\p8\Scripts\python.exe` dans PyCharm.

## Vérification

La version actuelle a été exécutée intégralement avec `nbclient`, dans un noyau neuf du `.venv`
du projet lancé depuis un dossier extérieur. Un état Matplotlib sombre a été simulé avant
la cellule de préparation : les 32 cellules et quinze figures s’exécutent sans erreur,
et aucun fichier n’est écrit dans le dossier de démarrage extérieur.
Les quatre graphiques d’arrondissements partagent les mêmes limites verticales ; les 20 séries
et les 20 barres du classement sont présentes. La taille des légendes, leur place dans la figure
et l’absence de recouvrement avec les axes ont été contrôlées. Les métriques de régression
et la valorisation n’ont pas changé.

Les démarrages à la racine, dans `livrables`, hors du projet avec son `.venv`, les chemins explicites,
l’ancien agencement, les ambiguïtés et l’annulation du sélecteur sont couverts par 28 tests :

```bash
python -m unittest discover -s tests -v
```

La boîte de dialogue Windows est testée par simulation ; un poste Windows natif n’est pas
disponible dans l’environnement Linux de vérification.
Le notebook exécuté et sa version HTML ont été enregistrés ; le rendu HTML a été inspecté.
Les principaux calculs ont été reproduits indépendamment à partir des trois classeurs.
Le PowerPoint a été ouvert par LibreOffice, exporté en PDF et ses 18 diapositives inspectées.

Les fichiers de départ ont été récupérés directement dans le dépôt
[`steve57000/p8`](https://github.com/steve57000/p8), branche `master`,
révision `f5ac63618ccaa14fe09c7652e4bccfe89be00ab2`. Les classeurs bruts sont inchangés.
La photographie de couverture provient d’Unsplash (identifiant `photo-1502602898657-3e91760cbb34`) ;
elle sert uniquement d’illustration.
