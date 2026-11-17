# Comprendre votre notebook P8, pas à pas

Guide pédagogique du 17 novembre 2026 — Steve Bell.
Notebook de référence : `Bell_Steve_1_Notebook_102026.ipynb`, commit `af488358e791cddcb36e55713c9d54b4d59e80b6`.
Empreinte SHA-256 : `3da24e6c6523b84e67f8937de13a9d8217fa5e8dfb885f80bec5873411d879f4`.

C01–C32 désignent l’ordre des cellules de code après redémarrage et exécution complète ; les compteurs In[] peuvent varier si une cellule est rejouée.
Le PDF contient un sommaire cliquable et des signets. Les fiches ci-dessous couvrent chaque point du notebook.

## Correspondance avec le modèle officiel OpenClassrooms

- Étape 1 — Analyse des données : §1.1 à §1.10 · C03 à C15.
- Étape 2 — Entraînement de l’algorithme : §2.1 à §2.5 · C16 à C20.
- Étape 3 — Prédiction définitive pour le client : §3.1 à §3.3 · C21 à C23.
- Étape 4 — Classification des données issues du jeu de test : §4.1 à §4.5 · C24 à C29.
- Étape 5 — Analyse et présentation des résultats : §5.1 à §5.5 · C30 à C32.

Le jalon 4 utilise le fichier distinct des 40 opportunités, pas X_test de la régression. Le test chronologique §2.5 et la validation conditionnelle §4.5 sont des compléments méthodologiques.
La page détaillée actuelle n’a pas pu être consultée ; la correspondance est vérifiée sur le gabarit officiel accessible, daté du 8 mars 2023.

## P.1 — Préparer les outils, les paramètres et un affichage lisible

Repères : C01.

### Objectif

Comprendre ce qui est chargé une fois, ce qui règle le calcul et ce qui règle seulement son apparence.

### Code à repérer

```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib.dates as mdates
```

```python
GRAINE = 42
PART_TEST = 0.33
DATE_ORIGINE = pd.Timestamp('2017-01-01')
DATE_ESTIMATION = pd.Timestamp('2022-12-31')
ANNEE_ECHANTILLON = 2021  # Indication du sujet, non vérifiable dans le classeur.
DOSSIER_PROJET = None  # Si nécessaire : r'C:/chemin/absolu/vers/le/projet'
DOSSIER_DONNEES = None  # Laisser None pour utiliser data/raw dans le projet détecté.
```

```python
LIBELLES_TYPES = {2: 'Appartement', 4: 'Local industriel. commercial ou assimilé'}
SEGMENTS = {2: 'Particuliers', 4: 'Corporate'}
BLEU, ORANGE, GRIS = '#245C8A', '#BC6C25', '#56616E'
```

```python
plt.style.use('default')
plt.rcParams.update({
    'figure.figsize': (9.2, 4.9), 'figure.dpi': 100, 'font.size': 12,
    'figure.facecolor': 'white', 'axes.facecolor': 'white',
    'savefig.facecolor': 'white', 'savefig.transparent': False,
    'text.color': '#223344', 'axes.labelcolor': '#223344',
    'xtick.color': '#223344', 'ytick.color': '#223344',
    'legend.fontsize': 12, 'legend.facecolor': 'white', 'legend.edgecolor': '#CFD8E1',
```

### Lecture pas à pas

Une bibliothèque rassemble des outils déjà écrits. « import pandas as pd » charge pandas sous le nom court pd ; « pd.read_excel(...) » désigne ensuite sa fonction de lecture Excel. NumPy sert aux calculs numériques, pandas aux tableaux, Matplotlib aux figures, SciPy aux corrélations et scikit-learn aux modèles et à leurs mesures. L’annexe inventorie chaque import réel du notebook, y compris les imports conditionnels.

GRAINE = 42 fixe le tirage pseudo-aléatoire demandé par certaines fonctions. Réutiliser la même graine aide à reproduire le découpage des données et K-means dans le même environnement ; cela ne prouve ni la qualité du modèle ni sa stabilité sous d’autres échantillons. PART_TEST = 0.33 réserve environ 33 % des observations au test aléatoire.

pd.Timestamp crée une date exploitable pour les calculs. DATE_ORIGINE sert à exprimer les dates historiques en années depuis le 1er janvier 2017 ; DATE_ESTIMATION fixe le 31 décembre 2022 pour le portefeuille. ANNEE_ECHANTILLON = 2021 est une indication du sujet, pas une date vérifiée dans le fichier de Louise : le classeur ne fournit aucune date.

DOSSIER_PROJET et DOSSIER_DONNEES valent None par défaut. None est une absence de valeur volontaire : le code cherchera le projet et ses données. Ce n’est ni le texte « None », ni une chaîne vide, ni zéro. La fiche P.3 explique quand renseigner un chemin absolu.

LIBELLES_TYPES et SEGMENTS sont des dictionnaires : chaque clé donne accès à une valeur. Les codes 2 et 4 nomment les deux types présents. La correspondance appartement → particuliers et local → corporate est une convention analytique ; ces mots ne prouvent pas l’existence de branches commerciales dans le fichier.

plt.style.use et plt.rcParams.update règlent une fois le fond blanc, les couleurs, la taille des caractères et les marges des figures. Les pd.set_option règlent l’affichage des tableaux. Ces réglages rendent les sorties plus lisibles, y compris dans PyCharm en thème sombre ; ils ne changent ni les prix ni les résultats des calculs.

La cellule définit aussi les fonctions de présentation étudiées en P.2. Définir une fonction ne l’exécute pas : sa logique sera appelée plus loin. Ainsi, terminer_figure peut être définie avant DOSSIER_FIGURES, à condition que ce dossier soit défini par C02 avant le premier appel.

### Fonctions et méthodes

- `import … as … / from … import …` : Charger une bibliothèque ou un outil précis et, éventuellement, lui donner un alias court.
- `pd.Timestamp` : Construire une date structurée pour les différences de dates et la valorisation.
- `plt.style.use / plt.rcParams.update` : Appliquer des réglages communs à toutes les figures Matplotlib suivantes.
- `pd.set_option` : Régler la présentation des tableaux pandas sans transformer les données de calcul.

### Résultat attendu

Les bibliothèques sont disponibles, les paramètres sont mémorisés et les fonctions d’affichage sont définies. Cette cellule seule ne lit aucun classeur et n’entraîne aucun modèle.

### À retenir

- Séparer trois choses : les données, les paramètres du calcul et les règles d’affichage. Modifier une couleur n’a pas le même effet que modifier PART_TEST ou DATE_ESTIMATION.

### Vérifier par vous-même

- [ ] Exécuter C01 en premier avec le noyau Python du projet. En cas de ModuleNotFoundError, installer les dépendances dans cet environnement, puis redémarrer le noyau ; installer un paquet dans un autre Python ne corrige pas ce noyau.

### Question minute

Pourquoi le code contient-il à la fois 0.33 et des pourcentages affichés comme 33 % ?

## P.2 — Lire les fonctions qui présentent nombres, tableaux et figures

Repères : C01.

### Objectif

Reconnaître l’entrée, l’action et le résultat d’une fonction, tout en distinguant la valeur numérique de son texte affiché.

### Code à repérer

```python
def fr(nombre, decimales=0):
    return f'{nombre:,.{decimales}f}'.replace(',', ' ').replace('.', ',')
```

```python
def afficher_p(p):
    # Une p-value arrondie à zéro n'est pas une probabilité strictement nulle.
    return '< 10⁻¹⁶' if p < 1e-16 else f'{p:.3g}'
```

```python
    formats_auto = {}
    # Figer la précision par colonne dans chaque fonction de formatage.
    for colonne in tableau.select_dtypes(include='number').columns:
        precision = 0 if pd.api.types.is_integer_dtype(tableau[colonne]) else 2
        formats_auto[colonne] = lambda valeur, p=precision: fr(valeur, p)
    formats_auto.update(formats or {})
    style = tableau.style.format(formats_auto, na_rep='—').set_caption(titre)
    style = style.set_table_styles([
```

```python
    legende = fig.legend(
        handles, labels, loc='outside lower center', ncol=ncol,
        fontsize=12, frameon=True, framealpha=1,
        facecolor='white', edgecolor='#CFD8E1',
        labelcolor='#223344', borderpad=.7, labelspacing=.6,
        columnspacing=1.5, handlelength=2.2,
```

```python
    fig.savefig(DOSSIER_FIGURES / f'{nom}.png', dpi=150,
                facecolor='white', transparent=False, bbox_inches='tight')
    plt.show()
    plt.close(fig)
```

```python
def libelle_arrondissement(code_postal):
    numero = int(code_postal) - 75000
    ordinal = '1er' if numero == 1 else f'{numero}e'
    return f'{ordinal} ({code_postal})'
```

### Lecture pas à pas

def introduit une fonction personnelle. Les noms entre parenthèses sont ses paramètres ; l’appel lui transmet des arguments. Avec fr(nombre, decimales=0), le nombre de décimales vaut zéro si l’appelant ne précise rien. return renvoie une valeur réutilisable ; une fonction sans return explicite renvoie None, même si elle affiche ou enregistre quelque chose.

fr construit une chaîne de caractères au format français. La f-string choisit le nombre de décimales ; les deux replace transforment le séparateur de milliers en espace et le point décimal en virgule. La valeur d’origine n’est pas arrondie dans le DataFrame par cette fonction : seul le texte retourné l’est. Un texte comme « 10 455,60 » ne doit pas remplacer la colonne numérique utilisée pour les calculs.

afficher_p prépare la p-value d’un test statistique. Une p-value inférieure à 10⁻¹⁶ est écrite « < 10⁻¹⁶ » plutôt que zéro ; sinon, le format .3g conserve trois chiffres significatifs. Cette fonction met en forme un résultat statistique : elle ne calcule pas le test et n’établit pas à elle seule une importance pratique ou une causalité.

afficher_tableau prend un DataFrame, un titre et éventuellement des formats particuliers. select_dtypes repère ses colonnes numériques ; les entiers sont affichés sans décimales, les autres avec deux. Le Styler produit une présentation HTML, un titre et des styles ; display l’affiche. Les données numériques restent disponibles dans leur tableau initial. formats permet par exemple de demander trois décimales pour un R².

Dans « lambda valeur, p=precision: fr(valeur, p) », la petite fonction sert à formater chaque valeur. p=precision mémorise la précision propre à la colonne au moment où cette fonction est créée. Sans cette précaution, les fonctions créées dans la boucle pourraient toutes employer la dernière précision rencontrée.

legende_figure rassemble les éléments de légende de tous les axes de la figure. Elle supprime les libellés répétés, place une seule légende en dessous du graphique et rend ses marqueurs opaques. Les points du nuage peuvent rester transparents dans les données : l’échantillon de la légende demeure lisible. Le résultat renvoyé est l’objet Legend, pas une nouvelle série statistique.

terminer_figure impose le fond blanc et des étiquettes foncées, enregistre un PNG à 150 dpi dans DOSSIER_FIGURES, affiche la figure, puis ferme son objet Matplotlib. L’ordre compte : sauvegarder avant de fermer évite de perdre le rendu ; fermer après l’affichage libère les ressources pour les figures suivantes.

libelle_arrondissement transforme un code postal parisien en libellé de lecture : int convertit d’abord le code, puis le calcul retire 75000. Le premier arrondissement s’écrit « 1er » et les suivants « 2e », « 3e », etc. format_euros est enfin un objet FuncFormatter qui appelle fr pour chaque graduation d’axe ; son paramètre pos est fourni par Matplotlib même si le calcul ne l’utilise pas.

### Fonctions et méthodes

- `fr(nombre, decimales=0)` : Renvoyer un texte numérique français ; ne pas transformer la donnée de calcul.
- `afficher_p(p)` : Renvoyer le texte d’une p-value, en évitant de présenter une très petite valeur comme zéro.
- `afficher_tableau(tableau, titre, formats=None, masquer_index=False)` : Afficher un tableau HTML lisible ; masquer l’index seulement si le paramètre le demande.
- `legende_figure(fig, ncol=2)` : Renvoyer une légende commune, sans doublons de libellés, sous la figure.
- `terminer_figure(fig, nom)` : Enregistrer, afficher puis fermer une figure dans cet ordre.
- `libelle_arrondissement(code_postal)` : Renvoyer un nom de lecture pour un code postal parisien déjà contrôlé.
- `mtick.FuncFormatter` : Adapter la fonction de formatage aux graduations d’un axe Matplotlib.

### Résultat attendu

Les tableaux et graphiques suivants utilisent les mêmes conventions de lecture : fond clair, nombres français, légendes séparées des données et fichiers PNG conservés.

### À retenir

- Une fonction peut renvoyer une valeur, produire un effet visible, ou faire les deux. fr renvoie un texte ; afficher_tableau affiche un objet ; terminer_figure enregistre un fichier et affiche une figure.

### Vérifier par vous-même

- [ ] Contrôler le titre, l’unité, les libellés, la précision et les légendes à taille de lecture. C02 doit avoir défini DOSSIER_FIGURES avant le premier appel à terminer_figure. Un beau tableau ne dispense pas de vérifier ses calculs.

### Question minute

Peut-on remplacer une colonne de prix par les textes produits par fr pour rendre tous les calculs plus lisibles ?

## P.3 — Retrouver le projet quand PyCharm démarre le noyau dans System32

Repères : C01 · C02.

### Objectif

Comprendre pourquoi le dossier de travail n’est pas nécessairement le dossier du notebook, et vérifier les chemins avant d’écrire un résultat.

### Code à repérer

```python
DEPART = Path.cwd().resolve()
NOM_NOTEBOOK = 'Bell_Steve_1_Notebook_102026.ipynb'
```

```python
def _racine_depuis(ancrage):
    """Reconnaître le projet par son notebook, jamais par un simple nom de dossier."""
    dossier = Path(ancrage).expanduser().resolve()
    for parent in (dossier, *dossier.parents):
        if (parent / 'livrables' / NOM_NOTEBOOK).is_file():
            return parent
        if (parent / NOM_NOTEBOOK).is_file():
            return parent.parent if parent.name == 'livrables' else parent
```

```python
if DOSSIER_PROJET is not None:
    projet_explicite = Path(DOSSIER_PROJET).expanduser()
    if not projet_explicite.is_absolute():
        raise ValueError('DOSSIER_PROJET doit être un chemin absolu, copié depuis PyCharm.')
    RACINE = _racine_depuis(projet_explicite) if projet_explicite.is_dir() else None
    if RACINE is None:
```

```python
    ancrages = [DEPART, Path(sys.prefix), Path(sys.executable).parent]
    if donnees_explicites is not None and donnees_explicites.is_absolute():
        ancrages.append(donnees_explicites)
    racines = list(dict.fromkeys(racine for ancrage in ancrages
                                if (racine := _racine_depuis(ancrage)) is not None))
```

```python
    candidats = [base / donnees_explicites for base in (RACINE, RACINE / 'livrables', DEPART)]
candidats = list(dict.fromkeys(d.resolve() for d in candidats))
complets = [d for d in candidats if not _manquants(d)]
if donnees_explicites is not None and len(complets) > 1:
    raise ValueError('DOSSIER_DONNEES relatif est ambigu : indiquez un chemin absolu parmi ' + ', '.join(map(str, complets)))
DATA_DIR = complets[0] if complets else None
```

```python
DOSSIER_RESULTATS = RACINE / 'livrables'
DOSSIER_FIGURES = DOSSIER_RESULTATS / 'figures'
DOSSIER_FIGURES.mkdir(parents=True, exist_ok=True)
print(f'Dossier de travail du noyau : {DEPART}')
```

### Lecture pas à pas

Le fichier .ipynb, le projet ouvert dans PyCharm et le dossier courant du noyau sont trois éléments différents. Path.cwd() demande le dossier courant du processus Python ; il peut renvoyer C:\Windows\System32 même si le notebook est affiché dans livrables. Le nom System32 ne doit donc jamais être utilisé comme preuve de la racine du projet.

Path représente un chemin. L’opérateur / lui ajoute un élément sans concaténer manuellement des antislashs. expanduser interprète le raccourci ~ de l’utilisateur ; resolve normalise le chemin et le rend absolu. Aucun de ces appels ne prouve à lui seul que les trois classeurs existent : is_file réalise ce contrôle.

_racine_depuis part d’un indice et remonte seulement ses dossiers parents. Elle confirme le projet par la présence du notebook connu, soit sous livrables, soit à l’emplacement vérifié directement. Le code ne parcourt pas tout le disque et ne prend pas n’importe quel dossier nommé .venv pour le projet.

Le choix explicite du projet est prioritaire : si DOSSIER_PROJET n’est pas None, son chemin doit être absolu et permettre de reconnaître le notebook. Un chemin explicite incorrect arrête le traitement ; le code ne le remplace pas silencieusement par un autre projet. Dans PyCharm, copier le chemin absolu du dossier qui contient data et livrables, puis le renseigner sous la forme r'C:/chemin/vers/le/projet'. Le préfixe r évite d’interpréter les antislashs comme des séquences spéciales dans une chaîne Windows.

Sans projet explicite, le code vérifie le dossier courant, sys.prefix (le dossier de l’environnement Python), le parent de sys.executable (l’exécutable du noyau) et, si elle est absolue, la localisation donnée dans DOSSIER_DONNEES. Un .venv situé dans le projet peut ainsi fournir la bonne piste lorsque le noyau démarre dans System32. Toutes les pistes doivent être confirmées par le marqueur du notebook ; si plusieurs projets distincts sont reconnus, une erreur demande de choisir DOSSIER_PROJET.

Les variables VIRTUAL_ENV et CONDA_PREFIX ne servent de recours que si les indices du noyau réel n’ont reconnu aucune racine. Elles peuvent provenir d’un ancien terminal. Si aucune piste ne suffit, Windows peut ouvrir un sélecteur de dossier grâce à Tkinter. Annuler, ne pas disposer de Tkinter ou ne pas reconnaître le dossier choisi mène à une instruction pour donner le chemin absolu ; les exports ne sont pas créés dans System32.

Après le projet, les sources sont contrôlées. DOSSIER_DONNEES = None cherche d’abord <projet>/data/raw, puis l’ancien <projet>/livrables/data/raw. Un DOSSIER_DONNEES absolu est strict : s’il manque un classeur, le code l’indique et ne prend pas un autre dossier. Ce contrôle d’un chemin absolu incorrect intervient même avant la recherche automatique de racine.

Pour un chemin relatif explicite, le code essaie des interprétations depuis la racine du projet, depuis son dossier livrables et depuis le dossier courant. Cela accepte notamment data/raw et ../data/raw lorsque le projet est reconnu grâce au noyau. Les candidats identiques sont dédupliqués. Plusieurs candidats complets pour le même chemin relatif provoquent une erreur d’ambiguïté : un chemin absolu est alors nécessaire.

Les trois noms de fichiers viennent du dictionnaire FICHIERS. _manquants renvoie la liste des noms absents ; un dossier n’est complet que lorsque cette liste est vide. Après validation de la racine et des sources, DOSSIER_RESULTATS est fixé à <projet>/livrables et DOSSIER_FIGURES à son sous-dossier figures. mkdir(parents=True, exist_ok=True) crée les répertoires nécessaires sans erreur s’ils existent déjà.

Les quatre lignes imprimées sont le diagnostic à lire : dossier courant du noyau, racine du projet, dossier des trois sources, dossier des exports. Les deux derniers doivent pointer vers le projet voulu. Après changement de paramètre ou mise à jour du notebook, redémarrer le noyau puis exécuter toutes les cellules dans l’ordre évite de conserver d’anciens chemins en mémoire.

### Fonctions et méthodes

- `_racine_depuis(ancrage)` : Renvoyer une racine reconnue par le notebook ou None ; remonter des parents sans recherche globale du disque.
- `_choisir_projet_windows()` : Demander en dernier recours un dossier sur Windows ; renvoyer None en cas d’annulation ou d’indisponibilité.
- `_manquants(dossier)` : Renvoyer les noms des classeurs requis qui ne sont pas des fichiers dans ce dossier.
- `verifier_colonnes(df, colonnes, nom)` : Arrêter plus loin la lecture d’un tableau s’il ne contient pas les colonnes attendues.
- `Path.cwd / Path.resolve / Path.is_file` : Lire le dossier courant, normaliser un chemin et vérifier un fichier ; ces rôles sont différents.
- `Path.mkdir` : Créer le dossier d’export seulement après les validations de la racine et des sources.

### Résultat attendu

RACINE, DATA_DIR, DOSSIER_RESULTATS et DOSSIER_FIGURES désignent des emplacements vérifiés et distincts. Une détection impossible ou ambiguë produit un message explicite avant la création des exports.

### À retenir

- Le notebook n’a pas à être déplacé dans data/raw. L’arborescence attendue est un dossier de projet contenant data/raw et livrables côte à côte ; le dossier courant du noyau peut être ailleurs.

### Vérifier par vous-même

- [ ] Les trois classeurs doivent être présents avec leurs noms exacts. Vérifier le noyau .venv du projet dans PyCharm et lire les chemins imprimés. En cas de recours manuel, renseigner un DOSSIER_PROJET absolu copié depuis le projet et laisser DOSSIER_DONNEES à None, puis relancer toutes les cellules.

### Question minute

Pourquoi remplacer automatiquement System32 par son dossier parent ne résoudrait-il pas le problème ?

## 1.1 — Importer l’historique et donner un sens aux colonnes

Repères : C03.

### Objectif

Passer du classeur Excel à un tableau Python dont les dates, montants et surfaces peuvent être utilisés dans des calculs fiables.

### Code à repérer

```python
historique_brut = pd.read_excel(DATA_DIR / FICHIERS['historique'], engine='openpyxl')
verifier_colonnes(historique_brut, [
    'date_mutation', 'valeur_fonciere', 'surface_reelle',
    'code_postal', 'code_type_local', 'type_local',
], 'Historique')
historique = historique_brut.copy()
```

```python
historique['date_mutation'] = pd.to_datetime(historique['date_mutation'], errors='coerce')
for colonne in ['valeur_fonciere', 'surface_reelle', 'code_postal', 'code_type_local']:
    historique[colonne] = pd.to_numeric(historique[colonne], errors='coerce')
```

### Lecture pas à pas

Une variable est un nom qui permet de retrouver un objet en mémoire. Ici, historique_brut désigne un DataFrame pandas : un tableau avec des lignes, des colonnes nommées et un index de lignes. La lecture Excel vient en premier, car aucun contrôle ou calcul ne peut encore utiliser des données qui ne sont pas chargées.

DATA_DIR / FICHIERS['historique'] assemble le dossier des sources et le nom du classeur. Le caractère / sert ici à construire un chemin avec Path ; ce n’est pas une division. Le moteur openpyxl lit le format .xlsx. verifier_colonnes contrôle ensuite la présence des six colonnes indispensables avant de continuer.

La copie historique = historique_brut.copy() sépare le travail de préparation de la version lue. Les conversions modifient historique et laissent historique_brut disponible pour comparer les types initiaux ou compter les répétitions exactes sur les données d’origine.

Une date lue comme simple texte ne permet pas encore d’extraire facilement une année. pd.to_datetime la transforme en date exploitable. La boucle for applique ensuite pd.to_numeric à chaque colonne numérique. errors='coerce' transforme les valeurs impossibles à convertir en valeurs manquantes : cela les rend repérables par le contrôle qualité suivant, sans les inventer ni les supprimer.

Le tableau profil compare les types avant et après conversion et compte les valeurs manquantes. historique.head(5) affiche seulement cinq lignes pour vérifier la lecture. Cet aperçu n’est ni un échantillon aléatoire, ni une preuve que les 26 196 lignes sont toutes correctes ; les contrôles complets viennent après.

### Fonctions et méthodes

- `pd.read_excel` : Charge le classeur dans un DataFrame ; engine précise le lecteur Excel.
- `verifier_colonnes` : Fonction définie dans la préparation : bloque le travail si une colonne nécessaire manque.
- `.copy()` : Crée le tableau de travail sans modifier la copie brute.
- `pd.to_datetime / pd.to_numeric` : Convertissent les dates et les nombres ; coerce rend une conversion impossible visible comme valeur manquante.
- `.dtypes / .isna().sum() / .head(5)` : Décrivent les types, comptent les absences par colonne et montrent un petit aperçu.

### Résultat attendu

Un historique de 26 196 lignes est chargé. Les dates et colonnes numériques sont converties ; le profil de cette version ne révèle aucune valeur manquante après conversion.

### À retenir

- Lire le fichier, vérifier ses colonnes, créer une copie, puis convertir les types : cet ordre évite de calculer sur un tableau mal interprété.
- coerce signale une valeur problématique ; il ne signifie pas que cette valeur a été corrigée.
- La valeur foncière est un montant total en euros ; la surface est une quantité en m². Le prix au m² sera calculé en 1.4.

### Vérifier par vous-même

- [ ] Le chemin affiché dans la cellule de localisation pointe vers les trois bons classeurs.
- [ ] Les colonnes demandées existent et le profil ne contient pas d’absences inattendues.
- [ ] Les dates sont bien de type date et les montants ne restent pas du texte.

### Question minute

Pourquoi ne pas convertir directement historique_brut et l’utiliser pour tout le projet ?

## Qualité — Contrôler avant d’analyser : anomalies et répétitions exactes

Repères : C04.

### Objectif

Vérifier que les données respectent les règles du projet et traiter les répétitions selon l’usage descriptif ou prédictif.

### Code à repérer

```python
controles_historique = pd.Series({
    'Valeurs manquantes après conversion': int(historique.isna().sum().sum()),
    'Valeurs numériques non finies': int((~np.isfinite(historique[colonnes_numeriques])).sum().sum()),
    'Prix nuls ou négatifs': int(historique['valeur_fonciere'].le(0).sum()),
    'Surfaces nulles ou négatives': int(historique['surface_reelle'].le(0).sum()),
    'Dates hors 2017–2021': int((~historique['date_mutation'].between('2017-01-01', '2021-12-31')).sum()),
    'Codes postaux hors Paris 1 à 20': int((~historique['code_postal'].isin(range(75001, 75021))).sum()),
```

```python
display(controles_historique.to_frame())
if controles_historique.gt(0).any():
    raise ValueError('Le fichier historique contient des anomalies à examiner avant de poursuivre.')

nb_identiques_historique = int(historique_brut.duplicated().sum())
historique['code_postal'] = historique['code_postal'].astype(int).astype(str)
historique['code_type_local'] = historique['code_type_local'].astype(int)
```

### Lecture pas à pas

Un calcul peut s’exécuter sans erreur Python tout en donnant un résultat faux. Un prix négatif, une surface nulle ou un code postal hors Paris doivent donc être repérés avant les moyennes, les divisions et l’apprentissage. La cellule rassemble ces règles dans une Series de compteurs.

Une condition comme historique['surface_reelle'].le(0) produit une valeur vraie ou fausse pour chaque ligne. sum() compte les valeurs vraies. Le signe ~ inverse une condition : les dates qui ne sont pas entre 2017 et 2021 deviennent les cas à signaler. np.isfinite repère notamment des nombres infinis ; isna repère les valeurs manquantes.

La cohérence code/libellé est aussi contrôlée : le code 2 doit correspondre à Appartement et le code 4 au libellé des locaux. map(LIBELLES_TYPES) traduit les codes en libellés attendus, puis .ne() compare le libellé réel au libellé attendu. Les compteurs se lisent par règle : une même ligne peut être signalée par plusieurs règles.

Si un compteur dépasse zéro, gt(0).any() devient vrai et raise ValueError arrête l’exécution. Cet arrêt est volontaire : il faut comprendre l’anomalie avant de poursuivre. La cellule ne supprime pas automatiquement une vente chère ni une surface inhabituelle.

duplicated() cherche ensuite les lignes entièrement identiques à une ligne précédente. Le fichier contient 16 répétitions exactes au-delà de la première occurrence. Sans identifiant de mutation fiable, elles restent dans les statistiques descriptives. Pour la modélisation, une seule occurrence sera gardée afin qu’une même observation ne puisse pas se retrouver à la fois dans l’apprentissage et dans le test.

Enfin, le code postal est converti en texte après validation : il représente une catégorie géographique, pas une quantité à additionner. Cela explique pourquoi les filtres ultérieurs utilisent la chaîne '75006'. Le code de type reste un entier catégoriel, 2 ou 4.

### Fonctions et méthodes

- `.le(), .between(), .isin()` : Construisent les conditions « inférieur ou égal », « dans l’intervalle » et « appartient à la liste autorisée ».
- `~ / .sum()` : Inverse un masque vrai/faux, puis compte les cas vrais.
- `np.isfinite / .isna()` : Repèrent les valeurs non finies et les valeurs manquantes.
- `.map() / .ne()` : Traduisent les codes puis comparent les libellés attendus et observés.
- `.gt(0).any() / raise ValueError` : Déclenchent un arrêt explicite lorsqu’au moins un contrôle échoue.
- `.duplicated() / .astype()` : Comptent les répétitions exactes et fixent les types utilisés ensuite.

### Résultat attendu

Aucune anomalie bloquante n’est observée dans les sources actuelles. Les 16 répétitions historiques sont signalées ; la future base de modélisation comporte 26 180 lignes distinctes.

### À retenir

- Une répétition exacte n’est pas automatiquement une vente à supprimer : son traitement dépend de l’objectif et des identifiants disponibles.
- Les compteurs d’anomalies peuvent se recouper ; leur somme n’est pas forcément le nombre de lignes différentes problématiques.
- Les données descriptives et la base d’apprentissage n’ont pas exactement le même nombre de lignes, pour une raison documentée.

### Vérifier par vous-même

- [ ] Tous les compteurs bloquants sont nuls avant de poursuivre.
- [ ] Les 16 répétitions sont expliquées dans le commentaire ; aucune suppression silencieuse n’a lieu à ce stade.
- [ ] Les codes postaux sont du texte pour rester cohérents avec les filtres suivants.

### Question minute

Pourquoi retirer les répétitions avant de séparer apprentissage et test, plutôt qu’après ?

## 1.2 — Identifier les deux familles de biens

Repères : C05.

### Objectif

Savoir ce que contient l’historique et mesurer la place de chaque type avant de comparer leurs prix.

### Code à repérer

```python
types_biens = (
    historique.groupby(['code_type_local', 'type_local']).size()
    .rename('Nombre de lignes').reset_index()
)
types_biens['Part (%)'] = 100 * types_biens['Nombre de lignes'] / len(historique)
display(types_biens)
```

### Lecture pas à pas

Une colonne de codes peut être difficile à interpréter seule. Le regroupement utilise donc ensemble code_type_local et type_local : un groupe correspond à une association entre un code et un libellé. La cohérence de cette association a déjà été vérifiée par le contrôle qualité.

groupby ne calcule pas encore un résultat final : il prépare des groupes de lignes partageant les mêmes clés. size() compte toutes les lignes de chaque groupe. On obtient ainsi un effectif par famille de biens, plutôt qu’un tableau de prix.

rename donne un nom lisible à la mesure, puis reset_index() transforme les clés de regroupement en colonnes ordinaires. Le tableau devient plus simple à afficher : une ligne par type, avec son code, son libellé et son effectif.

La part est calculée avec le même dénominateur pour les deux groupes : 100 × nombre de lignes du groupe / nombre total de lignes. Il faut multiplier par 100 pour passer d’une fraction entre 0 et 1 à un pourcentage. La catégorie des locaux réunit des usages industriels, commerciaux ou assimilés ; elle ne signifie pas uniquement « commerce ». 

### Fonctions et méthodes

- `.groupby([colonne1, colonne2])` : Rassemble les lignes selon les deux clés ; ici le code et son libellé.
- `.size()` : Compte les lignes de chaque groupe.
- `.rename() / .reset_index()` : Nomme la mesure et remet les clés de regroupement dans les colonnes du tableau.
- `len(historique)` : Donne le nombre total de lignes, utilisé comme dénominateur des parts.

### Résultat attendu

Deux types sont présents : 24 353 appartements, soit 92,96 % des lignes ; 1 843 locaux industriels, commerciaux ou assimilés, soit 7,04 %.

### À retenir

- Un code décrit une catégorie ; sa valeur numérique n’est pas une grandeur physique.
- Le type majoritaire influence fortement une moyenne calculée sur tous les biens.
- Les deux parts utilisent le même total et doivent représenter ensemble environ 100 %, aux arrondis près.

### Vérifier par vous-même

- [ ] Le tableau affiche bien deux associations code/libellé.
- [ ] Le code 4 n’est pas renommé « commerce » seul, ce qui rétrécirait à tort sa définition.
- [ ] Les effectifs des deux groupes se rapprochent du total de 26 196 lignes.

### Question minute

Pourquoi une moyenne sur tous les biens ne représente-t-elle pas également les deux familles ?

## 1.3 — Compter les observations et rapprocher les totaux

Repères : C06.

### Objectif

Vérifier que toutes les lignes historiques appartiennent à l’un des deux types autorisés.

### Code à repérer

```python
nb_appartements = int(historique['code_type_local'].eq(2).sum())
nb_locaux = int(historique['code_type_local'].eq(4).sum())
assert nb_appartements + nb_locaux == len(historique)
display(pd.DataFrame({
    'Population': ['Total', 'Appartements', 'Locaux industriels, commerciaux ou assimilés'],
    'Nombre de lignes / transactions représentées': [len(historique), nb_appartements, nb_locaux],
}))
```

### Lecture pas à pas

Cette cellule reprend les effectifs sous une autre forme pour vérifier leur cohérence. Elle ne cherche pas à entraîner un modèle ni à compter les lignes d’un tableau déjà agrégé : elle travaille directement sur la colonne code_type_local de l’historique.

eq(2) renvoie True pour chaque ligne d’appartement et False pour les autres. Dans une somme, True vaut 1 et False vaut 0. La somme donne donc le nombre de lignes qui satisfont la condition. Le même raisonnement est répété avec le code 4 pour les locaux.

L’assertion vérifie une identité simple : appartements + locaux = total. Si elle échoue, on ne doit pas ajuster le résultat à la main ; il faut chercher une catégorie inattendue, un filtre différent ou un changement dans les données. Cette vérification complète les contrôles de type.

Le DataFrame final rapproche total et sous-totaux dans un affichage unique. On parle de lignes ou de transactions représentées, car le classeur ne fournit pas d’identifiant permettant de garantir que chaque ligne est une vente distincte. Les répétitions descriptives signalées précédemment sont toujours incluses.

### Fonctions et méthodes

- `.eq(2) / .eq(4)` : Testent l’égalité ligne par ligne avec le code d’appartement ou de local.
- `.sum() / int()` : Comptent les réponses vraies et produisent un entier lisible.
- `assert` : Arrête l’exécution si l’égalité de rapprochement n’est pas respectée.
- `pd.DataFrame` : Présente les trois effectifs dans un tableau de synthèse.

### Résultat attendu

Le rapprochement est exact : 24 353 + 1 843 = 26 196 lignes historiques.

### À retenir

- Un filtre vrai/faux est appelé masque booléen.
- Un sous-total devient utile lorsqu’on peut le rapprocher d’un total de référence.
- Un nombre de lignes n’est pas nécessairement un nombre garanti de transactions distinctes.

### Vérifier par vous-même

- [ ] Les deux sous-totaux sont calculés sur le même DataFrame historique.
- [ ] L’assertion passe sans modifier les chiffres.
- [ ] Les effectifs concordent avec ceux de la section 1.2.

### Question minute

Que compterait historique['code_type_local'].eq(2).sum() sur une colonne contenant [2, 4, 2] ?

## 1.4 — Définir la période et calculer le prix au m²

Repères : C07.

### Objectif

Créer une mesure comparable entre biens et deux représentations du temps adaptées aux tableaux et à la régression.

### Code à repérer

```python
date_min = historique['date_mutation'].min()
date_max = historique['date_mutation'].max()
historique['annee'] = historique['date_mutation'].dt.year
historique['date_annees'] = (historique['date_mutation'] - DATE_ORIGINE).dt.days / 365.25
historique['prix_m2'] = historique['valeur_fonciere'] / historique['surface_reelle']
assert np.isfinite(historique['prix_m2']).all()
```

```python
display(historique.groupby(['annee', 'code_type_local']).size().unstack(fill_value=0)
        .rename(columns={2: 'Appartements', 4: 'Locaux'}))
display(historique[['date_mutation', 'valeur_fonciere', 'surface_reelle', 'prix_m2']].head(5))
```

### Lecture pas à pas

La première question est temporelle : de quand datent réellement les observations disponibles ? min() et max() appliqués à date_mutation donnent les bornes observées, qui peuvent différer des bornes annoncées par le nom du fichier.

Deux colonnes de temps répondent à deux usages. annee extrait seulement 2017, 2018, etc., pour regrouper les ventes par année. date_annees mesure un temps continu depuis le 1er janvier 2017 : différence en jours, puis division par 365,25 pour exprimer approximativement cette durée en années. Cette seconde mesure sera utilisée pour les corrélations et le modèle.

La valeur foncière est le prix total d’un bien en euros. Le prix au m² est ce montant divisé par sa surface réelle. Exemple pédagogique : 150 000 € pour 30 m² donnent 150 000 / 30 = 5 000 €/m². Le calcul est fait ligne par ligne : chaque montant est divisé par la surface de la même ligne.

Le contrôle des surfaces positives a été réalisé avant la division afin d’éviter une division par zéro. np.isfinite vérifie ensuite que le résultat reste un nombre fini. Le tableau croisé des années et types compte les lignes par année et par famille ; l’aperçu final permet de lire ensemble la date, la valeur, la surface et le prix calculé.

### Fonctions et méthodes

- `.min() / .max()` : Repèrent la première et la dernière date réellement observées.
- `.dt.year / .dt.days` : Extraient une année de calendrier et un nombre de jours depuis une durée.
- `Division entre colonnes` : Calcule un ratio pour chaque ligne en alignant les observations du tableau.
- `np.isfinite(...).all()` : Vérifie que chaque prix calculé est fini.
- `.groupby(...).size().unstack()` : Compte par année et type, puis transforme les types en colonnes de tableau.

### Résultat attendu

L’historique observé va du 02/01/2017 au 31/12/2021. Chaque ligne dispose maintenant de son année, de son temps continu depuis 2017 et de son prix au m².

### À retenir

- Valeur foncière : euros. Surface : m². Prix au m² : euros par m².
- annee sert à regrouper ; date_annees conserve une progression continue du temps.
- Un ratio individuel doit être calculé avant de calculer la moyenne de ces ratios.

### Vérifier par vous-même

- [ ] Les dates extrêmes sont compatibles avec la période du projet.
- [ ] Aucun prix au m² n’est infini et aucune surface n’est nulle.
- [ ] Sur quelques lignes, prix au m² × surface reconstitue la valeur foncière.

### Question minute

Un bien de 150 000 € et 30 m² et un bien de 300 000 € et 60 m² ont-ils le même prix total et le même prix au m² ?

## 1.5 — Comparer les prix des appartements d’une année à l’autre

Repères : C08.

### Objectif

Construire une synthèse annuelle des appartements et interpréter correctement moyenne, médiane et taux de variation.

### Code à repérer

```python
appartements = historique.loc[historique['code_type_local'].eq(2)].copy()
locaux = historique.loc[historique['code_type_local'].eq(4)].copy()
```

```python
annuel_appartements = appartements.groupby('annee').agg(
    transactions=('prix_m2', 'size'),
    valeur_moyenne_euros=('valeur_fonciere', 'mean'),
    surface_moyenne_m2=('surface_reelle', 'mean'),
    prix_m2_moyen=('prix_m2', 'mean'),
    prix_m2_median=('prix_m2', 'median'),
)
```

### Lecture pas à pas

Le filtre avec loc sélectionne les lignes dont code_type_local vaut 2. On sépare les appartements des locaux pour éviter qu’un changement dans la proportion des types brouille directement leur comparaison. copy() crée des sous-tableaux de travail indépendants.

groupby('annee') forme un groupe de ventes par année. agg calcule plusieurs indicateurs dans chaque groupe. Une paire comme transactions=('prix_m2', 'size') signifie : créer une colonne nommée transactions, à partir de la colonne prix_m2, en comptant ses lignes. Les autres paires demandent moyenne ou médiane de la colonne indiquée.

La moyenne du prix au m² donne le même poids à chaque ligne. Elle est différente du ratio des sommes, qui donne davantage de poids aux surfaces importantes. Exemple pédagogique : 150 000 €/30 m² = 5 000 €/m² et 600 000 €/100 m² = 6 000 €/m². La moyenne des deux prix est 5 500 €/m², alors que 750 000 €/130 m² vaut environ 5 769 €/m².

La médiane partage les prix triés en deux moitiés et réagit moins aux valeurs extrêmes. Afficher moyenne et médiane côte à côte aide à vérifier si quelques valeurs élevées déplacent fortement la moyenne. Le notebook conserve aussi les effectifs, la valeur totale moyenne par bien et la surface moyenne.

La variation entre deux années est 100 × (moyenne finale / moyenne initiale − 1). Les deux courbes permettent de lire le mouvement, puis les commentaires donnent les écarts calculés. Le formatage rend les chiffres lisibles sans arrondir les nombres conservés pour les calculs. Ces moyennes sont nominales : inflation et caractéristiques des biens ne sont pas corrigées.

### Fonctions et méthodes

- `.loc[masque].copy()` : Sélectionne une population puis en crée une copie de travail.
- `.groupby('annee').agg(...)` : Produit un tableau annuel avec plusieurs mesures nommées.
- `mean / median / size` : Calculent moyenne, médiane et nombre de lignes ; ces mesures ne répondent pas à la même question.
- `.loc[année, colonne]` : Lit une valeur par ses étiquettes dans le tableau annuel pour calculer les variations.
- `ax.plot / legende_figure / terminer_figure` : Dessinent les courbes, placent leur légende lisible et enregistrent la figure.

### Résultat attendu

Le prix moyen au m² des appartements passe de 9 493 € en 2017 à 10 675 € en 2020, puis 10 456 € en 2021. Variation 2017–2021 : +10,1 % ; variation 2020–2021 : −2,1 %.

### À retenir

- La hausse de 10,1 % concerne le prix moyen au m², pas le prix total moyen d’un appartement.
- La moyenne des ratios et le ratio des sommes sont deux indicateurs différents.
- Les ventes de 2017 et 2021 portent sur des biens différents : on ne suit pas ici le prix d’un même appartement.

### Vérifier par vous-même

- [ ] Les effectifs annuels se rapprochent des 24 353 appartements.
- [ ] Les axes affichent les années et l’unité €/m² ; la légende distingue moyenne et médiane.
- [ ] Le dénominateur du taux de variation est bien la moyenne de l’année de départ.

### Question minute

Pourquoi une baisse en 2021 peut-elle coexister avec une hausse entre 2017 et 2021 ?

## 1.6A — Construire le tableau des vingt arrondissements

Repères : C09.

### Objectif

Organiser les moyennes annuelles dans une matrice dont les lignes sont les arrondissements et les colonnes les années.

### Code à repérer

```python
codes_attendus = [str(cp) for cp in range(75001, 75021)]
codes_observes = sorted(appartements['code_postal'].unique())
assert codes_observes == codes_attendus, 'Vérifier la couverture des 20 arrondissements.'
prix_arrondissements = appartements.pivot_table(
    index='code_postal', columns='annee', values='prix_m2', aggfunc='mean'
).reindex(index=codes_attendus, columns=range(2017, 2022))
```

```python
comparaison_arrondissements = prix_arrondissements.copy()
comparaison_arrondissements['Évolution 2017–2021 (%)'] = 100 * (
    prix_arrondissements[2021] / prix_arrondissements[2017] - 1
)
comparaison_arrondissements['Ventes 2021 (n)'] = effectifs_arrondissements[2021]
tableau_arrondissements = comparaison_arrondissements.rename(index=libelle_arrondissement)
tableau_arrondissements.index.name = 'Arrondissement (code postal)'
```

### Lecture pas à pas

Une moyenne pour tout Paris cache les différences géographiques. La cellule vérifie donc d’abord que les appartements couvrent les vingt codes postaux attendus. range(75001, 75021) exclut sa borne finale : il produit bien les codes 75001 à 75020. str transforme chaque code en texte, comme dans la colonne déjà préparée.

pivot_table répond à quatre questions : quelles lignes ? index='code_postal'. Quelles colonnes ? columns='annee'. Quelles valeurs ? values='prix_m2'. Quel calcul dans chaque case ? aggfunc='mean'. Une case est donc la moyenne des prix au m² des appartements d’un arrondissement pour une année, et non la moyenne de tous les biens parisiens.

reindex impose l’ordre des vingt arrondissements et des cinq années. Il rend une combinaison absente visible au lieu de la laisser disparaître du tableau. Un second tableau, créé par crosstab, compte les observations dans les mêmes cases. Une moyenne et son effectif racontent des choses complémentaires : un prix élevé ne signifie pas qu’il y a beaucoup de ventes.

Les contrôles vérifient que la somme des effectifs retrouve le total des appartements et qu’aucune moyenne n’est absente. Une copie reçoit ensuite deux colonnes supplémentaires : l’évolution de la moyenne entre 2017 et 2021 et le nombre de ventes de 2021. Ces colonnes enrichissent la comparaison sans changer la matrice des moyennes utilisée pour les courbes.

L’index est une étiquette de ligne, ici un code postal sous forme de texte. Les années des colonnes sont des entiers. prix_arrondissements.loc['75006', 2021] lit donc la case du 6e en 2021 ; prix_arrondissements[2021] lit toute la colonne 2021. Les libellés « 6e (75006) » sont ajoutés seulement au tableau d’affichage.

### Fonctions et méthodes

- `range / str / sorted / unique` : Construisent les codes attendus et comparent cette couverture aux codes observés.
- `.pivot_table(index, columns, values, aggfunc)` : Calcule les moyennes dans une matrice arrondissement × année.
- `.reindex()` : Fixe l’ordre et fait apparaître les combinaisons éventuellement absentes.
- `pd.crosstab` : Produit la matrice des nombres de ventes, distincte de celle des prix.
- `.notna().all().all()` : Vérifie que toutes les cases de moyenne sont renseignées.
- `.rename() / afficher_tableau` : Préparent une copie lisible sans modifier les codes ni la précision de calcul.

### Résultat attendu

Le tableau contient 20 lignes et 7 colonnes : cinq moyennes annuelles, une évolution en pourcentage et un effectif 2021. Les 100 moyennes sont présentes ; la plus petite repose sur 63 ventes représentées.

### À retenir

- Une case du pivot possède un périmètre précis : un type, un arrondissement et une année.
- L’index n’est pas le numéro de position d’une ligne ; .loc lit ses étiquettes.
- Une absence de moyenne ne vaut pas zéro : il faut la signaler et examiner les effectifs.

### Vérifier par vous-même

- [ ] Les vingt arrondissements et les cinq années figurent dans le tableau.
- [ ] La somme des effectifs retrouve toutes les lignes d’appartements.
- [ ] La moyenne du 6e en 2021 est proche de 13 795 €/m², et non de 13 795 € par bien.

### Question minute

Que sélectionne prix_arrondissements[2021] et pourquoi ne pas écrire prix_arrondissements['2021'] ?

## 1.6B — Lire les trajectoires sans perdre les légendes

Repères : C10.

### Objectif

Afficher les vingt évolutions sur des figures comparables, tout en gardant chaque série identifiable.

### Code à repérer

```python
fig, ax = plt.subplots()
ax.plot(prix_arrondissements.columns, prix_arrondissements.loc['75001'], marker='o', color=BLEU)
ax.set(title='1er arrondissement — prix moyen au m² des appartements',
       xlabel='Année de vente', ylabel='Prix moyen (€/m²)', xticks=range(2017, 2022))
ax.yaxis.set_major_formatter(format_euros)
terminer_figure(fig, '02_premier_arrondissement')
```

```python
limite_basse = 500 * np.floor(prix_arrondissements.min().min() / 500)
limite_haute = 500 * np.ceil(prix_arrondissements.max().max() / 500)
for panneau in range(4):
    codes_groupe = codes_attendus[panneau * 5:(panneau + 1) * 5]
    debut, fin = panneau * 5 + 1, (panneau + 1) * 5
    fig, ax = plt.subplots(figsize=(9.2, 5.3))
```

```python
    for i, cp in enumerate(codes_groupe):
        ax.plot(prix_arrondissements.columns, prix_arrondissements.loc[cp],
                color=palette[i], marker=marqueurs[i], label=libelle_arrondissement(cp),
                linewidth=2, markersize=6)
    ax.set(title=f'Appartements — arrondissements {debut} à {fin} (2017–2021)',
           xlabel='Année de vente', ylabel='Prix moyen (€/m²)',
           xticks=range(2017, 2022), ylim=(limite_basse, limite_haute))
    ax.yaxis.set_major_formatter(format_euros)
```

### Lecture pas à pas

Le premier graphique isole le 1er arrondissement demandé dans l’exercice. L’abscisse contient les cinq années et l’ordonnée ses cinq prix moyens au m². Il sert à apprendre à lire une trajectoire simple avant de comparer plusieurs séries. Son axe est ajusté à cette seule courbe : on ne doit pas comparer sa pente visuelle directement à celle des quatre graphiques de groupe.

Vingt courbes sur une seule figure rendraient les couleurs et la légende difficiles à suivre. La cellule crée donc quatre figures successives, chacune avec cinq arrondissements. La tranche panneau * 5 : (panneau + 1) * 5 choisit d’abord les positions 0 à 4, puis 5 à 9, etc. La borne de fin d’une tranche est exclue.

Les limites verticales sont calculées une seule fois sur l’ensemble des vingt séries, puis arrondies vers le bas et vers le haut par pas de 500 €/m². Ces limites communes sont imposées aux quatre figures : ici 7 500 à 14 000 €/m². Une même hauteur représente ainsi le même prix partout ; un panneau n’amplifie pas artificiellement sa propre variation.

La boucle interne trace chaque arrondissement avec une couleur et un marqueur. Les couleurs sont réutilisées d’un groupe à l’autre ; la légende locale donne donc l’identité à lire. libelle_arrondissement transforme par exemple 75006 en « 6e (75006) ». Les marqueurs offrent un repère supplémentaire quand les couleurs se ressemblent.

legende_figure réserve une zone sous les axes. La légende ne recouvre ni les courbes ni les graduations et conserve une police de 12 points. terminer_figure enregistre chaque image sur fond clair. Les cinq figures produites par cette cellule ont des rôles distincts : un exemple isolé, puis quatre comparaisons à échelle commune.

### Fonctions et méthodes

- `plt.subplots()` : Crée la figure et son axe ; la cellule recommence pour chaque groupe afin de produire des images séparées.
- `.loc[code_postal]` : Lit la ligne des cinq années d’un arrondissement dans la matrice des prix.
- `np.floor / np.ceil` : Arrondissent les bornes communes vers le bas et vers le haut.
- `range(4) / enumerate()` : Parcourent les quatre groupes puis donnent une position et un code à chaque série du groupe.
- `ax.plot / ax.set(ylim=...)` : Tracent les lignes et imposent les mêmes limites verticales aux quatre comparaisons.
- `legende_figure / terminer_figure` : Séparent la légende des données et sauvegardent chaque figure lisible.

### Résultat attendu

La cellule produit une courbe du 1er arrondissement puis quatre graphiques : 1er–5e, 6e–10e, 11e–15e et 16e–20e. Les quatre comparaisons partagent les bornes 7 500–14 000 €/m².

### À retenir

- L’axe commun permet de comparer les niveaux et l’amplitude des mouvements entre les quatre groupes.
- La couleur seule ne suffit pas : il faut lire le libellé de la légende du graphique concerné.
- Une courbe annuelle représente une moyenne de ventes différentes, pas le suivi du même logement.

### Vérifier par vous-même

- [ ] Les quatre groupes contiennent cinq séries chacun, soit vingt au total.
- [ ] Les quatre axes verticaux ont exactement les mêmes bornes.
- [ ] La légende complète est visible sous chaque graphique, avec des codes et des marqueurs lisibles.

### Question minute

Pourquoi ne pas laisser chaque graphique de groupe choisir automatiquement son propre axe vertical ?

## 1.6C — Classer les niveaux de prix de 2021

Repères : C11.

### Objectif

Comparer les vingt moyennes d’une même année et quantifier l’écart entre les deux extrêmes.

### Code à repérer

```python
classement_2021 = prix_arrondissements[2021].sort_values(ascending=False)
cp_haut, cp_bas = classement_2021.index[0], classement_2021.index[-1]
fig, ax = plt.subplots(figsize=(9.2, 8.0))
couleurs_classement = [BLEU if cp == cp_haut else ORANGE if cp == cp_bas else '#9AAEBE'
                       for cp in classement_2021.index]
barres = ax.barh([libelle_arrondissement(cp) for cp in classement_2021.index],
                classement_2021.values, color=couleurs_classement, height=.72)
ax.invert_yaxis()
```

```python
ecart_arrondissements_2021 = classement_2021.iloc[0] - classement_2021.iloc[-1]
ecart_relatif_arrondissements = 100 * (classement_2021.iloc[0] / classement_2021.iloc[-1] - 1)
```

### Lecture pas à pas

Les courbes précédentes répondent à « comment les moyennes ont-elles évolué ? ». Le classement répond à une autre question : « où les prix moyens sont-ils les plus élevés en 2021 ? ». On sélectionne la colonne 2021, puis on la trie du plus grand au plus petit. Comparer une seule année évite de mélanger ici des périodes différentes.

classement_2021 est une Series : son index contient les codes postaux et ses valeurs contiennent les moyennes triées. index[0] donne le code du premier, index[-1] celui du dernier. iloc[0] et iloc[-1] donnent leurs valeurs par position. C’est la différence entre l’identité d’une observation et sa mesure.

Le graphique utilise des barres horizontales pour garder les vingt libellés lisibles. invert_yaxis place le premier du classement en haut. L’axe horizontal commence à zéro, afin que la longueur des barres représente honnêtement les niveaux de prix. Les valeurs sont ajoutées au bout des barres pour permettre une lecture exacte.

Deux écarts complètent l’image. La soustraction donne un écart absolu en €/m². Le ratio donne un écart relatif en pourcentage ; le dénominateur choisi est la moyenne du 19e, la plus basse. Ces indicateurs ne sont pas interchangeables et le pourcentage dépend de la référence retenue.

Le commentaire ajoute les effectifs : 105 appartements dans le 6e contre 230 dans le 19e en 2021. Ces moyennes ne comparent pas des biens identiques et ne neutralisent ni état, étage, surface ou qualité. Le classement décrit les ventes du fichier ; il ne prouve pas un effet causal isolé de l’arrondissement.

### Fonctions et méthodes

- `prix_arrondissements[2021]` : Sélectionne la Series des moyennes d’une seule année.
- `.sort_values(ascending=False)` : Classe les moyennes de la plus élevée à la plus faible.
- `.index / .iloc` : Accèdent respectivement aux étiquettes et aux valeurs par position.
- `ax.barh / ax.invert_yaxis / ax.bar_label` : Tracent des barres horizontales, placent le meilleur rang en haut et ajoutent les valeurs.
- `Différence / ratio` : Mesurent un écart dans l’unité initiale et un écart relatif à une référence explicitée.

### Résultat attendu

En 2021 : 6e, 13 795 €/m² et 105 ventes ; 19e, 8 829 €/m² et 230 ventes. L’écart est de 4 966 €/m², soit +56,3 % par rapport au 19e.

### À retenir

- Un classement d’une année et une trajectoire sur cinq ans répondent à deux questions différentes.
- Le prix du 6e est 56,3 % au-dessus du 19e ; inverser le dénominateur ne donnerait pas −56,3 %.
- Un prix moyen élevé n’est ni un rendement locatif, ni une recommandation d’achat.

### Vérifier par vous-même

- [ ] Les vingt arrondissements sont présents, dans l’ordre décroissant.
- [ ] L’axe des barres commence à zéro et les valeurs ne sont pas tronquées.
- [ ] Le commentaire donne l’unité, l’année, la population et les effectifs des extrêmes.

### Question minute

Pourquoi le pourcentage d’écart utilise-t-il classement_2021.iloc[-1] au dénominateur ?

## 1.7 — Regarder les ventes individuelles dans le 6e arrondissement

Repères : C12.

### Objectif

Observer la dispersion des prix au m² derrière les moyennes annuelles avant de calculer une corrélation.

### Code à repérer

```python
appartements_6e = appartements.loc[appartements['code_postal'].eq('75006')].sort_values('date_mutation').copy()
print(f'Appartements du 6ᵉ arrondissement : {fr(len(appartements_6e))} transactions représentées.')
display(appartements_6e.groupby('annee').agg(
    transactions=('prix_m2', 'size'), moyenne_euros_m2=('prix_m2', 'mean'),
    minimum_euros_m2=('prix_m2', 'min'), maximum_euros_m2=('prix_m2', 'max'),
))
```

```python
fig, ax = plt.subplots()
ax.scatter(appartements_6e['date_mutation'], appartements_6e['prix_m2'], s=18, alpha=.45, color=BLEU)
ax.set(title='6ᵉ arrondissement — prix au m² de chaque appartement vendu', xlabel='Date de vente (2017–2021)', ylabel='Prix (€/m²)')
ax.set_xlim(pd.Timestamp('2017-01-01'), pd.Timestamp('2022-01-01'))
ax.set_xticks([pd.Timestamp(f'{an}-01-01') for an in range(2017, 2022)])
ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y'))
ax.yaxis.set_major_formatter(format_euros)
terminer_figure(fig, '04_transactions_sixieme')
```

### Lecture pas à pas

Une moyenne annuelle résume beaucoup de lignes en un nombre. Le nuage de points revient aux observations individuelles pour montrer les écarts entre ventes au sein d’un même arrondissement. Le filtre part du tableau appartements, puis ne conserve que le code postal texte '75006' : les locaux du 6e sont donc exclus.

sort_values('date_mutation') place les ventes dans l’ordre temporel. Il ne change pas leurs prix ni leur effectif. copy() crée un sous-tableau que les sections 1.7 et 1.8 vont partager. Le tableau annuel complémentaire indique combien de points se trouvent dans chaque année et fournit moyenne, minimum et maximum.

Dans ax.scatter, chaque ligne donne un point : sa date est l’abscisse et son prix au m² l’ordonnée. Une zone dense représente plusieurs ventes proches dans le temps et le prix, pas un seul bien suivi plusieurs fois. La transparence alpha=.45 laisse apparaître les superpositions sans changer les données.

Les limites et graduations temporelles sont fixées pour rendre les années lisibles. La borne droite 01/01/2022 sert seulement à encadrer les dernières ventes de 2021 ; elle n’ajoute aucune observation de 2022. Le format des graduations affiche les années et les prix avec leurs unités.

On peut observer une progression au début de la période puis un tassement, ainsi qu’une dispersion à date proche. Cette dispersion rappelle que la date seule ne suffit pas à décrire tous les prix. La section suivante mesurera l’association observée ; elle ne transformera pas cette observation en explication causale.

### Fonctions et méthodes

- `.loc[...eq('75006')]` : Restreint le tableau déjà filtré aux appartements du 6e arrondissement.
- `.sort_values('date_mutation')` : Ordonne les lignes par date sans modifier leur contenu.
- `.groupby('annee').agg(...)` : Rapproche effectif, moyenne et extrêmes annuels du nuage individuel.
- `ax.scatter` : Dessine un point par observation ; alpha règle uniquement la transparence graphique.
- `ax.set_xlim / ax.set_xticks / mdates.DateFormatter` : Définissent la fenêtre temporelle et ses graduations lisibles.

### Résultat attendu

Le sous-ensemble contient 709 appartements. Leurs prix au m² vont d’environ 12 065 à 14 170 €/m² sur la période 2017–2021.

### À retenir

- Un point représente une ligne de vente ; une courbe de moyenne représenterait un résumé de plusieurs points.
- Un filtre géographique ne suffit pas : le filtre sur le type doit également être correct.
- Une borne d’axe peut dépasser la dernière observation sans représenter une prévision.

### Vérifier par vous-même

- [ ] Les 709 lignes ont toutes code_postal = '75006' et code_type_local = 2.
- [ ] Les dates sont triées et restent dans 2017–2021.
- [ ] L’axe vertical indique bien €/m², et non la valeur foncière totale en euros.

### Question minute

Pourquoi voir plusieurs prix différents autour d’une même date est-il utile ?

## 1.8 — Mesurer l’association entre le temps et les prix du 6e

Repères : C13.

### Objectif

Lire un coefficient de corrélation et sa p-value sur le bon périmètre, sans lui faire dire davantage que ce qu’il mesure.

### Code à repérer

```python
r_date, p_date = pearsonr(appartements_6e['date_annees'], appartements_6e['prix_m2'])
rho_date, p_spearman = spearmanr(appartements_6e['date_annees'], appartements_6e['prix_m2'])
display(pd.DataFrame({
    'Méthode': ['Pearson (linéaire)', 'Spearman (monotone)'],
    'Coefficient': [r_date, rho_date],
    'p-value': [afficher_p(p_date), afficher_p(p_spearman)],
    'Nombre de ventes': [len(appartements_6e)] * 2,
}))
```

### Lecture pas à pas

La cellule reprend exactement les 709 appartements préparés en 1.7. date_annees est la durée numérique depuis le début de 2017, calculée en 1.4. Un nombre de jours ou d’années permet de comparer des dates à une mesure numérique ; il ne représente pas une caractéristique physique du bien.

pearsonr renvoie deux résultats, affectés à r_date et p_date. Le premier, compris entre −1 et +1, mesure une association linéaire : positif signifie que les valeurs élevées de l’une tendent à accompagner les valeurs élevées de l’autre. Une valeur proche de +1 indique une association linéaire forte dans l’échantillon étudié.

La p-value est calculée sous une hypothèse de corrélation linéaire nulle et sous les hypothèses du test. Une petite p-value indique que les données observées sont peu compatibles avec cette hypothèse ; ce n’est pas la probabilité que notre conclusion soit vraie. Les ventes peuvent partager des facteurs géographiques et temporels : l’indépendance n’est pas garantie et la p-value reste indicative.

spearmanr complète le calcul en travaillant sur les rangs : il cherche une association monotone, c’est-à-dire une tendance à augmenter ou diminuer ensemble, qui n’a pas besoin d’être une droite. Le tableau place les deux méthodes côte à côte avec leur effectif pour éviter de confondre des périmètres différents.

afficher_p évite d’imprimer « 0,00 » lorsque la p-value est seulement très petite. Le résultat r = 0,904 ne signifie ni « 90,4 % de bons classements », ni « le temps cause 90,4 % du prix ». Il s’agit d’une corrélation locale sur 2017–2021 ; elle ne garantit aucune hausse après 2021.

### Fonctions et méthodes

- `pearsonr(x, y)` : Renvoie le coefficient de corrélation linéaire et la p-value de son test.
- `spearmanr(x, y)` : Mesure l’association monotone à partir des rangs des observations.
- `Affectation à deux noms` : r_date, p_date = ... range séparément les deux résultats de la fonction.
- `afficher_p` : Présente les p-values très petites sans les confondre avec un zéro exact.
- `pd.DataFrame / display` : Rapprochent les deux coefficients, leurs p-values et le nombre d’observations.

### Résultat attendu

Sur les 709 appartements du 6e, Pearson vaut environ 0,904 et Spearman 0,915. Les p-values sont inférieures à 10⁻¹⁶ dans l’affichage. L’association temporelle observée est positive et forte.

### À retenir

- Un coefficient de corrélation dépend de la population et de la période utilisées.
- La p-value n’est pas un score de précision ni la probabilité d’un lien causal.
- Pearson et Spearman apportent deux lectures complémentaires ; aucun ne valide une prévision future.

### Vérifier par vous-même

- [ ] Les deux tableaux de mesures utilisent bien les mêmes 709 lignes du 6e.
- [ ] La date est numérique et les prix au m² sont finis.
- [ ] La conclusion parle d’association, en rappelant les limites des hypothèses statistiques.

### Question minute

Peut-on remplacer ce coefficient de 0,904 par une corrélation calculée sur toutes les ventes parisiennes ?

## 1.9 — Distinguer la valeur totale du prix unitaire dans le lien à la surface

Repères : C14.

### Objectif

Comparer deux relations qui paraissent proches mais ne portent pas sur la même grandeur : surface/valeur totale et surface/prix au m².

### Code à repérer

```python
resultats_correlations = []
for nom, sous_ensemble in [('Tous les biens', historique), ('Appartements', appartements), ('Locaux', locaux)]:
    for cible, nom_cible in [('valeur_fonciere', 'Valeur foncière (€)'), ('prix_m2', 'Prix au m² (€/m²)')]:
        r, p = pearsonr(sous_ensemble['surface_reelle'], sous_ensemble[cible])
        resultats_correlations.append({
            'Population': nom, 'Variable comparée à la surface': nom_cible,
            'n': len(sous_ensemble), 'Pearson r': r, 'p-value': afficher_p(p),
        })
```

```python
        ax.scatter(donnees['surface_reelle'], donnees[cible], s=14, alpha=.3,
                   color=couleur, label=label, marker=marker)
    ax.set(title=titre, xlabel='Surface réelle (m² ; échelle logarithmique)',
           ylabel=axe_y, xscale='log')
    if log_y:
        ax.set_yscale('log')
    else:
        ax.yaxis.set_major_formatter(format_euros)
```

### Lecture pas à pas

Une grande surface peut être associée à une valeur totale élevée sans avoir un prix au m² élevé. L’identité utile est valeur totale = surface × prix au m². Par exemple, à prix unitaire identique de 5 000 €/m², 30 m² valent 150 000 € et 60 m² valent 300 000 €. La valeur double alors que le prix au m² ne change pas.

La boucle extérieure parcourt trois populations : tous les biens, les appartements puis les locaux. La boucle intérieure parcourt deux mesures à comparer à la surface. Il y a donc six combinaisons. Chaque calcul crée un petit dictionnaire avec population, cible, effectif, coefficient et p-value ; append l’ajoute à une liste, ensuite transformée en tableau.

Deux figures séparées rendent la différence visible. La première compare surface et valeur foncière ; les deux axes sont logarithmiques. La seconde compare surface et prix au m² ; seule la surface est logarithmique. Des couleurs et marqueurs différents identifient les deux familles, tandis qu’une légende réservée sous la figure reste lisible.

Une échelle logarithmique représente les rapports : passer de 10 à 100 occupe la même distance que passer de 100 à 1 000. Elle aide à voir simultanément de petites et de grandes surfaces sans supprimer les grands biens. Elle nécessite des valeurs positives, déjà vérifiées en amont.

Le changement d’échelle concerne l’affichage. Les coefficients de Pearson sont calculés avant, sur les valeurs originales et non sur leurs logarithmes. La forte relation surface/valeur totale est compatible avec l’identité multiplicative ; elle n’établit pas qu’augmenter une surface ferait mécaniquement monter son prix au m², toutes choses égales par ailleurs.

### Fonctions et méthodes

- `Boucles for imbriquées` : Effectuent le même calcul sur trois populations et deux mesures, sans recopier six blocs.
- `pearsonr` : Mesure l’association linéaire sur les colonnes numériques originales.
- `.append() / pd.DataFrame` : Accumulent les résultats unitaires puis construisent la table de comparaison.
- `ax.scatter` : Affiche une observation par point, avec un marqueur et une couleur par type.
- `xscale='log' / ax.set_yscale('log')` : Changent la représentation des axes, sans changer les données des calculs précédents.

### Résultat attendu

Sur les 26 196 lignes historiques, Pearson surface/valeur totale vaut environ 0,984, contre seulement 0,103 pour surface/prix au m². Les deux résultats décrivent des relations différentes.

### À retenir

- « Plus grand, donc plus cher au total » ne signifie pas « plus grand, donc plus cher par m² ».
- Le graphique peut avoir une échelle logarithmique alors que la corrélation reste calculée sans logarithme.
- Comparer les populations séparément permet de vérifier ce que cache le total.

### Vérifier par vous-même

- [ ] Les axes précisent l’unité et les échelles logarithmiques.
- [ ] Les couleurs et marqueurs correspondent aux mêmes familles sur les deux figures.
- [ ] Le commentaire distingue clairement le coefficient 0,984 du coefficient 0,103.

### Question minute

Le fait d’afficher un axe logarithmique transforme-t-il automatiquement le Pearson calculé plus haut ?

## 1.10 — Comparer les locaux et les appartements sur un même indicateur

Repères : C15.

### Objectif

Décrire les locaux par année, puis comparer les deux familles avec la même unité et une période clairement définie.

### Code à repérer

```python
annuel_locaux = locaux.groupby('annee').agg(
    transactions=('prix_m2', 'size'), surface_moyenne_m2=('surface_reelle', 'mean'),
    prix_m2_moyen=('prix_m2', 'mean'), prix_m2_median=('prix_m2', 'median'),
)
afficher_tableau(annuel_locaux.rename(columns={
    'transactions': 'Ventes (n)', 'surface_moyenne_m2': 'Surface moyenne (m²)',
    'prix_m2_moyen': 'Prix moyen (€/m²)', 'prix_m2_median': 'Prix médian (€/m²)',
}), 'Locaux industriels, commerciaux ou assimilés — indicateurs annuels')
```

```python
fig, ax = plt.subplots()
ax.plot(annuel_appartements.index, annuel_appartements['prix_m2_moyen'], marker='o', color=BLEU, label='Appartements')
ax.plot(annuel_locaux.index, annuel_locaux['prix_m2_moyen'], marker='s', linestyle='--', color=ORANGE, label='Locaux et assimilés')
ax.set(title='Paris — prix moyen au m² selon le type de bien', xlabel='Année de vente', ylabel='Prix (€/m²)', xticks=range(2017, 2022))
ax.yaxis.set_major_formatter(format_euros)
legende_figure(fig)
terminer_figure(fig, '06_comparaison_types')
```

### Lecture pas à pas

Le tableau locaux a été créé en 1.5 à partir du code 4. La première agrégation reprend la logique annuelle déjà utilisée pour les appartements : nombre de lignes, surface moyenne, moyenne et médiane du prix au m². Garder la même définition des indicateurs rend la comparaison possible.

Un second regroupement porte sur toute la période 2017–2021 et utilise le type de bien comme clé. Il fournit un niveau global par famille. Ce tableau ne doit pas être confondu avec un indicateur calculé sur 2021 seulement : le périmètre temporel influence la valeur moyenne et doit rester visible dans le titre.

Les deux courbes annuelles partagent le même axe horizontal et la même unité verticale, €/m². Le libellé graphique « locaux et assimilés » est plus court pour rester lisible ; la catégorie source conserve sa définition complète, industrielle, commerciale ou assimilée. Le style de ligne et le marqueur complètent la couleur.

L’écart global est 100 × (moyenne des prix au m² des locaux / moyenne des prix au m² des appartements − 1). Chaque moyenne est calculée directement sur les lignes de la famille pour l’ensemble de la période. Ce n’est pas une moyenne non pondérée des cinq moyennes annuelles, car les effectifs peuvent changer selon l’année.

Un niveau moyen supérieur chez les locaux ne suffit pas à reconnaître le type d’un bien particulier. Les distributions se recouvrent et les localisations ou caractéristiques des biens diffèrent. Le résultat ne mesure ni une rentabilité locative, ni la performance d’un investissement : loyers, charges et coûts d’acquisition ne sont pas analysés ici.

### Fonctions et méthodes

- `.groupby('annee').agg(...)` : Décrit les locaux chaque année avec les mêmes familles de mesures que les appartements.
- `.groupby('type_local').agg(...)` : Calcule la comparaison globale des deux familles sur toute la période.
- `.rename()` : Raccourcit uniquement les libellés d’affichage et rend les unités explicites.
- `ax.plot / legende_figure` : Comparent les séries sur un axe commun avec une légende séparée des données.
- `.mean() / ratio − 1` : Mesurent l’écart relatif des moyennes globales des deux familles.

### Résultat attendu

Sur l’ensemble de 2017–2021 : moyenne des locaux 11 705 €/m², moyenne des appartements 10 222 €/m², soit un écart de +14,5 % relativement aux appartements. En 2021 seulement : 12 006 €/m² contre 10 456 €/m².

### À retenir

- Le pourcentage global de 14,5 % concerne toute la période, pas la seule année 2021.
- Une comparaison doit conserver la même unité et annoncer le dénominateur de son pourcentage.
- Une différence de moyennes n’est pas une règle certaine de classification d’un bien individuel.

### Vérifier par vous-même

- [ ] Les familles portent sur les bons codes 2 et 4.
- [ ] Les deux courbes ont les mêmes années et la même unité €/m².
- [ ] Les conclusions n’assimilent pas la valeur moyenne à la rentabilité ou à un type individuel certain.

### Question minute

Pourquoi ne pas appeler tous les biens du code 4 des « commerces » dans la légende ?

## 2.1 — Séparer ce que le modèle connaît de ce qu’il doit prédire

Repères : C16.

### Objectif

Comprendre X, y et le découpage de 33 % avant de lancer le moindre apprentissage.

### Code à repérer

```python
base_modele = historique.loc[~historique_brut.duplicated()].copy()
VARIABLES_NUMERIQUES = ['surface_reelle', 'date_annees']
VARIABLES_CATEGORIELLES = ['code_postal', 'type_local']
VARIABLES = VARIABLES_NUMERIQUES + VARIABLES_CATEGORIELLES
X = base_modele[VARIABLES]
y = base_modele['valeur_fonciere']
```

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=PART_TEST, random_state=GRAINE,
    stratify=base_modele['code_type_local'],
)
assert set(X_train.index).isdisjoint(X_test.index)
assert len(X_train) + len(X_test) == len(base_modele)
```

### Lecture pas à pas

Commencez par la première ligne. historique_brut.duplicated() repère les répétitions exactes après la première occurrence ; ~ inverse le masque pour garder les autres lignes. .loc sélectionne ces lignes et .copy() crée une table distincte. Les 16 répétitions sont ainsi retirées uniquement de la base de modélisation : les statistiques descriptives conservent leurs 26 196 lignes. Le modèle travaille sur 26 180 observations, pour éviter qu’une copie d’un même enregistrement se retrouve à la fois dans l’apprentissage et dans le test.

X est le tableau des informations disponibles avant la prédiction : surface réelle, date numérique, code postal et type. y est la colonne de réponses connues, valeur_fonciere, exprimée en euros. Une ligne de X et la ligne de même index dans y décrivent le même bien. Les noms X et y sont des conventions courantes ; X n’est pas une formule mystérieuse, mais un DataFrame de quatre colonnes, et y une Series.

VARIABLES_NUMERIQUES et VARIABLES_CATEGORIELLES sont deux listes de noms de colonnes. Leur addition avec + forme une liste de quatre noms ; elle n’additionne aucune donnée. Le code postal et le type restent des catégories : 75020 ne doit pas être compris comme une quantité vingt fois supérieure à une autre localisation.

train_test_split reçoit X et y ensemble pour les découper de façon synchronisée. X_train et y_train servent à apprendre ; X_test sert ensuite à prédire et y_test à vérifier ces prédictions. PART_TEST vaut 0.33 : environ un tiers des lignes est réservé au test, avec un arrondi nécessaire au nombre entier de lignes. random_state=GRAINE utilise ici 42 et rend le tirage reproductible à données et versions comparables. stratify maintient approximativement la proportion des deux types de biens dans les deux ensembles.

Les index originaux ne sont pas renumérotés, ce qui est normal. Les deux assert contrôlent que les lignes d’apprentissage et de test sont disjointes, puis que leur nombre total retrouve la base de départ. Ne triez pas X et y séparément et ne remplacez pas leurs index de façon différente : vous pourriez associer les caractéristiques d’un bien au prix d’un autre. Ce découpage aléatoire mélange les années 2017–2021 ; il prépare un test hors apprentissage, pas encore une véritable prévision d’année future.

### Fonctions et méthodes

- `duplicated()` : Produit un masque vrai pour les répétitions exactes après leur première occurrence.
- `.loc[...] et .copy()` : Sélectionnent les lignes choisies puis créent une table de travail séparée.
- `train_test_split(X, y, ...)` : Découpe ensemble les caractéristiques et leurs réponses, en conservant leur correspondance.
- `stratify` : Demande de conserver approximativement la proportion de chaque type dans le tirage.
- `assert et isdisjoint()` : Arrêtent l’exécution si le partage des lignes ne respecte pas les contrôles attendus.

### Résultat attendu

La base contient 26 180 lignes distinctes : 17 540 pour l’apprentissage et 8 640 pour le test. X possède quatre variables et y contient la valeur foncière totale en euros.

### À retenir

- X contient les informations d’entrée ; y contient la réponse connue pendant l’apprentissage.
- Le modèle apprend sur train. Le jeu test reste à l’écart de cet apprentissage.
- Les répétitions sont traitées avant le découpage ; les index assurent l’alignement des biens et de leurs prix.

### Vérifier par vous-même

- [ ] Contrôler que les nombres affichés sont 26 180, 17 540 et 8 640.
- [ ] Comparer X_train.index et y_train.index : ils doivent correspondre ligne à ligne, comme X_test.index et y_test.index.
- [ ] Vérifier que valeur_fonciere et le prix au m² observé ne figurent pas dans VARIABLES.

### Question minute

Pourquoi passer X et y au même train_test_split, plutôt que lancer deux tirages séparés ?

## 2.2 — Encoder les catégories, puis apprendre une valeur en euros

Repères : C17.

### Objectif

Suivre le passage des quatre colonnes d’entrée aux 22 variables utilisées par LinearRegression, sans apprendre sur le test.

### Code à repérer

```python
preparation = ColumnTransformer([
    ('numerique', 'passthrough', VARIABLES_NUMERIQUES),
    ('categoriel', OneHotEncoder(drop='first', handle_unknown='error'), VARIABLES_CATEGORIELLES),
], sparse_threshold=0)
modele_definition = Pipeline([
    ('preparation', preparation),
    ('regression', LinearRegression()),
])
```

```python
modele_test = clone(modele_definition)
modele_test.fit(X_train, y_train)
prediction_test = modele_test.predict(X_test)
assert np.isfinite(prediction_test).all()
```

### Lecture pas à pas

Une régression linéaire attend des nombres. La surface et la date sont déjà numériques : la branche numerique du ColumnTransformer les transmet avec passthrough, sans les modifier. Le code postal et le libellé du type demandent un autre traitement. La branche categoriel applique OneHotEncoder à ces deux colonnes. ColumnTransformer réunit ensuite les deux résultats dans le même ordre pour chaque bien.

OneHotEncoder remplace chaque catégorie par des indicateurs 0 ou 1. Par exemple, un indicateur de code postal vaut 1 quand le bien appartient à cette catégorie et 0 sinon. drop='first' retire une catégorie de référence par colonne, pour éviter une redondance avec l’interception de la régression. Dans cette exécution, les références affichées sont 75001 et Appartement. Elles ne sont ni des valeurs absentes ni des catégories exclues des biens : leurs indicateurs sont simplement implicites.

Le paramètre remainder n’est pas écrit dans la cellule : sa valeur par défaut est 'drop'. Une colonne qui n’est citée dans aucune des deux branches n’est donc pas transmise au modèle. Ici, X contient déjà exactement les quatre colonnes prévues. sparse_threshold=0 demande un résultat dense, c’est-à-dire un tableau numérique ordinaire ; il ne standardise pas les valeurs et ne change pas le sens des variables.

Pipeline fixe l’ordre : d’abord preparation, puis regression. LinearRegression apprend des coefficients qui combinent la surface, la date et les indicateurs pour estimer directement valeur_fonciere en euros. Le modèle ne prédit pas d’abord le prix au m². Les coefficients décrivent une relation statistique dans les données ; ils ne démontrent pas un effet causal de chaque caractéristique.

clone(modele_definition) crée un modèle neuf avec les mêmes réglages, sans paramètres déjà appris. Lors de modele_test.fit(X_train, y_train), le pipeline apprend les catégories de l’encodeur sur X_train et transforme ces entrées, puis la régression apprend ses coefficients à partir de ces entrées transformées et de y_train. C’est le rôle combiné de fit et de transform, géré ici automatiquement pour les étapes intermédiaires.

Lors de predict(X_test), l’encodeur utilise les catégories déjà apprises pour transformer X_test ; il ne les réapprend pas. La régression produit alors une estimation par ligne de test. Appeler fit sur le test détruirait cette séparation. On n’appelle pas fit_predict pour cette régression : LinearRegression s’utilise ici avec fit puis predict. Vous rencontrerez fit_predict plus tard pour K-means, où l’on apprend des groupes et attribue un groupe aux mêmes observations.

handle_unknown='error' fait arrêter le pipeline si une catégorie imprévue apparaît. Ce choix oblige à examiner le problème au lieu d’inventer silencieusement un encodage. Le prix au m² observé reste exclu : comme il est calculé à partir du prix total à prédire, le fournir au modèle lui donnerait déjà une partie de la réponse. C’est une fuite de la cible.

### Fonctions et méthodes

- `ColumnTransformer` : Applique des préparations différentes aux colonnes numériques et aux catégories, puis combine les résultats.
- `OneHotEncoder` : Transforme des catégories en indicateurs numériques 0/1 ; drop et handle_unknown fixent la référence et le traitement des catégories nouvelles.
- `remainder et sparse_threshold` : remainder='drop' est implicite et retire les colonnes non sélectionnées ; sparse_threshold=0 produit un tableau dense.
- `Pipeline` : Enchaîne les transformations et le modèle, en gardant la même préparation à l’apprentissage et à la prédiction.
- `fit / transform / predict` : fit apprend des paramètres ; transform applique une préparation ; predict calcule les réponses avec le modèle appris.
- `LinearRegression et clone` : La première apprend une combinaison linéaire pour la valeur totale ; le second crée un nouvel estimateur avec les mêmes réglages.

### Résultat attendu

Le modèle utilise 22 variables après encodage : deux numériques, 19 indicateurs de code postal et un indicateur de type. Les catégories de référence sont 75001 et Appartement. Aucune prédiction du test n’est nulle ou négative dans cette exécution.

### À retenir

- Les catégories sont des étiquettes : on les encode sans leur inventer un ordre quantitatif.
- fit apprend ; transform applique ; predict estime. Le pipeline organise ces étapes sans réapprendre sur le test.
- La cible est un montant total en euros ; le prix au m² observé ne doit pas devenir une entrée.

### Vérifier par vous-même

- [ ] Retrouver 22 variables après encodage et les références affichées par la cellule.
- [ ] Lire les deux appels dans l’ordre : fit sur X_train/y_train, puis predict sur X_test.
- [ ] Vérifier que les branches du ColumnTransformer citent uniquement les quatre entrées décidées en 2.1.

### Question minute

Pourquoi la préparation doit-elle apprendre sur X_train, même si elle ne fait « que » encoder des catégories ?

## 2.3 — Mesurer l’erreur sans confondre pourcentage, euros et biais

Repères : C18.

### Objectif

Donner un sens différent à MAPE, MAE, RMSE, R² et biais, puis lire les résultats réels sans en faire une garantie.

### Code à repérer

```python
        'MAPE (%)': 100 * mean_absolute_percentage_error(reel, predit),
        'MAE (€)': mean_absolute_error(reel, predit),
        'RMSE (€)': np.sqrt(mean_squared_error(reel, predit)),
        'R²': r2_score(reel, predit),
        'Biais relatif (%)': 100 * np.mean((predit - reel) / reel),
```

```python
reference_mediane = DummyRegressor(strategy='median').fit(X_train, y_train)
metriques_test = mesurer_regression(y_test, prediction_test)
metriques_naives = mesurer_regression(y_test, reference_mediane.predict(X_test))
```

```python
diagnostic_test = X_test.copy()
diagnostic_test['valeur_reelle'] = y_test
diagnostic_test['valeur_predite'] = prediction_test
diagnostic_test['erreur_absolue_euros'] = np.abs(prediction_test - y_test)
diagnostic_test['erreur_absolue_pct'] = 100 * diagnostic_test['erreur_absolue_euros'] / y_test
```

### Lecture pas à pas

Les premières lignes montrées sont un extrait du dictionnaire renvoyé par mesurer_regression : chaque clé est le nom d’un indicateur et chaque valeur est son calcul. La fonction reçoit reel et predit dans le même ordre de biens et les convertit en tableaux NumPy. Les indicateurs portent ensuite sur toutes les lignes du test. Les prix réels sont strictement positifs, ce qui est nécessaire pour interpréter les divisions par reel.

La MAPE calcule, pour chaque bien, abs(prédit − réel) / réel, puis fait la moyenne. La fonction scikit-learn renvoie une proportion ; le code multiplie par 100 pour obtenir des pourcentages. Chaque bien compte autant dans cette moyenne, quelle que soit sa valeur totale. Une MAPE de 9,141018 % n’est ni un taux de biens correctement classés, ni une précision de 90,858982 %, ni une promesse d’erreur maximale de 9,14 %.

Exercice pédagogique, distinct des résultats du notebook : supposons deux prix réels de 100 000 € et 200 000 €, avec des prédictions de 110 000 € et 180 000 €. Les erreurs relatives signées sont +10 % et −10 %. La MAPE vaut (10 % + 10 %) / 2 = 10 % : les erreurs ne s’annulent pas grâce à la valeur absolue. Le biais relatif moyen vaut (+10 % − 10 %) / 2 = 0 %. Cet exemple montre qu’un biais nul peut coexister avec des erreurs importantes.

La MAE exprime la moyenne des erreurs absolues en euros : c’est l’ordre de grandeur monétaire moyen de l’écart. La RMSE élève les erreurs au carré avant leur moyenne, puis prend la racine carrée ; elle reste en euros et donne davantage de poids aux grandes erreurs. Un écart important entre RMSE et MAE invite à examiner les biens dont les erreurs sont les plus fortes.

R² compare la somme des erreurs au carré à celle d’une prédiction constante égale à la moyenne des valeurs réelles du jeu évalué. Il vaut 1 pour des prédictions parfaites et peut être négatif. R² = 0,980032 ne signifie pas 98 % de biens bien estimés : il résume une réduction d’erreur quadratique sur ce test, par rapport à cette référence. Il ne remplace pas les erreurs en euros et en pourcentage.

Le biais relatif moyen garde le signe de l’erreur. Une valeur positive signifie que les estimations sont en moyenne trop hautes en pourcentage du prix réel. Ce biais est la moyenne de rapports individuels ; ce n’est pas le rapport entre la somme des erreurs et la somme des prix. Des surestimations et sous-estimations peuvent s’y compenser.

DummyRegressor(strategy='median') apprend la médiane de y_train, puis prédit ce même montant pour tous les biens de test : c’est un point de comparaison simple. Le tableau compare cette référence à la régression. diagnostic_test conserve ensuite, pour chaque ligne de X_test, le vrai prix, la prédiction et les deux erreurs absolues. La série y_test s’aligne sur les index du DataFrame ; le tableau de prédictions conserve l’ordre de X_test. Ce tableau permettra de rechercher quels biens ou quels types sont moins bien estimés.

### Fonctions et méthodes

- `mean_absolute_percentage_error` : Moyenne des erreurs absolues divisées par les valeurs réelles ; multiplier par 100 pour lire un pourcentage.
- `mean_absolute_error` : Moyenne des distances entre prix réel et prix prédit, en euros.
- `mean_squared_error et np.sqrt` : Calculent la RMSE : racine de la moyenne des erreurs au carré, en euros.
- `r2_score` : Compare les erreurs quadratiques à une référence constante ; ce score n’est pas un taux de réussite.
- `np.mean et np.abs` : Calculent une moyenne et retirent le signe des écarts lorsque l’on veut mesurer leur amplitude.
- `DummyRegressor` : Fournit une référence naïve, ici la médiane apprise uniquement sur y_train.

### Résultat attendu

Test aléatoire : MAPE 9,141018 %, MAE 33 802,85 €, RMSE 71 188,30 €, R² 0,980032 et biais relatif moyen +0,288186 %. Le diagnostic par type montre 8 032 appartements et 608 locaux dans le test, avec des erreurs différentes selon le type.

### À retenir

- MAPE et biais s’expriment en pourcentage, MAE et RMSE en euros ; R² n’a pas d’unité.
- La MAPE mesure l’amplitude des erreurs ; le biais mesure leur direction moyenne.
- Une moyenne d’erreur ne donne ni un maximum d’erreur individuelle ni un intervalle de confiance du portefeuille.

### Vérifier par vous-même

- [ ] Retrouver la multiplication par 100 devant la MAPE et le biais, mais pas devant la MAE ou R².
- [ ] Vérifier que mesurer_regression compare y_test à prediction_test, jamais à y_train.
- [ ] Comparer les erreurs par type plutôt que supposer que la moyenne globale décrit aussi bien chaque catégorie.

### Question minute

Une MAPE de 9,14 % signifie-t-elle que 90,86 % des biens sont correctement estimés ?

## 2.4 — Voir où le modèle se trompe, au-delà d’une moyenne

Repères : C19.

### Objectif

Comprendre le nuage réel/prédit et la distribution des erreurs, sans confondre leurs axes ou leurs unités.

### Code à repérer

```python
minimum = min(y_test.min(), prediction_test.min())
maximum = max(y_test.max(), prediction_test.max())
ax.plot([minimum, maximum], [minimum, maximum], '--', color=GRIS, label='Prédiction exacte')
ax.set(title='Test de 33 % — valeurs réelles et prédites',
       xlabel='Valeur réelle (€ ; échelle logarithmique)',
       ylabel='Valeur prédite (€ ; échelle logarithmique)', xscale='log', yscale='log')
legende_figure(fig, ncol=2)
terminer_figure(fig, '07a_valeurs_reelles_predites')
```

```python
fig, ax = plt.subplots()
ax.hist(diagnostic_test['erreur_absolue_pct'], bins=35, color=BLEU, edgecolor='white')
ax.axvline(metriques_test['MAPE (%)'], color=ORANGE, linestyle='--', linewidth=2,
           label=f'MAPE : {fr(metriques_test["MAPE (%)"], 2)} %')
ax.set(title='Test de 33 % — distribution des erreurs relatives',
       xlabel='Erreur absolue relative (%)', ylabel='Nombre de biens')
legende_figure(fig, ncol=1)
terminer_figure(fig, '07b_distribution_erreurs')
```

### Lecture pas à pas

Le premier graphique place la valeur réelle en abscisse, donc sur l’axe horizontal, et la valeur prédite en ordonnée, sur l’axe vertical. Chaque point représente un bien du test. Les marqueurs et les couleurs distinguent appartements et locaux ; ce sont des groupes de diagnostic, pas deux régressions séparées.

La ligne diagonale est construite avec les mêmes coordonnées horizontales et verticales : [minimum, maximum] sur les deux axes. Elle représente y = x, c’est-à-dire une prédiction exactement égale au vrai prix. Un point au-dessus indique une surestimation ; un point en dessous, une sous-estimation. La distance visuelle à cette diagonale aide à repérer des cas à examiner, mais ne remplace pas le calcul numérique de l’erreur.

Les deux axes sont logarithmiques. Cette échelle rend visibles dans le même graphique des biens de valeurs très différentes : des distances identiques correspondent à des rapports identiques, et non à des écarts identiques en euros. L’affichage en logarithme ne signifie pas que la régression a été entraînée sur le logarithme des prix : la cible reste bien la valeur foncière totale en euros. Des valeurs nulles ou négatives seraient incompatibles avec cet affichage ; les prédictions ont été contrôlées en amont.

Le second graphique répond à une autre question : combien de biens présentent une erreur relative faible ou élevée ? hist répartit les erreurs absolues en pourcentage dans 35 classes, ou intervalles. La hauteur d’une barre est un nombre de biens, pas leur prix. La ligne verticale axvline repère la moyenne de ces erreurs, donc la MAPE du test.

La médiane affichée sous les figures est le niveau en dessous duquel se trouve au moins la moitié des erreurs observées. Le quantile 0.9, ou 90e percentile, est le seuil auquel au moins 90 % des erreurs du test sont inférieures ou égales. Ces statistiques complètent la moyenne lorsque quelques grosses erreurs la tirent vers le haut. Elles décrivent le test déjà observé ; elles ne constituent pas une garantie pour 90 % du portefeuille futur.

legende_figure réserve une zone pour la légende et terminer_figure enregistre l’image, l’affiche puis ferme la figure. Ces fonctions concernent la présentation. Modifier une couleur, une taille de figure ou le nombre de classes de l’histogramme ne réentraîne pas la régression et ne change pas les prédictions.

### Fonctions et méthodes

- `ax.scatter` : Dessine un point par bien pour comparer son prix réel et sa prédiction.
- `ax.plot` : Trace ici la diagonale de prédiction exacte, où valeur réelle = valeur prédite.
- `xscale='log' et yscale='log'` : Changent l’échelle d’affichage des axes ; ne changent pas la cible utilisée pour entraîner le modèle.
- `ax.hist et ax.axvline` : Comptent les erreurs dans des intervalles puis ajoutent un repère vertical à la MAPE.
- `median() et quantile(.9)` : Résument le milieu de la distribution et son seuil de 90 %, sur le test observé.
- `legende_figure et terminer_figure` : Organisent la lisibilité et enregistrent les graphiques sans modifier les calculs.

### Résultat attendu

Deux images sont produites : 07a_valeurs_reelles_predites.png et 07b_distribution_erreurs.png. La première situe les surestimations et sous-estimations ; la seconde montre la dispersion des erreurs autour d’une MAPE de 9,141018 %.

### À retenir

- Au-dessus de la diagonale réel/prédit : prix surestimé ; en dessous : prix sous-estimé.
- L’histogramme présente des erreurs en pourcentage, pas la distribution des prix.
- Les quantiles du test sont descriptifs ; ils ne sont pas des intervalles de prédiction pour 2022.

### Vérifier par vous-même

- [ ] Lire les noms et unités des axes avant d’interpréter les points ou les barres.
- [ ] Retrouver les deux groupes dans la légende et la diagonale « Prédiction exacte ».
- [ ] Contrôler que la ligne verticale de l’histogramme est étiquetée avec la même MAPE que le tableau de 2.3.

### Question minute

Si un point est au-dessus de la diagonale du premier graphique, le modèle a-t-il surestimé ou sous-estimé le bien ?

## 2.5 — Tester le futur avec une année laissée après l’apprentissage

Repères : C20.

### Objectif

Comprendre pourquoi le contrôle 2017–2020 vers 2021 est plus proche de l’usage de prévision que le tirage aléatoire.

### Code à repérer

```python
masque_avant_2021 = base_modele['date_mutation'].lt('2021-01-01')
modele_chronologique = clone(modele_definition)
modele_chronologique.fit(X.loc[masque_avant_2021], y.loc[masque_avant_2021])
prediction_2021 = modele_chronologique.predict(X.loc[~masque_avant_2021])
metriques_2021 = mesurer_regression(y.loc[~masque_avant_2021], prediction_2021)
```

```python
afficher_tableau(
    pd.DataFrame([metriques_test, metriques_2021], index=['Test aléatoire 33 %', 'Test chronologique 2021']),
    'Régression — comparaison des deux évaluations', formats={'R²': lambda valeur: fr(valeur, 3)},
)
print('Apprentissage chronologique :', int(masque_avant_2021.sum()), 'biens ; test 2021 :', int((~masque_avant_2021).sum()), 'biens.')
```

### Lecture pas à pas

Le masque masque_avant_2021 est une Series de vrai/faux alignée sur base_modele. .lt('2021-01-01') signifie « strictement avant le 1er janvier 2021 ». Les lignes vraies appartiennent à 2017–2020 ; ~masque_avant_2021 sélectionne les autres lignes, ici toute l’année 2021 puisque l’historique a déjà été contrôlé. X et y portent les mêmes index : le même masque s’applique aux caractéristiques et aux prix.

Un nouveau clone du pipeline est créé. Il apprend seulement sur 2017–2020 : les catégories de l’encodeur et les coefficients de la régression sont ajustés sur cette période, sans reprendre l’apprentissage du modèle de test aléatoire. predict est ensuite appelé sur les entrées de 2021, puis mesurer_regression confronte ces prédictions aux prix réels de 2021.

Ce contrôle change la question posée au modèle. Dans le tirage aléatoire, les exemples d’apprentissage et de test proviennent des mêmes années : l’apprentissage peut déjà contenir des ventes de la période évaluée. Ici, le modèle doit prévoir une année située après toutes ses observations d’apprentissage. C’est plus proche de l’estimation demandée au 31/12/2022, même si aucun prix réel de 2022 n’est fourni pour mesurer cette dernière erreur.

La MAPE passe de 9,141018 % sur le test aléatoire à 13,617991 % sur 2021. Le biais relatif moyen atteint +12,812944 % : les prix prédits sont en moyenne trop hauts en pourcentage des prix réels. Le signe + indique la direction de l’erreur ; il ne s’agit pas d’un complément à 100 %, ni de la même quantité que la MAPE. Une tendance linéaire apprise avant 2021 ne reproduit pas complètement le tassement de cette année.

Le tableau compare deux évaluations du même type de modèle, chacune sur son propre jeu tenu à l’écart. Il ne faut pas présenter le meilleur score comme une précision garantie pour l’avenir. Il ne faut pas non plus soustraire automatiquement 12,812944 % au portefeuille ou appliquer ±13,617991 % autour de son total : ces moyennes d’erreurs individuelles de 2021 ne définissent ni un facteur de correction validé pour 2022, ni un intervalle de confiance du total.

Une fois l’évaluation terminée et la méthode fixée, l’étape 3.2 réentraînera un modèle final sur toutes les observations historiques distinctes de 2017–2021. C’est permis pour produire l’estimation finale. Les scores de cette cellule restent toutefois ceux du modèle évalué en apprenant sur 2017–2020 ; ils ne deviennent pas un score d’évaluation indépendant du modèle final réentraîné.

### Fonctions et méthodes

- `.lt('2021-01-01') et ~` : Construisent les sélections chronologiques : avant 2021, puis leur complément.
- `.loc[masque]` : Sélectionne les mêmes lignes datées dans X et dans y grâce aux index conservés.
- `clone puis fit` : Créent un pipeline neuf et l’entraînent uniquement sur la période passée.
- `predict puis mesurer_regression` : Prévoient les prix de 2021, puis mesurent leurs écarts aux prix réellement connus.
- `afficher_tableau` : Présente côte à côte les résultats aléatoires et chronologiques, sans les confondre.

### Résultat attendu

21 112 lignes servent à apprendre sur 2017–2020 ; 5 068 servent au test 2021. Résultats chronologiques : MAPE 13,617991 %, biais relatif moyen +12,812944 %, MAE 51 997,86 €, RMSE 103 368,02 € et R² 0,970037.

### À retenir

- Une évaluation aléatoire et une évaluation dans le temps répondent à des questions différentes.
- Le biais positif du test 2021 signale une surestimation moyenne à communiquer avec la prévision.
- Réentraîner ensuite sur tout l’historique améliore l’utilisation des données disponibles ; cela ne crée pas une validation sur 2022.

### Vérifier par vous-même

- [ ] Contrôler les bornes : l’apprentissage est strictement avant le 01/01/2021 et le test porte sur 2021.
- [ ] Retrouver 21 112 lignes d’apprentissage et 5 068 lignes de test.
- [ ] Lire ensemble MAPE 13,617991 % et biais +12,812944 %, puis conserver leur distinction dans le commentaire.

### Question minute

Pourquoi le score aléatoire de 9,14 % ne suffit-il pas à annoncer la précision attendue en 2022 ?

## 3.1 — Préparer les actifs à estimer avec les mêmes définitions

Repères : C21.

### Objectif

Contrôler les 275 lignes et comprendre le choix de surface, la date d’estimation et la convention de segments.

### Code à repérer

```python
portefeuille_brut = pd.read_excel(DATA_DIR / FICHIERS['portefeuille'], engine='openpyxl')
verifier_colonnes(portefeuille_brut, [
    'surface_reelle_bati', 'code_postal', 'code_type_local', 'type_local',
    'adresse_numero', 'adresse_nom_voie',
], 'Portefeuille')
nb_identiques_portefeuille = int(portefeuille_brut.duplicated().sum())
portefeuille = portefeuille_brut.copy()
```

```python
portefeuille['code_postal'] = portefeuille['code_postal'].astype(int).astype(str)
portefeuille['code_type_local'] = portefeuille['code_type_local'].astype(int)
portefeuille['surface_reelle'] = portefeuille['surface_reelle_bati']
portefeuille['date_mutation'] = DATE_ESTIMATION
portefeuille['date_annees'] = (DATE_ESTIMATION - DATE_ORIGINE).days / 365.25
portefeuille.insert(0, 'id_bien', np.arange(1, len(portefeuille) + 1))
portefeuille['segment_conventionnel'] = portefeuille['code_type_local'].map(SEGMENTS)
print(f'{len(portefeuille)} biens ; {nb_identiques_portefeuille} répétitions exactes signalées et conservées.')
```

### Lecture pas à pas

Le portefeuille est un autre fichier que l’historique. Il contient les biens à estimer, sans fournir leurs prix réels au 31/12/2022. read_excel le lit dans portefeuille_brut, puis verifier_colonnes impose les colonnes nécessaires. La copie portefeuille est la table de travail ; le fichier source n’est pas modifié. Les conversions et contrôles de la cellule arrêtent le calcul si une surface est manquante, non finie ou non positive, si un type est inconnu, si son libellé ne correspond pas au code, ou si le code postal est hors Paris 1 à 20.

La cellule compte deux répétitions exactes et les conserve. Sans identifiant cadastral ou confirmation du gestionnaire, deux lignes identiques ne prouvent pas qu’un même actif a été inscrit deux fois. Il faut donc les signaler et les faire vérifier, plutôt que les supprimer automatiquement et diminuer le total. Les 275 lignes seront toutes estimées ; ce nombre n’est pas une certification de 275 actifs distincts.

Le point essentiel est portefeuille['surface_reelle'] = portefeuille['surface_reelle_bati']. Le modèle a été entraîné avec la surface réelle. On donne donc à son entrée homonyme la surface réelle bâtie du portefeuille. La surface Carrez répond à une autre définition et ne peut pas lui être substituée sans revoir le modèle. Dans la première ligne réellement affichée, la surface réelle vaut 25 m² et Carrez 16,41 m² : ce ne sont pas deux écritures du même nombre.

Les codes postaux sont convertis en chaînes de caractères comme dans l’apprentissage ; les codes de type restent des entiers servant aux correspondances. DATE_ESTIMATION vaut le 31 décembre 2022. La colonne date_mutation du portefeuille reçoit cette date de calcul pour satisfaire le schéma du modèle : cela ne décrit pas une mutation réellement observée. date_annees exprime ensuite cette date dans la même unité temporelle que pendant l’apprentissage.

insert ajoute id_bien de 1 à 275. Cet identifiant repère la ligne du classeur, pas une parcelle ou un actif juridiquement unique. map(SEGMENTS) associe le code 2 à Particuliers et le code 4 à Corporate. C’est une convention de travail basée sur le type, car le fichier ne possède pas de colonne de branche commerciale. La préparation ne prouve donc pas que l’entreprise rattache effectivement chaque appartement ou local à ces segments.

### Fonctions et méthodes

- `pd.read_excel et verifier_colonnes` : Lisent le fichier et vérifient la présence des champs attendus avant les calculs.
- `pd.to_numeric et np.isfinite` : Convertissent les données attendues numériques puis repèrent les valeurs manquantes ou non finies.
- `duplicated()` : Signale les répétitions exactes, sans les supprimer dans cette cellule.
- `astype(int).astype(str)` : Harmonise le format du code postal avec celui utilisé par le modèle.
- `np.arange et insert` : Créent puis ajoutent un numéro de ligne de 1 à 275.
- `map(SEGMENTS)` : Applique explicitement la convention type de bien vers segment commercial supposé.

### Résultat attendu

275 lignes de portefeuille sont préparées, avec deux répétitions exactes signalées et conservées. La surface utilisée est surface_reelle_bati, la date de calcul est le 31/12/2022, et les segments restent conventionnels.

### À retenir

- Une variable doit garder la même définition et la même unité entre l’apprentissage et la prédiction.
- Surface réelle bâtie et surface Carrez ne sont pas interchangeables dans ce modèle.
- id_bien est un numéro de ligne ; les répétitions et les rattachements de segments nécessitent une confirmation métier.

### Vérifier par vous-même

- [ ] Retrouver le message « 275 biens ; 2 répétitions exactes signalées et conservées ».
- [ ] Comparer les colonnes surface_reelle et surface_carrez dans l’aperçu : comprendre pourquoi seule la première entre dans VARIABLES.
- [ ] Vérifier que la date d’estimation est bien le 31/12/2022 et qu’elle est présentée comme une hypothèse de valorisation.

### Question minute

Peut-on choisir la surface Carrez parce qu’elle paraît plus familière dans une annonce immobilière ?

## 3.2 — Réentraîner après l’évaluation, puis estimer chaque ligne

Repères : C22.

### Objectif

Distinguer le modèle final des modèles de test et comprendre les contrôles qui précèdent l’utilisation de ses prédictions.

### Code à repérer

```python
modele_final = clone(modele_definition)
modele_final.fit(X, y)
for colonne in VARIABLES_CATEGORIELLES:
    inconnues = set(portefeuille[colonne]) - set(X[colonne])
    if inconnues:
        raise ValueError(f'Catégories absentes de l’apprentissage pour {colonne} : {inconnues}')
```

```python
portefeuille['surface_hors_plage_historique'] = ~portefeuille['surface_reelle'].between(
    base_modele['surface_reelle'].min(), base_modele['surface_reelle'].max()
)
portefeuille['valeur_estimee_euros'] = modele_final.predict(portefeuille[VARIABLES])
if (not np.isfinite(portefeuille['valeur_estimee_euros']).all()
        or portefeuille['valeur_estimee_euros'].le(0).any()):
    raise ValueError('Une estimation est non finie ou non positive : ne pas valider la valorisation.')
portefeuille['prix_m2_estime'] = portefeuille['valeur_estimee_euros'] / portefeuille['surface_reelle']
```

### Lecture pas à pas

L’évaluation est terminée : on peut utiliser toutes les observations historiques distinctes de 2017–2021 pour produire l’estimation finale. clone(modele_definition) crée un pipeline neuf, puis fit(X, y) apprend sur les 26 180 lignes. Cette cellule ne recharge pas simplement les coefficients du test aléatoire ou du test chronologique ; elle effectue un nouvel apprentissage avec la même méthode et les mêmes réglages.

Utiliser l’ensemble de l’historique à ce stade n’est pas une fuite pour la production finale : le but n’est plus de mesurer un score sur ces lignes, mais d’exploiter les informations disponibles pour estimer le portefeuille. En revanche, on ne doit plus évaluer ce modèle sur 2021 en prétendant que 2021 est indépendant : il vient d’y apprendre. Les scores 9,141018 % et 13,617991 % restent attachés à leurs protocoles de test précédents.

Pour chaque variable catégorielle, set(portefeuille[colonne]) - set(X[colonne]) cherche les catégories du portefeuille absentes de l’historique. Une différence non vide déclenche une erreur à examiner. Le modèle ne peut pas prétendre connaître une localisation ou un type qu’il n’a jamais rencontré. La sélection portefeuille[VARIABLES] fournit ensuite exactement les mêmes noms d’entrées que pendant l’apprentissage, sans ajouter adresses, identifiants ou surface Carrez.

between(minimum, maximum) vérifie si chaque surface est comprise dans la plage historique. ~ inverse le résultat pour signaler les surfaces hors plage. Ce contrôle porte sur la plage globale, pas sur toutes les combinaisons de surface, type et arrondissement. Dans l’exécution réelle, aucune surface n’est hors de cette plage ; cela ne garantit pas pour autant la précision de chaque bien.

predict renvoie une valeur foncière totale en euros pour chaque ligne du portefeuille. Le code exige que ces valeurs soient finies et strictement positives. Il calcule ensuite prix_m2_estime en divisant la prédiction totale par la surface : ce ratio est une sortie de lecture, pas le prix au m² observé interdit comme entrée en 2.2.

La dernière vente historique date du 31/12/2021 ; la date de prévision se situe 365 jours plus tard. Le modèle extrapole donc dans le temps, même si toutes les surfaces se trouvent dans la plage connue. Le biais du contrôle 2021, les caractéristiques absentes comme l’état ou le DPE et l’absence de prix réels 2022 limitent la portée de la valorisation. Aucun intervalle de prédiction ou de confiance du portefeuille n’est calculé ici.

### Fonctions et méthodes

- `clone(modele_definition)` : Crée un nouveau pipeline avec les mêmes réglages, sans coefficients ni catégories déjà appris.
- `fit(X, y)` : Réentraîne le pipeline final sur toutes les observations historiques distinctes après l’évaluation.
- `set(...) - set(...)` : Repère les catégories du portefeuille qui n’existent pas dans l’apprentissage.
- `between et ~` : Détectent les surfaces en dehors de la plage minimale/maximale observée dans l’historique.
- `predict(portefeuille[VARIABLES])` : Estime la valeur totale de chaque ligne avec le schéma d’entrées prévu.
- `np.isfinite et .le(0)` : Empêchent de valider des estimations non finies, nulles ou négatives.

### Résultat attendu

Les 275 lignes reçoivent une estimation positive et finie. Aucune surface n’est hors de la plage historique globale ; la date est extrapolée de 365 jours. La première ligne affichée est estimée à 435 840,20 €. Le total, calculé en 3.3, atteint 169 701 260,65 €.

### À retenir

- On évalue d’abord la méthode, puis on réentraîne le modèle final sur tout l’historique distinct disponible.
- Le prix au m² estimé est dérivé du prix total prédit ; il ne sert pas d’entrée au modèle.
- Être dans la plage de surfaces connue ne supprime pas le risque d’extrapolation temporelle.

### Vérifier par vous-même

- [ ] Identifier fit(X, y), différent de fit(X_train, y_train) et du fit chronologique de 2.5.
- [ ] Retrouver zéro surface hors plage et un écart temporel de 365 jours.
- [ ] Contrôler que le tableau de sortie présente des valeurs en euros et des prix dérivés en €/m², sans valeur réelle 2022 inventée.

### Question minute

Pourquoi peut-on maintenant apprendre sur toute l’année 2021 alors qu’elle devait rester à l’écart du test chronologique ?

## 3.3 — Additionner les valeurs et comparer les segments avec prudence

Repères : C23.

### Objectif

Lire groupby/agg, les conversions en millions et les rapprochements de totaux sans confondre valeur estimée et rentabilité.

### Code à repérer

```python
valorisation_segments = portefeuille.groupby('segment_conventionnel').agg(
    nombre_biens=('id_bien', 'size'), surface_totale_m2=('surface_reelle', 'sum'),
    valeur_estimee_euros=('valeur_estimee_euros', 'sum'),
    valeur_moyenne_par_bien=('valeur_estimee_euros', 'mean'),
).reindex(['Particuliers', 'Corporate'])
valorisation_segments['valorisation_MEUR'] = valorisation_segments['valeur_estimee_euros'] / 1_000_000
total_portefeuille = portefeuille['valeur_estimee_euros'].sum()
valorisation_segments['part_valorisation_pct'] = 100 * valorisation_segments['valeur_estimee_euros'] / total_portefeuille
```

```python
assert valorisation_segments['nombre_biens'].sum() == len(portefeuille)
assert np.isclose(valorisation_segments['valeur_estimee_euros'].sum(), total_portefeuille)
```

```python
fig, ax = plt.subplots(figsize=(9.2, 4.8))
barres = ax.barh(valorisation_segments.index, valorisation_segments['valorisation_MEUR'], color=[BLEU, ORANGE])
ax.bar_label(barres, labels=[f'{fr(v, 2)} M€' for v in valorisation_segments['valorisation_MEUR']], padding=6)
ax.set_xlim(0, valorisation_segments['valorisation_MEUR'].max() * 1.22)
ax.set(title='Portefeuille — valorisation estimée au 31/12/2022', xlabel='Millions d’euros — segments définis par convention')
ax.grid(axis='y', visible=False)
terminer_figure(fig, '08_valorisation_portefeuille')
```

### Lecture pas à pas

groupby('segment_conventionnel') sépare les lignes en Particuliers et Corporate selon la convention préparée en 3.1. agg calcule ensuite plusieurs résumés. Dans nombre_biens=('id_bien', 'size'), le nom à gauche sera celui de la nouvelle colonne, id_bien indique la colonne utilisée et size compte les lignes. Les autres couples demandent la somme des surfaces, la somme des estimations et la moyenne des estimations individuelles.

reindex(['Particuliers', 'Corporate']) impose l’ordre de présentation des deux lignes. Il ne réentraîne pas le modèle et ne change pas les montants. Les sommes sont calculées à partir des estimations en euros avant de les arrondir pour l’affichage. Diviser valeur_estimee_euros par 1_000_000 produit une nouvelle colonne en M€ ; les traits de soulignement dans 1_000_000 facilitent simplement la lecture du nombre en Python.

total_portefeuille additionne les estimations des 275 lignes. La part d’un segment est sa valeur totale divisée par ce total, multipliée par 100. Ce pourcentage porte sur la valeur, pas sur le nombre de lignes ni sur la surface. Un segment comportant moins de lignes peut donc représenter davantage de valeur si ses biens sont en moyenne plus chers ou plus grands.

Les assert rapprochent les agrégats de la table détaillée : le nombre de lignes des deux segments doit faire 275 et leurs valeurs additionnées doivent retrouver le total. np.isclose compare des nombres décimaux avec une tolérance, car les calculs informatiques en virgule flottante peuvent produire d’infimes écarts. Cela ne constitue pas une tolérance d’erreur économique de la valorisation ; c’est un contrôle de cohérence arithmétique.

barh trace deux barres horizontales en millions d’euros et bar_label place les montants près des barres. La limite supérieure égale au maximum multiplié par 1.22 laisse de la place aux étiquettes ; elle ne multiplie pas les données. L’axe commence à zéro, ce qui permet de comparer honnêtement les longueurs. La couleur ne modifie pas le calcul.

Sous la convention retenue, Particuliers correspond à 154 appartements et Corporate à 121 locaux. Le corporate concentre 58,03 % de la valeur estimée, bien qu’il compte moins de lignes. idxmax renvoie le nom du segment ayant la plus grande valeur totale. Cela ne dit pas qu’il est plus rentable : loyers, charges, coûts et prix d’acquisition ne sont pas fournis. Les deux répétitions conservées et la convention de segments doivent être confirmées avant usage opérationnel.

### Fonctions et méthodes

- `groupby et agg` : Regroupent les lignes par segment puis calculent plusieurs résumés nommés.
- `size / sum / mean` : Comptent les lignes, additionnent les valeurs ou calculent leur moyenne ; ces opérations répondent à des questions différentes.
- `reindex` : Fixe ici l’ordre des deux segments dans les sorties.
- `np.isclose et assert` : Vérifient que les synthèses retrouvent les totaux détaillés malgré de minuscules écarts d’arrondi informatique.
- `barh et bar_label` : Affichent les valeurs en barres horizontales avec leurs montants.
- `idxmax` : Renvoie le nom du segment dont la valeur totale estimée est la plus élevée.

### Résultat attendu

Total au 31/12/2022 : 169 701 260,65 €, soit 169,70 M€. Particuliers : 154 lignes, 6 286 m², 71 221 764,00 € et 41,97 % de la valeur. Corporate : 121 lignes, 7 696 m², 98 479 496,65 € et 58,03 %. Les valeurs moyennes sont respectivement 462 478,99 € et 813 880,14 € par ligne.

### À retenir

- Additionner les montants en euros avant de convertir ou d’arrondir pour l’affichage.
- La part de valeur, la part du nombre de biens et la part de surface sont trois mesures différentes.
- Une valeur totale supérieure ne démontre ni une meilleure rentabilité ni l’intérêt d’un achat ou d’une vente.

### Vérifier par vous-même

- [ ] Contrôler 154 + 121 = 275 et le rapprochement des valeurs avec 169 701 260,65 €.
- [ ] Vérifier que 41,97 % + 58,03 % = 100 % à l’arrondi affiché et que les barres sont en M€.
- [ ] Lire la convention appartements = particuliers, locaux = corporate avec le résultat, et signaler les deux répétitions conservées.

### Question minute

Le corporate vaut davantage au total. Peut-on conclure qu’il rapporte davantage ?

## 4.1 — Importer et préparer les opportunités de Louise

Repères : C24.

### Objectif

Créer une base fiable de 40 biens et une seule variable de regroupement : le prix au m².

### Code à repérer

```python
echantillon_brut = pd.read_excel(DATA_DIR / FICHIERS['echantillon'], engine='openpyxl')
verifier_colonnes(echantillon_brut, ['valeur_fonciere', 'surface_reelle', 'code_postal'], 'Échantillon')
echantillon = echantillon_brut.copy()
for colonne in ['valeur_fonciere', 'surface_reelle', 'code_postal']:
    echantillon[colonne] = pd.to_numeric(echantillon[colonne], errors='coerce')
```

```python
echantillon.insert(0, 'id_opportunite', np.arange(1, len(echantillon) + 1))
echantillon['prix_m2'] = echantillon['valeur_fonciere'] / echantillon['surface_reelle']
X_kmeans = echantillon[['prix_m2']].copy()
```

### Lecture pas à pas

Un apprentissage supervisé apprend avec une réponse connue pour chaque exemple : la régression précédente disposait de la valeur foncière historique. Un apprentissage non supervisé, comme K-means ici, reçoit des caractéristiques sans réponse métier à apprendre. Il regroupe des ressemblances ; il ne connaît ni « appartement » ni « local ». Le mot classification du titre du milestone ne transforme pas ce regroupement en apprentissage supervisé.

La lecture Excel crée echantillon_brut. La copie echantillon sert au travail afin de conserver la source. Les conversions numériques avec errors="coerce" transforment les contenus illisibles en valeurs manquantes. Les contrôles suivants les détectent : np.isfinite refuse les valeurs manquantes et les infinis ; le(0) signale les valeurs nulles ou négatives. Une surface nulle empêcherait de calculer un prix au m² valide.

Le code vérifie que toutes les lignes appartiennent au seul code postal 75019. Une autre zone exigerait de revoir la comparaison historique de l’étape 4.3. Le code postal reste utile pour le contexte, mais une colonne constante ne sépare pas les 40 biens.

insert place id_opportunite au début de la table. np.arange(1, len(echantillon) + 1) produit les nombres de 1 à 40 : la borne finale est exclue, d’où le +1. Cet identifiant repère une ligne du classeur, pas une parcelle ou un actif cadastral ; changer l’ordre du fichier source peut modifier ce repère.

Le prix au m² vaut valeur_fonciere / surface_reelle. X_kmeans = echantillon[["prix_m2"]] crée un tableau à une colonne et plusieurs lignes : les doubles crochets conservent la forme 2D attendue par scikit-learn. La valeur totale et la surface servent au ratio, puis restent hors de X_kmeans. La date n’est pas présente et n’est pas inventée.

### Fonctions et méthodes

- `pd.read_excel(..., engine="openpyxl")` : Lit le classeur XLSX dans un DataFrame.
- `verifier_colonnes()` : Fonction du notebook qui arrête l’exécution si une colonne indispensable manque.
- `pd.to_numeric(..., errors="coerce")` : Convertit les nombres ; remplace une conversion impossible par une valeur manquante, ensuite contrôlée.
- `np.isfinite(), le(), all(), any()` : Vérifient les valeurs finies et positives ; all exige que tous les éléments passent, any détecte au moins une anomalie.
- `nunique()` : Compte les valeurs distinctes ; ici il doit rester un seul code postal.
- `insert(), np.arange()` : Ajoutent le numéro de ligne utilisé pour retrouver les opportunités.
- `copy()` : Crée un objet de travail distinct de l’objet source.

### Résultat attendu

40 opportunités du 19e arrondissement, sans répétition exacte observée. Aucune date ni aucun type réel n’est fourni. X_kmeans contient uniquement 40 prix au m².

### À retenir

- Une ligne = une opportunité du fichier.
- Une seule caractéristique entre dans K-means : prix_m2.
- Non supervisé signifie sans type réel utilisé à l’apprentissage.

### Vérifier par vous-même

- [ ] Lire le message « 40 opportunités, toutes dans le 19e arrondissement ».
- [ ] Vérifier les colonnes et les valeurs positives avant le ratio.
- [ ] Ne pas ajouter date_mutation ou type_local par supposition.

### Question minute

Pourquoi ne pas donner aussi le prix total et la surface à K-means ?

## 4.2 — Comprendre les deux centres et leur frontière

Repères : C25 · C26.

### Objectif

Relier le code à l’idée concrète de proximité : chaque prix est rattaché au centre le plus proche.

### Code à repérer

```python
kmeans = KMeans(n_clusters=2, n_init=20, random_state=GRAINE)
echantillon['cluster'] = kmeans.fit_predict(X_kmeans)
centres = pd.Series(kmeans.cluster_centers_.ravel(), index=range(2), name='Centre (€/m²)')
cluster_bas = int(centres.idxmin())
cluster_haut = int(centres.idxmax())
noms_groupes = {cluster_bas: 'Prix au m² bas', cluster_haut: 'Prix au m² haut'}
echantillon['groupe_prix'] = echantillon['cluster'].map(noms_groupes)
```

```python
score_silhouette = silhouette_score(X_kmeans, echantillon['cluster'])
seuil_kmeans = centres.mean()
display(resume_clusters)
print(f'Silhouette : {score_silhouette:.3f} ; frontière entre les deux centres : {fr(seuil_kmeans)} €/m².')
```

```python
for cluster, couleur, marqueur in [(cluster_bas, BLEU, 'o'), (cluster_haut, ORANGE, '^')]:
    part = echantillon.loc[echantillon['cluster'].eq(cluster)]
    ax.scatter(part['id_opportunite'], part['prix_m2'], color=couleur, marker=marqueur,
               s=40, label=f'{noms_groupes[cluster]} (n = {len(part)})')
    ax.axhline(centres.loc[cluster], color=couleur, linestyle=':', linewidth=1.5)
ax.axhline(seuil_kmeans, color=GRIS, linestyle='--', label='Frontière K-means')
```

### Lecture pas à pas

KMeans(n_clusters=2) impose la recherche de deux groupes. Cela ne découvre pas qu’il existe exactement deux natures de biens. L’algorithme cherche des centres qui réduisent la somme des distances au carré entre chaque point et son centre. Avec une seule variable, les points sont simplement des positions sur une ligne graduée en €/m².

L’idée de calcul est la suivante : proposer deux centres, affecter chaque prix au centre le plus proche, recalculer chaque centre comme moyenne des prix de son groupe, puis répéter jusqu’à stabilisation. n_init=20 essaie plusieurs départs et garde la solution retenue selon le critère de K-means ; ce paramètre ne crée pas 20 groupes. random_state=GRAINE rend ces départs reproductibles.

fit_predict ajuste les centres et renvoie un numéro de groupe pour chaque bien. Ces numéros 0 et 1 sont arbitraires : une autre exécution ou un autre jeu de données peut inverser les numéros sans changer le sens de la partition. idxmin et idxmax identifient donc le centre bas et le centre haut à partir de leurs valeurs, puis map associe des noms compréhensibles.

Les centres calculés sont environ 7 408,775 et 9 806,925 €/m². En une dimension, la frontière entre deux centres est leur milieu : (7 408,775 + 9 806,925) / 2 = 8 607,850 €/m² environ. Sous ce seuil, le centre bas est le plus proche ; au-dessus, le centre haut est le plus proche. À égalité exacte, les distances sont les mêmes et l’algorithme applique sa convention d’affectation.

Exemple pédagogique fictif : un bien à 8 000 €/m² est à environ 591 €/m² du centre bas et 1 807 €/m² du centre haut. Il rejoint donc le groupe bas. Cela ne permet toujours pas de dire que son type réel est appartement : l’affectation concerne le groupe de prix.

Le résumé groupby/agg calcule effectif, minimum, moyenne et maximum de chaque groupe, puis sort_values place le groupe bas en premier. Chaque groupe contient 20 biens ; ces effectifs sont constatés, pas imposés par n_clusters=2. Les prix pourraient former des groupes de tailles très différentes dans un autre fichier.

La silhouette compare la proximité d’un point aux autres points de son groupe et à ceux du groupe voisin. Pour un point, s = (b − a) / max(a, b), où a est sa distance moyenne interne et b la distance moyenne au groupe voisin. Le score varie entre −1 et 1 : proche de 1, les groupes sont bien séparés ; proche de 0, la frontière est floue ; négatif, certains points sont plus proches d’un autre groupe. Le score global de 0,909 décrit ici une nette séparation des prix. Il ne signifie jamais 90,9 % de types correctement identifiés.

Dans C26, le nuage affiche un point par identifiant de ligne. Les couleurs ET les formes distinguent les groupes ; les lignes pointillées repèrent les centres, la ligne discontinue la frontière. L’axe horizontal ne représente ni une date ni une surface. Une standardisation affine d’une seule variable ne change pas la partition recherchée ; conserver les €/m² rend les centres directement lisibles.

### Fonctions et méthodes

- `KMeans(n_clusters=2, n_init=20, random_state=GRAINE)` : Configure deux groupes, plusieurs départs et une graine reproductible.
- `fit_predict()` : Apprend les centres et fournit le numéro de groupe de chaque observation.
- `cluster_centers_.ravel()` : Récupère les centres appris et transforme leur tableau en une suite de deux nombres.
- `idxmin(), idxmax(), map()` : Trouvent le groupe bas/haut et associent des noms sans dépendre du numéro 0 ou 1.
- `groupby().agg()` : Résume les observations de chaque groupe.
- `silhouette_score()` : Mesure la cohésion et la séparation des groupes, sans types réels.
- `mean()` : Calcule ici le milieu des deux centres.
- `ax.scatter(), ax.axhline()` : Dessinent les observations et les lignes de repère.

### Résultat attendu

Deux groupes de 20 biens. Centres : 7 408,775 et 9 806,925 €/m² environ ; frontière : 8 607,850 €/m² environ ; silhouette : 0,909.

### À retenir

- Deux centres décrivent deux niveaux de prix.
- 0 et 1 ne sont pas des codes métier.
- La silhouette mesure la séparation, pas l’exactitude.

### Vérifier par vous-même

- [ ] Retrouver 20 + 20 = 40 dans le résumé.
- [ ] Recalculer le milieu des centres sur une calculatrice.
- [ ] Distinguer le paramètre n_clusters=2 du résultat effectif=20 par groupe.
- [ ] Lire correctement les axes du graphique C26.

### Question minute

Un score de silhouette de 0,909 prouve-t-il que 90,9 % des biens sont bien classés ?

## 4.3 — Passer d’un groupe de prix à un type supposé

Repères : C27.

### Objectif

Comprendre pourquoi le notebook propose « appartement » et « local », et pourquoi cette proposition reste fragile.

### Code à repérer

```python
reference_19e = historique.loc[
    historique['code_postal'].eq('75019') & historique['annee'].eq(ANNEE_ECHANTILLON)
]
resume_reference_19e = reference_19e.groupby('code_type_local').agg(
    effectif=('prix_m2', 'size'), moyenne_euros_m2=('prix_m2', 'mean'),
    mediane_euros_m2=('prix_m2', 'median'), minimum_euros_m2=('prix_m2', 'min'),
    maximum_euros_m2=('prix_m2', 'max'),
)
```

```python
ordre_types = resume_reference_19e['moyenne_euros_m2'].sort_values().index.tolist()
if set(ordre_types) != {2, 4}:
    raise ValueError('Les deux types ne sont pas représentés dans la référence locale.')
correspondance_types = {cluster_bas: ordre_types[0], cluster_haut: ordre_types[1]}
echantillon['code_type_estime'] = echantillon['cluster'].map(correspondance_types)
echantillon['type_estime'] = echantillon['code_type_estime'].map(LIBELLES_TYPES)
echantillon['statut'] = 'Hypothèse à confirmer'
```

```python
centre_appartement = centres.loc[[c for c, t in correspondance_types.items() if t == 2][0]]
ecart_centre_reference = 100 * (centre_appartement / resume_reference_19e.loc[2, 'moyenne_euros_m2'] - 1)
```

### Lecture pas à pas

Le regroupement précédent ne possède aucun nom de type. C27 cherche un repère dans l’historique : uniquement le code postal 75019 et l’année ANNEE_ECHANTILLON. Le & signifie que les deux conditions doivent être vraies sur la même ligne. La sélection .loc conserve ces ventes de référence.

ANNEE_ECHANTILLON vaut 2021 dans les paramètres. C’est une année de référence retenue dans le notebook, pas une date retrouvée dans le classeur de Louise : ce classeur n’a pas de date. Il faut donc présenter la comparaison comme une hypothèse temporelle, à confirmer avec Louise.

Les types des ventes historiques, eux, sont connus : code 2 pour les appartements et code 4 pour les locaux industriels, commerciaux ou assimilés. groupby puis agg résume les prix au m² par type. Dans le 19e en 2021, la référence contient 230 appartements et seulement 11 locaux. Leurs prix moyens sont environ 8 828,586 et 9 737,620 €/m².

sort_values classe les moyennes historiques par ordre croissant. Puis correspondance_types associe le groupe bas au type dont la moyenne historique est la plus basse, et le groupe haut au type dont la moyenne est la plus haute. Ici cela propose bas → appartement, haut → local. Le contrôle set(... ) == {2, 4} exige simplement que les deux types soient disponibles pour cette comparaison.

Une première map crée code_type_estime ; une deuxième ajoute le libellé de ce code. Le mot estime et le statut « Hypothèse à confirmer » sont essentiels : le notebook a nommé des groupes à partir d’un repère, sans observer le type réel des 40 opportunités.

Le centre bas, 7 408,775 €/m², se situe environ 16,1 % sous la moyenne des appartements de référence : 100 × (centre / référence − 1). Cet écart fragilise l’interprétation. Période différente, caractéristiques particulières ou autre contenu du fichier pourraient intervenir, mais les données ne permettent pas d’affirmer l’une de ces explications. La référence des locaux ne compte que 11 observations, ce qui invite aussi à rester prudent.

### Fonctions et méthodes

- `loc et eq()` : Sélectionnent les lignes répondant aux conditions du 19e et de l’année de référence.
- `groupby("code_type_local").agg()` : Calcule les effectifs et les repères de prix de chaque type connu dans l’historique.
- `sort_values().index.tolist()` : Récupère les codes des types classés du prix moyen le plus bas au plus haut.
- `set()` : Contrôle la présence des deux types attendus sans dépendre de leur ordre.
- `map()` : Traduit le numéro de groupe en code de type supposé, puis en libellé.
- `loc[...]` : Retrouve la moyenne historique ou le centre nécessaire à la comparaison.

### Résultat attendu

Proposition provisoire : 20 appartements supposés et 20 locaux supposés. Référence historique : 230 appartements et 11 locaux du 19e en 2021. Le centre du groupe bas est 16,1 % sous la moyenne des appartements de référence.

### À retenir

- Groupe calculé et type réel sont deux notions différentes.
- Le nom du groupe est déduit de l’ordre des prix moyens locaux.
- La référence 2021 et l’étiquette proposée doivent être confirmées.

### Vérifier par vous-même

- [ ] Contrôler que la référence porte bien sur le 19e.
- [ ] Retrouver les effectifs 230 et 11 avant de généraliser.
- [ ] Présenter −16,1 % comme un écart au repère, pas comme une décote immobilière démontrée.
- [ ] Conserver le statut « Hypothèse à confirmer ».

### Question minute

Pourquoi ne pas appeler directement le cluster 0 « appartement » ?

## 4.4 — Lire le classement provisoire et retrouver chaque ligne

Repères : C28.

### Objectif

Produire une liste exploitable pour la discussion avec Louise, sans transformer une hypothèse en vérité.

### Code à repérer

```python
classement_affiche = echantillon[[
    'id_opportunite', 'surface_reelle', 'valeur_fonciere',
    'prix_m2', 'groupe_prix', 'type_estime',
]].sort_values('id_opportunite').copy()
```

```python
for debut in (0, 20):
    afficher_tableau(
        classement_affiche.iloc[debut:debut + 20],
        f'Louise — biens {debut + 1} à {debut + 20} du 19e ; types à confirmer',
        masquer_index=True,
    )
```

### Lecture pas à pas

value_counts compte les types proposés et produit un résumé de 20 appartements supposés et 20 locaux supposés. L’intitulé « Type proposé, à confirmer » empêche de confondre ce tableau avec un inventaire des types réels.

classement_affiche sélectionne les colonnes utiles : identifiant, surface, valeur totale, prix au m², groupe de prix et type proposé. sort_values("id_opportunite") remet les biens dans l’ordre des identifiants du fichier ; ce n’est pas un classement d’attractivité ou un ordre de prix.

copy crée une table d’affichage. replace raccourcit le long libellé des locaux et rename traduit les noms techniques en en-têtes français avec unités. Ces opérations de présentation ne réentraînent pas K-means et ne modifient pas le sens des résultats.

La boucle for debut in (0, 20) affiche deux tableaux de 20 lignes. iloc sélectionne des positions : [0:20] contient les positions 0 à 19, puis [20:40] les positions 20 à 39, car la borne de fin est exclue. Les identifiants visibles vont bien de 1 à 40.

Pour préparer une validation, transmettre à Louise l’identifiant avec la proposition et lui demander le type réel indépendamment de cette proposition. L’identifiant doit rester attaché à la même ligne source ; il permettra l’appariement contrôlé de l’étape 4.5.

### Fonctions et méthodes

- `value_counts()` : Compte les lignes de chaque type proposé.
- `sort_values("id_opportunite")` : Replace les observations dans l’ordre des identifiants.
- `replace(), rename()` : Simplifient les libellés et ajoutent des en-têtes lisibles ; elles ne changent pas le modèle.
- `iloc[début:fin]` : Sélectionne un intervalle de positions avec une borne finale exclue.
- `afficher_tableau()` : Fonction du notebook qui met en forme les tableaux de restitution.

### Résultat attendu

Un résumé des 40 hypothèses et deux tableaux détaillés de 20 lignes, avec les identifiants nécessaires à la validation future.

### À retenir

- Le tableau est ordonné par identifiant, pas par intérêt commercial.
- Le type proposé reste une hypothèse.
- La correspondance identifiant/ligne doit rester stable.

### Vérifier par vous-même

- [ ] Compter 40 lignes au total dans les deux tableaux.
- [ ] Vérifier l’unité de chaque colonne.
- [ ] Ne pas renommer « Type proposé » en « Type réel ».

### Question minute

Pourquoi le tableau peut-il proposer 20 appartements sans prouver qu’il y a réellement 20 appartements ?

## 4.5 — Valider avec des types réels et comprendre les métriques

Repères : C29.

### Objectif

Distinguer ce qui est calculable aujourd’hui de ce qui nécessite des labels, puis comprendre les métriques sans les confondre.

### Code à repérer

```python
fichier_labels = DATA_DIR / 'labels_reference_louise.csv'
validation_louise = None
if not fichier_labels.exists():
    display(Markdown(
        '**Validation externe non disponible :** les types réels de Louise ne sont pas fournis. '
        'Le classement reste provisoire ; aucune performance de classification n’est annoncée.'
    ))
```

```python
    controle_labels = echantillon.merge(labels, on='id_opportunite', validate='one_to_one')
    reel = controle_labels['code_type_reel']
    predit = controle_labels['code_type_estime']
    validation_louise = {
        'Exactitude': accuracy_score(reel, predit),
        'Exactitude équilibrée': balanced_accuracy_score(reel, predit),
        'Précision locaux': precision_score(reel, predit, pos_label=4, zero_division=0),
        'Rappel locaux': recall_score(reel, predit, pos_label=4, zero_division=0),
```

```python
    display(pd.DataFrame(confusion_matrix(reel, predit, labels=[2, 4]),
        index=['Réel : appartement', 'Réel : local'],
        columns=['Prédit : appartement', 'Prédit : local']))
```

### Lecture pas à pas

Un label est ici le type réel confirmé d’un bien. Le fichier labels_reference_louise.csv est facultatif et attendu dans DATA_DIR. Il doit contenir id_opportunite et code_type_reel, avec 2 pour appartement et 4 pour local. Tant qu’il manque, validation_louise reste None et le notebook affiche que la validation externe est indisponible : ce comportement est normal, ce n’est pas une erreur à contourner.

Si le fichier existe, read_csv le lit ; sep=None avec engine="python" tente de détecter son séparateur. Les contrôles exigent des colonnes présentes, des nombres lisibles, des identifiants sans doublon, exactement les mêmes identifiants que l’échantillon et uniquement les types 2 ou 4. La comparaison des ensembles d’identifiants évite des biens manquants ou supplémentaires.

merge(..., on="id_opportunite", validate="one_to_one") associe chaque type réel à sa proposition par identifiant, pas simplement par position de ligne. Une ligne réelle et une ligne prédite doivent désigner le même bien. reel contient alors les réponses de référence ; predit contient les types proposés avant consultation de ces réponses.

Le code considère le local, code 4, comme la classe positive avec pos_label=4. Vrai positif (TP) : un local réel proposé comme local. Faux positif (FP) : un appartement réel proposé comme local, donc une fausse alerte. Faux négatif (FN) : un local réel proposé comme appartement, donc un local manqué. Vrai négatif (TN) : un appartement réel proposé comme appartement.

L’exactitude, accuracy, vaut (TP + TN) / nombre total : la part de propositions correctes. La précision des locaux vaut TP / (TP + FP) : parmi les biens proposés locaux, quelle part l’est réellement ? Le rappel des locaux vaut TP / (TP + FN) : parmi tous les locaux réels, quelle part a été retrouvée ? Ces questions ont des dénominateurs différents.

F1 est la moyenne harmonique de précision et rappel : 2 × précision × rappel / (précision + rappel), soit aussi 2TP / (2TP + FP + FN). Elle baisse lorsqu’une des deux dimensions est faible. L’exactitude équilibrée, balanced accuracy, est la moyenne des rappels des deux classes : [TP/(TP+FN) + TN/(TN+FP)] / 2. Elle donne autant de poids aux appartements qu’aux locaux, même s’ils n’ont pas le même effectif.

EXEMPLE PÉDAGOGIQUE FICTIF, jamais calculé sur les biens de Louise : imaginons 20 biens dont 16 appartements et 4 locaux. Avec TN=14, FP=2, FN=1 et TP=3, la matrice selon les lignes « réel : appartement/local » et les colonnes « prédit : appartement/local » est [[14, 2], [1, 3]]. L’exactitude est 17/20 = 85 % ; la précision locaux 3/5 = 60 % ; le rappel locaux 3/4 = 75 % ; F1 vaut 6/9 = 66,7 % ; l’exactitude équilibrée vaut (87,5 % + 75 %)/2 = 81,25 %. Ces nombres servent uniquement à apprendre les formules et ne décrivent aucune performance réelle du projet.

confusion_matrix(..., labels=[2, 4]) fixe cet ordre des lignes et colonnes. Les cellules ne se lisent donc pas toutes comme de bonnes prédictions : les bonnes sont sur la diagonale. zero_division=0 fixe la valeur renvoyée lorsqu’un dénominateur de précision, rappel ou F1 ne peut pas être calculé ; cela évite une division indéfinie mais ne rend pas le classement meilleur.

Les labels servent à évaluer une correspondance figée, pas à réajuster les clusters ou à inverser opportunément leur nom après avoir vu les réponses. Si l’on conçoit ensuite un modèle supervisé avec ces labels, une véritable évaluation indépendante devra être prévue. La silhouette de 0,909 restera une mesure distincte de toute exactitude supervisée.

### Fonctions et méthodes

- `Path.exists()` : Détermine si le fichier de référence a été fourni.
- `pd.read_csv(), pd.to_numeric(..., errors="raise")` : Lisent les labels et arrêtent la validation si une valeur numérique est illisible.
- `duplicated(), isin(), set()` : Contrôlent l’unicité, les codes autorisés et la couverture exacte des identifiants.
- `merge(..., validate="one_to_one")` : Apparie un seul label réel avec une seule opportunité par identifiant.
- `accuracy_score()` : Calcule la proportion totale de types proposés corrects.
- `balanced_accuracy_score()` : Calcule la moyenne des rappels des deux classes.
- `precision_score(), recall_score(), f1_score()` : Évaluent les propositions de locaux, ici classe positive 4.
- `confusion_matrix(..., labels=[2, 4])` : Compte les accords et erreurs dans un ordre explicite de classes.

### Résultat attendu

Dans les fichiers fournis, les labels réels manquent : aucune exactitude, précision, rappel, F1 ou matrice de confusion réelle des 40 biens n’est annoncée. Le code de validation est prêt à être exécuté si le fichier complet de référence est fourni.

### À retenir

- Silhouette ≠ exactitude.
- Comparer une proposition au type réel du même identifiant.
- La classe positive est le local, code 4.
- Ne jamais présenter les chiffres de l’exemple fictif comme des résultats.

### Vérifier par vous-même

- [ ] Sans labels, retrouver le message de validation externe indisponible.
- [ ] Avec labels, vérifier leur couverture exacte des 40 identifiants.
- [ ] Lire les intitulés réel/prédit de la matrice avant d’interpréter ses cases.
- [ ] Conserver la correspondance de groupes établie avant l’évaluation.

### Question minute

Dans l’exemple fictif, pourquoi une exactitude de 85 % coexiste-t-elle avec une précision locaux de 60 % ?

## 4.conclusion — Conclure le classement sans dépasser les données

Repères : Lecture Markdown — sans cellule de code.

### Objectif

Séparer le résultat mathématique vérifié, l’interprétation métier proposée et la vérité terrain absente.

### Code à repérer

### Lecture pas à pas

La conclusion comporte trois étages. Premier étage, observé : les 40 prix au m² forment deux groupes séparés, avec 20 biens par groupe et des centres d’environ 7 409 et 9 807 €/m². Deuxième étage, interprété : le groupe bas est proposé comme appartement et le haut comme local, à partir de l’ordre des moyennes du 19e en 2021. Troisième étage, encore inconnu : les types réels des 40 biens.

Le décalage de 16,1 % entre le centre bas et la moyenne des appartements de référence, la date inconnue de l’échantillon et les 11 locaux seulement dans la référence empêchent de considérer les noms proposés comme validés. Une séparation visuelle convaincante ne supprime pas ces limites.

La suite proposée est de demander les types réels et les dates à Louise, puis de confronter les propositions à ces réponses. Avec des exemples étiquetés fiables et suffisamment nombreux, on pourrait ensuite étudier une classification supervisée. Ce serait un nouveau protocole, avec séparation apprentissage/test et évaluation indépendante ; l’existence de deux clusters ne garantit pas sa future performance.

Cette fiche commente la conclusion rédigée du notebook ; elle n’ajoute ni calcul ni cellule de code. Elle ferme le Milestone 4 et prépare le Milestone 5 — Analyse et présentation des résultats.

### Fonctions et méthodes


### Résultat attendu

Le regroupement de prix est calculé ; les noms de types sont proposés ; la validation des types reste à faire.

### À retenir

- Calculé : groupes de prix.
- Supposé : correspondance groupe/type.
- À obtenir : dates et types réels.

### Vérifier par vous-même

- [ ] Conserver ces trois niveaux dans la conclusion orale.
- [ ] Ne pas employer « 20 appartements réels ».
- [ ] Relier chaque limite à une action réalisable.

### Question minute

Quelle phrase résume honnêtement le résultat de Louise ?

## 5.1 — Assembler une synthèse à partir des calculs

Repères : C30.

### Objectif

Comprendre comment les variables calculées alimentent automatiquement la synthèse, sans ressaisie manuelle des chiffres.

### Code à repérer

```python
synthese = f"""
1. **Données :** {fr(len(historique))} lignes de ventes du {date_min:%d/%m/%Y} au {date_max:%d/%m/%Y},
   dont {fr(nb_appartements)} appartements et {fr(nb_locaux)} locaux.
2. **Prix moyen au m² des appartements :** {fr(variation_2017_2021, 1)} % entre les moyennes 2017 et 2021 ;
   {fr(variation_2020_2021, 1)} % de 2020 à 2021. Le prix moyen varie aussi selon l’arrondissement.
3. **Régression :** MAPE de {fr(metriques_test['MAPE (%)'], 2)} % sur le test de 33 %,
   et de {fr(metriques_2021['MAPE (%)'], 2)} % sur le test chronologique 2021.
   Ce dernier présente un biais relatif moyen de {fr(metriques_2021['Biais relatif (%)'], 2)} %.
```

```python
5. **Louise :** {len(echantillon)} biens séparés en deux groupes de
   {int(resume_clusters.iloc[0].effectif)} et {int(resume_clusters.iloc[1].effectif)} observations.
   Silhouette : {fr(score_silhouette, 3)}. Les types proposés ne sont pas validés par des labels réels.
"""
display(Markdown(synthese))
```

### Lecture pas à pas

La variable synthese reçoit une longue chaîne de caractères entre triples guillemets. Le préfixe f indique une f-string : chaque expression entre accolades est remplacée par sa valeur calculée. On ne recopie donc pas « 169,70 » à la main ; l’expression total_portefeuille / 1_000_000 est recalculée puis mise en forme.

La fonction fr est une fonction d’affichage du notebook. Par exemple fr(valeur, 2) montre deux décimales avec une présentation française. Cet arrondi facilite la lecture ; il ne doit pas remplacer les valeurs de calcul conservées en mémoire. Les formats de dates comme %d/%m/%Y rendent la période explicite.

La synthèse reprend le Milestone 1 — Analyse des données ; le Milestone 2 — Entraînement de l’algorithme ; le Milestone 3 — Prédiction pour le client ; et le Milestone 4 — Classification des données de Louise. Leur restitution commune constitue le Milestone 5 — Analyse et présentation des résultats. Ce sont les intitulés du notebook consulté, pas une attestation de couverture d’un énoncé OpenClassrooms complet non consulté ici.

Les chiffres à lire ensemble sont : 26 196 lignes historiques, dont 24 353 appartements et 1 843 locaux ; hausse de 10,1 % du prix moyen au m² des appartements entre 2017 et 2021 et baisse de 2,1 % entre 2020 et 2021 ; MAPE de 9,14 % sur le test aléatoire et de 13,62 % sur le test chronologique, avec un biais de +12,81 % ; portefeuille de 275 lignes estimé à 169,70 M€, partagé entre 71,22 M€ et 98,48 M€ selon les segments conventionnels ; enfin 40 opportunités et deux groupes de 20, sans validation des types.

display(Markdown(synthese)) affiche la chaîne comme un texte mis en forme dans Jupyter. Le Markdown gère notamment les numéros et le gras ; il ne réalise aucun calcul statistique supplémentaire. Si des paramètres ou des données changent, il faut redémarrer et exécuter toutes les cellules pour éviter une synthèse mélangeant anciens et nouveaux objets.

### Fonctions et méthodes

- `f"""...""" et accolades` : Construisent un texte multi-lignes en y insérant les résultats calculés.
- `fr()` : Formate les nombres à la française pour la lecture.
- `len(), int()` : Obtiennent un effectif ou transforment un effectif affiché en entier.
- `loc[] et iloc[]` : Retrouvent un résultat par son étiquette ou sa position dans un tableau.
- `display(Markdown(...))` : Rend la synthèse lisible dans le notebook sans changer les calculs.

### Résultat attendu

Une synthèse dynamique reliant les principaux résultats aux objets calculés dans les sections précédentes, avec les limites du classement de Louise conservées.

### À retenir

- Une synthèse rassemble les résultats ; elle ne les réinvente pas.
- Toujours préciser l’unité, la population et la période.
- Les chiffres d’une exécution complète doivent rester cohérents entre eux.

### Vérifier par vous-même

- [ ] Le +10,1 % concerne le prix moyen au m², pas le prix total moyen.
- [ ] Le total de 169,70 M€ porte sur le 31/12/2022, pas sur la date actuelle.
- [ ] La silhouette 0,909 ne devient pas une exactitude dans le résumé.

### Question minute

Pourquoi produire la synthèse avec une f-string plutôt que recopier les chiffres ?

## 5.2 — Répondre au client et transformer les limites en actions

Repères : Lecture Markdown — sans cellule de code.

### Objectif

Apprendre à associer chaque conclusion à sa condition d’utilisation et à une prochaine action.

### Code à repérer

### Lecture pas à pas

Cette section est une cellule Markdown de rédaction, sans code supplémentaire. Une réponse au client ne consiste pas à empiler tous les tableaux : elle doit dire ce que l’étude apporte, ce qu’elle ne permet pas de conclure et quelle information demander ensuite.

L’étude apporte une description des ventes du fichier 2017–2021, une première estimation du portefeuille au 31/12/2022 et un classement exploratoire des opportunités. Les données sont pédagogiques et historiques : elles ne représentent pas automatiquement le marché immobilier actuel.

Sous la convention appartements = particuliers et locaux = corporate, la valeur totale estimée du corporate, 98,48 M€, dépasse celle des particuliers, 71,22 M€. Une valeur totale dépend notamment du nombre de biens, de leur taille et de leurs caractéristiques. La rentabilité demanderait d’autres informations, comme les revenus, charges et coûts ; ces deux totaux ne justifient donc pas une recommandation de vente ou de développement d’un segment.

Les répétitions exactes et l’absence d’identifiants de mutation invitent à parler de nombres de lignes et à vérifier les actifs répétés. Les moyennes et corrélations ne neutralisent pas toutes les caractéristiques des ventes : une association n’est pas une explication causale. L’erreur chronologique et le biais observés imposent de communiquer une estimation indicative, sans promesse de précision individuelle.

La date 2022 est hors de l’historique d’apprentissage ; il faut des données plus récentes et une nouvelle évaluation temporelle avant usage réel. Les segments commerciaux doivent être confirmés par l’entreprise. Les types et les dates des opportunités doivent être obtenus auprès de Louise pour évaluer les propositions.

La réponse se termine donc par des priorités concrètes : confirmer les répétitions et les segments ; récupérer les labels et les dates ; enrichir les caractéristiques des biens et réévaluer les modèles dans le temps. Une limite bien formulée ne bloque pas la discussion : elle indique le prochain travail utile.

### Fonctions et méthodes


### Résultat attendu

Une réponse métier qui distingue description historique, estimation indicative et hypothèse de classement, puis propose des actions réalistes.

### À retenir

- Valeur totale supérieure ≠ rentabilité supérieure.
- Prévision après 2021 = extrapolation à contrôler.
- Chaque limite doit conduire à une demande ou à une vérification précise.

### Vérifier par vous-même

- [ ] Ne pas présenter la valorisation comme une expertise actuelle.
- [ ] Faire apparaître la convention des segments près de la comparaison.
- [ ] Ne pas convertir une corrélation en causalité.

### Question minute

Peut-on recommander de développer le corporate parce qu’il vaut plus dans le portefeuille ?

## 5.3 — Construire un récit oral avec les cinq milestones

Repères : Lecture Markdown — sans cellule de code.

### Objectif

Passer d’un ordre d’exécution informatique à un fil oral qui relie question, méthode, preuve, limites et suite proposée.

### Code à repérer

### Lecture pas à pas

Cette section est une trame de rédaction en Markdown, sans nouvelle cellule de code. Le notebook contient les éléments nécessaires à l’analyse et à leur présentation, mais il ne constitue pas à lui seul un diaporama séparé.

Commencer par la question métier : comprendre l’évolution des prix, estimer le portefeuille et explorer les opportunités. Nommer les trois fichiers et préciser la période historique avant de montrer des résultats. Ce cadrage évite que le public interprète les chiffres comme des prix actuels.

Pour le Milestone 1 — Analyse des données, sélectionner l’évolution annuelle, les écarts entre arrondissements et les différences entre types. Les unités €/m², euros et m² doivent rester distinctes. Une moyenne décrit les ventes observées ; elle ne raconte pas nécessairement l’évolution d’un même bien.

Pour le Milestone 2 — Entraînement de l’algorithme, expliquer d’abord la cible en euros et les quatre variables : surface, date, code postal et type. Exposer ensuite le test de 33 % et la MAPE, puis le contrôle chronologique. Le passage de 9,14 % à 13,62 % et le biais de +12,81 % expliquent pourquoi prévoir le futur demande plus de prudence.

Pour le Milestone 3 — Prédiction pour le client, annoncer la date du 31/12/2022 et la valeur totale estimée de 169,70 M€, puis sa ventilation en 71,22 M€ et 98,48 M€ selon les segments conventionnels. Expliquer aussitôt l’extrapolation et la convention de segmentation.

Pour le Milestone 4 — Classification des données de Louise, montrer les deux groupes de prix. Distinguer les centres calculés, les noms de types proposés et les types réels absents. Expliquer avec une phrase simple que silhouette et exactitude répondent à des questions différentes.

Le Milestone 5 — Analyse et présentation des résultats ferme le récit : rappeler les résultats utiles, les conditions d’usage et les informations à obtenir. Ces cinq intitulés sont repris du notebook ; le guide n’affirme pas avoir vérifié un énoncé OpenClassrooms complet ou une grille d’évaluation extérieure au fichier.

### Fonctions et méthodes


### Résultat attendu

Une trame orale en six mouvements : question et sources ; marché ; modèle ; évaluation et valorisation ; groupes de Louise ; limites et prochaines actions.

### À retenir

- Expliquer la question avant la technique.
- Placer les limites matérielles près du résultat concerné.
- Répondre « ce que cela change pour le client » après chaque partie.

### Vérifier par vous-même

- [ ] Conserver les mêmes chiffres et mêmes dates que le notebook exécuté.
- [ ] Éviter les détails de bibliothèques avant d’avoir expliqué la méthode.
- [ ] Ne pas confondre le guide, le notebook et le diaporama : ce sont des supports différents.

### Question minute

Pourquoi présenter le test chronologique avant d’insister sur la valorisation ?

## 5.4 — Exporter les résultats et conserver leur provenance

Repères : C31.

### Objectif

Comprendre les exports CSV, les empreintes des sources et les versions de l’environnement.

### Code à repérer

```python
export_portefeuille = DOSSIER_RESULTATS / 'predictions_valorisation_portefeuille_2022-12-31.csv'
export_classification = DOSSIER_RESULTATS / 'classification_echantillon_louise_102026.csv'
portefeuille[colonnes_portefeuille].to_csv(export_portefeuille, index=False, sep=';', encoding='utf-8-sig', float_format='%.2f')
echantillon.to_csv(export_classification, index=False, sep=';', encoding='utf-8-sig', float_format='%.2f')
valorisation_segments.to_csv(DOSSIER_RESULTATS / 'synthese_valorisation_segments.csv', sep=';', encoding='utf-8-sig', float_format='%.2f')
pd.DataFrame([metriques_test, metriques_2021], index=['test_33_pct', 'test_2021']).to_csv(
    DOSSIER_RESULTATS / 'metriques_regression.csv', sep=';', encoding='utf-8-sig', float_format='%.6f')
```

```python
provenance = pd.DataFrame([
    {'Fichier': nom, 'SHA-256': sha256((DATA_DIR / nom).read_bytes()).hexdigest()}
    for nom in FICHIERS.values()
])
provenance.to_csv(DOSSIER_RESULTATS / 'sources_sha256.csv', index=False)
```

```python
environnement = {'Python': platform.python_version()}
environnement.update({nom: version(nom) for nom in [
    'pandas', 'numpy', 'matplotlib', 'scipy', 'scikit-learn', 'openpyxl',
]})
(DOSSIER_RESULTATS / 'environnement.json').write_text(
    json.dumps(environnement, ensure_ascii=False, indent=2), encoding='utf-8'
)
display(pd.Series(environnement, name='Version utilisée').to_frame())
```

### Lecture pas à pas

Les objets pandas en mémoire ne suffisent pas pour un destinataire qui n’exécute pas Python. to_csv écrit des tableaux dans des fichiers texte séparant les colonnes par un caractère. Le code crée notamment la valorisation ligne par ligne, le classement des opportunités, la synthèse des segments, les métriques, l’évolution annuelle et la comparaison des arrondissements.

Pour les principaux résultats, sep=";" choisit le point-virgule comme séparateur. Il faut reprendre sep=";" lors de leur relecture, sinon toutes les valeurs peuvent être lues comme une seule colonne. encoding="utf-8-sig" conserve les accents et ajoute une marque d’encodage souvent bien reconnue par Excel. Le séparateur décimal des fichiers reste celui produit par pandas ; l’affichage français d’Excel dépend aussi de ses réglages.

index=False évite d’ajouter l’index technique aux exports ligne par ligne. Dans d’autres tableaux, l’index porte une information utile, comme le segment ou l’année, et il est conservé. float_format="%.2f" écrit deux décimales dans les CSV concernés, tandis que les métriques gardent six décimales. Cet arrondi de sortie ne modifie pas les valeurs conservées en mémoire ; il explique les tolérances de relecture de C32.

colonnes_portefeuille fixe les colonnes livrées et leur ordre. La table de classement conserve aussi les propositions et leur statut. Un export n’est pas une validation supplémentaire : un fichier correctement écrit peut encore contenir une hypothèse métier non confirmée.

sha256((DATA_DIR / nom).read_bytes()).hexdigest() lit exactement les octets d’un classeur et calcule son empreinte SHA-256, une longue signature de contenu. Si un octet change, l’empreinte change normalement. Comparer les empreintes permet de vérifier que les mêmes sources sont utilisées. Ce n’est ni un chiffrement, ni une preuve de véracité du contenu, ni à lui seul une garantie de l’identité de l’auteur.

sources_sha256.csv utilise le séparateur par défaut de to_csv, la virgule, car aucun sep n’est donné pour ce fichier. Il ne faut donc pas appliquer aveuglément le point-virgule à tous les CSV. Le fichier environnement.json enregistre la version de Python et celles de pandas, numpy, matplotlib, scipy, scikit-learn et openpyxl.

platform.python_version() décrit Python ; version(nom) consulte les versions des bibliothèques installées. json.dumps transforme le dictionnaire en texte JSON ; ensure_ascii=False garde les accents lisibles et indent=2 ajoute une indentation de deux espaces. write_text sauvegarde ce texte en UTF-8. Ces informations facilitent une reproduction et le diagnostic d’un écart, sans garantir à elles seules une reproduction exacte sur toute machine.

### Fonctions et méthodes

- `to_csv()` : Écrit un DataFrame dans un fichier texte tabulaire avec séparateur, encodage et précision choisis.
- `Path / nom_de_fichier` : Construit un chemin de fichier dans le dossier de résultats.
- `read_bytes(), sha256(), hexdigest()` : Lisent les octets puis calculent et affichent l’empreinte du contenu source.
- `platform.python_version(), version()` : Récupèrent les versions de Python et des bibliothèques.
- `json.dumps(), write_text()` : Sérialisent le dictionnaire de versions en JSON puis le sauvegardent.

### Résultat attendu

Les résultats et leur traçabilité sont sauvegardés dans livrables/ : CSV analytiques, graphiques, sources_sha256.csv et environnement.json.

### À retenir

- CSV = données tabulaires réutilisables.
- SHA-256 = repère du contenu exact des sources.
- JSON de versions = description de l’environnement utilisé.
- Arrondir l’export ne remplace pas les valeurs de calcul.

### Vérifier par vous-même

- [ ] Ouvrir les fichiers exportés et vérifier séparateur, accents et nombre de colonnes.
- [ ] Distinguer les CSV principaux à point-virgule du CSV des empreintes à virgule.
- [ ] Vérifier que les trois classeurs apparaissent dans les empreintes.
- [ ] Conserver les sources et le fichier de versions avec les résultats.

### Question minute

Deux analyses donnent des chiffres différents : à quoi servent les empreintes et les versions ?

## 5.5 — Relire les exports et vérifier la cohérence finale

Repères : C32.

### Objectif

Comprendre ce qu’un contrôle automatique garantit, et ce qu’il ne peut pas garantir sur les hypothèses métier.

### Code à repérer

```python
verif_portefeuille = pd.read_csv(export_portefeuille, sep=';')
verif_classification = pd.read_csv(export_classification, sep=';')
assert len(verif_portefeuille) == len(portefeuille_brut)
assert verif_portefeuille['id_bien'].is_unique
assert np.isclose(verif_portefeuille['valeur_estimee_euros'].sum(), total_portefeuille, atol=0.01 * len(portefeuille), rtol=0)
assert len(verif_classification) == len(echantillon_brut)
assert verif_classification['id_opportunite'].is_unique
```

```python
assert len(X_train.index.intersection(X_test.index)) == 0
assert np.allclose(historique['prix_m2'] * historique['surface_reelle'], historique['valeur_fonciere'])
assert np.isclose(np.mean(np.abs(prediction_test - y_test) / y_test) * 100, metriques_test['MAPE (%)'])
assert (appartements_6e['code_postal'] == '75006').all()
assert (appartements_6e['code_type_local'] == 2).all()
print('Contrôles de cohérence et rapprochement des exports : OK.')
```

### Lecture pas à pas

Le notebook relit les CSV réellement sauvegardés, au lieu de supposer que l’export s’est bien passé. pd.read_csv(..., sep=";") doit retrouver les bonnes colonnes. Les assertions comparent alors ces fichiers à la base en mémoire : même nombre de lignes et identifiants uniques, plus une proposition de type non manquante pour chaque opportunité.

assert est une instruction de vérification : si la condition est fausse, Python lève une AssertionError et arrête l’exécution. Si elle est vraie, aucune ligne particulière n’est affichée. Le message final « Contrôles de cohérence et rapprochement des exports : OK » n’apparaît donc qu’après toutes les assertions.

Les nombres décimaux peuvent présenter de très petits écarts de représentation et les CSV sont arrondis à deux décimales. np.isclose compare deux nombres avec une tolérance, plutôt que d’exiger une égalité stricte. Pour le total du portefeuille, atol=0.01 * len(portefeuille) autorise un écart absolu jusqu’à 2,75 € pour 275 lignes ; rtol=0 désactive la tolérance proportionnelle. Ce contrôle porte sur le total relu, pas sur l’erreur immobilière du modèle ni sur chaque actif individuellement.

np.allclose sert à vérifier plusieurs comparaisons élément par élément et à rendre une seule réponse vraie/fausse. Ici, prix_m2 × surface_reelle doit retrouver valeur_fonciere pour toutes les lignes. np.isclose compare aussi la MAPE recalculée manuellement à la métrique stockée : moyenne(|prédit − réel| / réel) × 100. Le ×100 transforme une proportion en pourcentage.

X_train.index.intersection(X_test.index) retrouve les identifiants de lignes communs à apprentissage et test. Exiger une longueur nulle vérifie qu’aucun même index n’est présent des deux côtés. Ce contrôle complète la suppression antérieure des répétitions exactes, mais ne prouve pas à lui seul l’absence de toute fuite d’information : l’encodage et les autres préparations doivent aussi avoir été appris seulement sur l’entraînement.

Les deux dernières assertions vérifient que appartements_6e porte bien le code postal 75006 et le code de type 2 pour toutes ses lignes. Elles protègent le périmètre de la corrélation locale. Un coefficient exact calculé sur la mauvaise population ne répondrait pas à la bonne question.

Le tableau de couverture qui suit rattache les demandes reprises dans le notebook à leurs sections et distingue les points calculés de la validation des types réels encore en attente. Il s’agit d’un rapprochement documentaire avec ce notebook, pas d’une certification d’un énoncé OpenClassrooms complet ou d’une validation métier automatique.

Des contrôles OK signifient que ces cohérences ont été respectées dans cette exécution. Ils ne confirment ni les segments commerciaux supposés, ni les types réels absents de Louise, ni la précision du portefeuille au 31/12/2022 dont les valeurs réelles ne sont pas fournies. Les limites restent visibles même quand tous les contrôles passent.

### Fonctions et méthodes

- `pd.read_csv(..., sep=";")` : Relit les exports avec leur séparateur réel.
- `assert (instruction)` : Arrête l’exécution si la condition vérifiée est fausse.
- `is_unique, notna().all()` : Contrôlent des identifiants sans répétition et des valeurs présentes partout.
- `np.isclose(..., atol=..., rtol=...)` : Compare deux nombres en autorisant un petit écart numérique explicite.
- `np.allclose()` : Vérifie une suite de comparaisons numériques et renvoie un résultat global.
- `Index.intersection()` : Trouve les index présents dans deux ensembles de lignes.
- `np.mean(), np.abs()` : Recalculent la moyenne des erreurs relatives absolues pour rapprocher la MAPE.

### Résultat attendu

Les 275 lignes de portefeuille et les 40 opportunités sont relues ; les identifiants, totaux, formules, périmètres et séparation d’index passent les contrôles. Le message final est OK. La validation métier des types réels reste en attente.

### À retenir

- Une assertion teste une condition précise, pas toute la qualité de l’étude.
- isclose compare deux nombres ; allclose vérifie plusieurs valeurs.
- Tolérance d’arrondi ≠ incertitude du modèle.
- Le test doit rester séparé de l’apprentissage.

### Vérifier par vous-même

- [ ] Retrouver le message final OK après une exécution complète.
- [ ] Vérifier qu’aucune AssertionError n’a été ignorée.
- [ ] Contrôler 275 lignes et 40 identifiants uniques dans les exports.
- [ ] Lire le tableau de couverture avec son point restant en attente.

### Question minute

Si tous les assert passent, peut-on affirmer que les types proposés à Louise sont corrects ?

## Annexe A — Imports

### pathlib.Path

Manipuler les chemins de fichiers et dossiers.

C01/C02 : chemins des sources et des exports ; C31 : lecture des octets et écriture JSON.

### hashlib.sha256

Calculer une empreinte de contrôle du contenu d’un fichier.

C31 : sha256((DATA_DIR / nom).read_bytes()).hexdigest() ; identifier la version des sources, sans prouver leur qualité métier.

### importlib.metadata.version

Lire la version installée d’une distribution Python.

C31 : consigner pandas, NumPy, Matplotlib, SciPy, scikit-learn et openpyxl dans environnement.json.

### json

Convertir des structures Python vers un texte JSON.

C31 : json.dumps(environnement, ensure_ascii=False, indent=2), puis write_text.

### platform

Décrire la plate-forme et la version de Python.

C02 : activer le sélecteur seulement sur Windows ; C31 : platform.python_version().

### numpy → np

Faire des calculs numériques sur des tableaux.

Alias np. Contrôles isfinite, calculs de moyenne/erreur, np.asarray et np.isclose ; les résultats restent numériques.

### pandas → pd

Lire, organiser, filtrer et agréger des tableaux.

Alias pd. Lecture Excel/CSV, DataFrame, Series, dates, groupby, jointures et exports ; moteur Excel openpyxl demandé par read_excel, sans import direct d’openpyxl.

### matplotlib.pyplot → plt

Créer et afficher les figures Matplotlib.

Alias plt. Style partagé en C01, subplots, show et close pour les graphiques.

### matplotlib.ticker → mtick

Formater les graduations des axes.

Alias mtick. C01 : FuncFormatter adapte fr au format numérique des axes.

### matplotlib.dates → mdates

Définir les repères et formats des axes de dates.

Alias mdates. C12 : DateFormatter affiche les années sur les graduations datées, choisies explicitement avec set_xticks.

### IPython.display.display

Afficher un objet riche dans les sorties du notebook.

Tableaux, Styler et objets Markdown ; cet affichage n’est pas un export CSV.

### IPython.display.Markdown

Construire un texte interprété comme Markdown par le notebook.

Interprétations calculées, chiffres mis en gras et avertissements de méthode.

### scipy.stats.pearsonr

Mesurer une association linéaire et fournir une p-value.

C13 : date/prix au m² dans le 6e ; C14 : surface/valeur totale, puis surface/prix au m².

### scipy.stats.spearmanr

Mesurer une association fondée sur les rangs.

C13 : complément de Pearson pour la relation date/prix au m² du 6e ; pas une preuve de causalité.

### sklearn.base.clone

Créer une copie non entraînée de la configuration d’un estimateur.

C17/C20/C22 : réutiliser la configuration du prétraitement ou du modèle sans conserver un apprentissage précédent.

### sklearn.cluster.KMeans

Regrouper des observations autour de centres appris sans labels réels.

C25 : deux groupes sur le prix au m² des 40 biens, n_init=20 et random_state=GRAINE.

### sklearn.compose.ColumnTransformer

Appliquer des traitements différents à plusieurs groupes de colonnes.

C17 : encoder les catégories et conserver les variables numériques prévues pour le modèle.

### sklearn.dummy.DummyRegressor

Construire une prévision de référence simple.

C18 : prédire la médiane apprise sur y_train ; point de comparaison avec la régression.

### sklearn.linear_model.LinearRegression

Ajuster une régression linéaire.

C17 : prédire directement la valeur foncière totale en euros à partir des variables autorisées.

### sklearn.metrics.mean_absolute_error

Calculer la moyenne des erreurs absolues.

C18 : MAE en euros, dans mesurer_regression.

### sklearn.metrics.mean_absolute_percentage_error

Calculer la moyenne des erreurs absolues relatives.

C18 : résultat multiplié par 100 pour la MAPE en pourcentage ; les prix réels sont contrôlés positifs en amont.

### sklearn.metrics.mean_squared_error

Calculer la moyenne des erreurs au carré.

C18 : np.sqrt transforme cette MSE en RMSE, exprimée en euros.

### sklearn.metrics.r2_score

Mesurer le coefficient de détermination par rapport à la variabilité des valeurs réelles.

C18 : R² sans unité ; il peut être négatif et n’est pas un pourcentage de prédictions correctes.

### sklearn.metrics.silhouette_score

Mesurer la séparation et la compacité relatives de groupes.

C25 : silhouette de K-means sur les 40 prix au m² ; elle ne compare pas des types réels.

### sklearn.metrics.accuracy_score

Mesurer la proportion de labels correctement prédits.

C29 uniquement si les types réels de Louise sont fournis et correctement appariés.

### sklearn.metrics.balanced_accuracy_score

Moyenner le rappel de chaque classe pour limiter l’effet d’une classe majoritaire.

C29, branche conditionnelle de validation externe après réception des labels.

### sklearn.metrics.precision_score

Mesurer la part de vrais locaux parmi les biens prédits locaux.

C29 si labels disponibles ; pos_label=4 fixe le local comme classe positive.

### sklearn.metrics.recall_score

Mesurer la part de locaux réels retrouvés par les prédictions.

C29 si labels disponibles ; pos_label=4 et zero_division=0 sont explicites.

### sklearn.metrics.f1_score

Combiner précision et rappel par une moyenne harmonique.

C29 si labels disponibles ; score calculé pour les locaux, sans promesse de validité tant que les labels manquent.

### sklearn.metrics.confusion_matrix

Compter les croisements entre labels réels et prédits.

C29 si labels disponibles ; labels=[2, 4] fixe l’ordre appartement/local dans les lignes et colonnes.

### sklearn.model_selection.train_test_split

Partager les données en apprentissage et test.

C16 : test_size=0.33, random_state=42 et stratification sur le type de bien.

### sklearn.pipeline.Pipeline

Enchaîner les transformations et l’estimateur dans le même objet.

C17 : apprendre l’encodage sur l’entraînement, puis l’appliquer de façon cohérente au test et aux prédictions.

### sklearn.preprocessing.OneHotEncoder

Transformer les catégories en indicateurs numériques.

C17 : code postal et type ; apprendre les modalités sur l’entraînement pour éviter une fuite entre ensembles.

### os

Lire les variables d’environnement du processus.

C02 : os.environ pour VIRTUAL_ENV et CONDA_PREFIX, seulement en recours après les indices du noyau.

### sys

Décrire l’interpréteur Python qui exécute réellement le notebook.

C02 : sys.prefix et sys.executable fournissent des indices de chemin à confirmer par le marqueur du notebook.

### tkinter → tk

Créer une interface graphique native simple.

Alias tk ; import conditionnel dans _choisir_projet_windows. Fenêtre de sélection uniquement en dernier recours sous Windows ; ImportError ou TclError peuvent mener à None.

### tkinter.filedialog

Ouvrir une boîte de dialogue de sélection de dossier.

Import conditionnel. C02 : askdirectory demande le projet ; annuler renvoie une absence de choix, pas une racine devinée.

## Annexe B — Fonctions personnelles

### fr(nombre, decimales=0)

Mettre un nombre au format français, sans modifier la donnée numérique initiale.

str : nombre arrondi pour l’affichage, espaces de milliers et virgule décimale.

C01

### afficher_p(p)

Présenter une p-value avec trois chiffres significatifs ou une borne « < 10⁻¹⁶ ».

str ; ne calcule pas de test statistique.

C01

### legende_figure(fig, ncol=2)

Collecter les légendes des axes, dédupliquer leurs libellés et placer une légende commune sous la figure.

Objet matplotlib.legend.Legend ; agit aussi sur la figure reçue.

C01

### terminer_figure(fig, nom)

Fixer un rendu blanc lisible, enregistrer le PNG dans DOSSIER_FIGURES, afficher puis fermer la figure.

None implicitement ; effets : fichier PNG créé et sortie graphique affichée.

C01

### afficher_tableau(tableau, titre, formats=None, masquer_index=False)

Construire et afficher un Styler HTML avec titre, formats par colonne et masquage facultatif de l’index.

None implicitement ; affiche le Styler sans remplacer les valeurs numériques du DataFrame.

C01

### libelle_arrondissement(code_postal)

Calculer le numéro depuis le code postal et produire un libellé « 1er (75001) », « 2e (75002) », etc.

str ; suppose un code postal déjà contrôlé comme parisien dans l’analyse.

C01

### _racine_depuis(ancrage)

Remonter les parents d’un ancrage pour reconnaître le projet grâce au notebook attendu ; ne pas rechercher sur tout le disque.

pathlib.Path de la racine reconnue, ou None si aucun marqueur n’est trouvé.

C02

### _choisir_projet_windows(Aucun argument)

Demander en dernier recours un dossier via Tkinter sous Windows, puis fermer la fenêtre.

pathlib.Path du choix ou None : autre système, import/affichage indisponible ou annulation. Le code appelant doit encore valider le marqueur du projet.

C02

### _manquants(dossier)

Comparer les trois noms requis de FICHIERS avec les fichiers réellement présents dans un dossier.

list[str] des noms absents ; liste vide si les trois fichiers sont présents.

C02

### verifier_colonnes(df, colonnes, nom)

Comparer les colonnes attendues à df.columns et nommer les colonnes absentes dans une erreur explicite.

None si le schéma requis est présent ; lève ValueError sinon.

C02

### mesurer_regression(reel, predit)

Convertir les valeurs réelles et prédites en tableaux NumPy, puis calculer MAPE, MAE, RMSE, R² et biais relatif moyen.

dict de cinq mesures : pourcentages, euros et R² sans unité ; une même position doit désigner le même bien dans les deux entrées.

C18

## Annexe C — Syntaxe

### None et is None

None représente une absence de valeur. « is None » teste cette absence ; « None » entre guillemets serait du texte. Ici, l’absence de chemin déclenche la recherche automatique.

```python
DOSSIER_PROJET = None  # Si nécessaire : r'C:/chemin/absolu/vers/le/projet'
DOSSIER_DONNEES = None  # Laisser None pour utiliser data/raw dans le projet détecté.
```

### Import et alias

import charge un module ; as lui donne un nom local. from choisit un objet précis à importer. Les noms courts np et pd sont des alias, pas des mots réservés de Python.

```python
import numpy as np
import pandas as pd
```

### Affectation et paramètres partagés

Le signe = associe un nom à une valeur. Les noms en majuscules signalent ici des paramètres communs par convention ; Python n’interdit pas de les réaffecter.

```python
GRAINE = 42
PART_TEST = 0.33
```

### def, arguments par défaut et return

def définit une fonction ; les parenthèses décrivent les entrées. decimales=0 fournit une valeur par défaut. return fournit le résultat de l’appel ; sans return explicite, le résultat vaut None.

```python
def fr(nombre, decimales=0):
    return f'{nombre:,.{decimales}f}'.replace(',', ' ').replace('.', ',')
```

### lambda et capture d’une valeur

lambda crée une petite fonction sans nom. Dans la boucle de formatage, p=precision fige la précision de la colonne au moment de la création de cette fonction.

```python
    for colonne in tableau.select_dtypes(include='number').columns:
        precision = 0 if pd.api.types.is_integer_dtype(tableau[colonne]) else 2
        formats_auto[colonne] = lambda valeur, p=precision: fr(valeur, p)
```

### F-strings et format numérique

Une chaîne précédée de f insère les expressions écrites entre accolades. La partie après : règle la présentation ; dans fr, le nombre de décimales vient lui-même d’un paramètre. replace renvoie ensuite un nouveau texte.

```python
def fr(nombre, decimales=0):
    return f'{nombre:,.{decimales}f}'.replace(',', ' ').replace('.', ',')
```

### Dictionnaires : clé → valeur

Un dictionnaire entre accolades relie des clés uniques à leurs valeurs. L’accès par une clé, comme FICHIERS['historique'], évite de répéter un nom de fichier à plusieurs endroits.

```python
FICHIERS = {
    'historique': 'historique_immobilier_paris_2017_2021.xlsx',
    'portefeuille': 'portefeuille_actifs.xlsx',
    'echantillon': 'echantillon_a_classer2.xlsx',
}
```

### Listes, tuples et décomposition

Une liste entre crochets conserve un ordre ; un tuple regroupe aussi des éléments, souvent entre parenthèses. L’affectation multiple récupère plusieurs sorties dans le même ordre. Un tuple d’agrégation pandas associe par exemple une colonne et une opération.

```python
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=PART_TEST, random_state=GRAINE,
    stratify=base_modele['code_type_local'],
)
```

### Compréhension de liste

La forme [expression for élément in ensemble if condition] construit une liste à partir d’une boucle et d’un filtre. Ici, elle conserve les noms de fichiers dont is_file est faux.

```python
def _manquants(dossier):
    return [nom for nom in FICHIERS.values() if not (dossier / nom).is_file()]
```

### Générateur et déduplication ordonnée

Un générateur entre parenthèses produit des valeurs au fil de son parcours. dict.fromkeys conserve une seule occurrence de chaque clé dans l’ordre de rencontre ; list en récupère la liste. Ce mécanisme ne choisit pas entre deux projets différents : le code vérifie l’ambiguïté ensuite.

```python
    racines = list(dict.fromkeys(racine for ancrage in ancrages
                                if (racine := _racine_depuis(ancrage)) is not None))
```

### Affectation dans une expression : :=

L’opérateur := mémorise une valeur tout en permettant de la tester dans la même expression. Il évite ici d’appeler deux fois _racine_depuis pour un même ancrage. Il ne remplace pas le == qui compare deux valeurs.

```python
    racines = list(dict.fromkeys(racine for ancrage in ancrages
                                if (racine := _racine_depuis(ancrage)) is not None))
```

### if, else et expression conditionnelle

if/else choisit une branche. Une expression « valeur_si_vrai if condition else valeur_si_faux » choisit une valeur à l’intérieur d’une affectation. Les parenthèses ne sont pas nécessaires autour de la condition en Python.

```python
def libelle_arrondissement(code_postal):
    numero = int(code_postal) - 75000
    ordinal = '1er' if numero == 1 else f'{numero}e'
    return f'{ordinal} ({code_postal})'
```

### Booléens : and, or, not et &

and/or combinent des conditions Python ; not les inverse. « formats or {} » choisit le dictionnaire fourni s’il est non vide. Pour combiner des masques pandas ligne par ligne, le notebook emploie & et des parenthèses autour de chaque comparaison.

```python
    formats_auto.update(formats or {})
```

### Ensembles : set et différence

Un set représente des éléments distincts sans ordre de lecture garanti. La soustraction entre deux sets trouve ce qui manque. sorted remet les résultats dans un ordre stable pour le message d’erreur.

```python
def verifier_colonnes(df, colonnes, nom):
    manquantes = sorted(set(colonnes) - set(df.columns))
    if manquantes:
        raise ValueError(f'{nom} : colonnes manquantes {manquantes}')
```

### Index et colonnes pandas

Le DataFrame possède un Index de lignes et des noms de colonnes. Après filtrage, les étiquettes de lignes initiales sont conservées sauf réinitialisation explicite. Elles servent notamment à vérifier qu’aucune observation ne se trouve dans l’apprentissage et le test.

```python
assert len(X_train.index.intersection(X_test.index)) == 0
```

### .loc : sélection par étiquettes ou masque

.loc sélectionne des lignes par leur étiquette ou un masque booléen, et des colonnes par leur nom. Dans ce filtre, le résultat de eq(2) indique les lignes qui sont des appartements ; copy crée un tableau de travail séparé.

```python
appartements = historique.loc[historique['code_type_local'].eq(2)].copy()
locaux = historique.loc[historique['code_type_local'].eq(4)].copy()
```

### .iloc : sélection par position

.iloc utilise la position entière dans l’ordre courant : 0 est la première ligne. Après un tri, la première ligne peut correspondre à une autre étiquette d’index ; il ne faut pas confondre position et identité du groupe.

```python
ecart_arrondissements_2021 = classement_2021.iloc[0] - classement_2021.iloc[-1]
```

### pd.DataFrame et pd.Series

Un DataFrame est un tableau à deux dimensions, avec lignes et colonnes nommées ; une Series est une suite de valeurs indexée, souvent une colonne. Une Series issue d’une colonne peut conserver l’index des lignes d’origine. Ces objets sont différents d’une simple liste Python.

```python
centres = pd.Series(kmeans.cluster_centers_.ravel(), index=range(2), name='Centre (€/m²)')
cluster_bas = int(centres.idxmin())
cluster_haut = int(centres.idxmax())
```

### np.ndarray et calcul vectorisé

NumPy représente les tableaux numériques par le type ndarray. np.asarray transforme ici les entrées en tableaux sans leurs étiquettes pandas ; les calculs de différence et de division se font position par position. L’ordre et la taille des entrées doivent donc correspondre.

```python
def mesurer_regression(reel, predit):
    reel, predit = np.asarray(reel), np.asarray(predit)
```

### Méthodes et copie de travail

Une méthode agit sur un objet, comme tableau.copy() ou colonne.astype(...). L’objet avant le point est le récepteur. copy évite de mélanger les transformations du tableau de travail avec la copie brute conservée au départ.

```python
historique = historique_brut.copy()
historique['date_mutation'] = pd.to_datetime(historique['date_mutation'], errors='coerce')
```

### with — repère complémentaire

with active un contexte puis le referme à la fin du bloc, même en cas d’erreur. Cette version du notebook ne contient aucun bloc with : les tableaux de Louise sont présentés par groupes de vingt lignes. L’exemple ci-dessous est illustratif ; il explique comment limiter une option d’affichage à un bloc sans modifier les données.

```python
# Exemple illustratif, absent du notebook actuel.
with pd.option_context('display.max_rows', 40):
    display(echantillon.head(40))
```

### try / except / finally

try tente une opération ; except traite certaines erreurs prévues ; finally exécute la fermeture dans tous les cas. Le sélecteur peut donc être indisponible ou annulé sans conduire à choisir un dossier système par défaut.

```python
    except (tk.TclError, OSError):
        return None
    finally:
        if fenetre is not None:
            fenetre.destroy()
```

### raise et exceptions explicites

raise arrête le chemin d’exécution normal et signale une erreur. FileNotFoundError décrit ici des fichiers absents ; ValueError décrit une valeur ou un choix ambigu. Le message indique ce que l’utilisateur doit corriger avant de continuer.

```python
    if not projet_explicite.is_absolute():
        raise ValueError('DOSSIER_PROJET doit être un chemin absolu, copié depuis PyCharm.')
```

### assert : vérifier une propriété attendue

assert vérifie une condition et lève AssertionError si elle est fausse. Ces contrôles rapprochent les résultats ; ils ne réparent pas une donnée incorrecte. Pour les entrées essentielles, le notebook utilise aussi des if/raise explicites, car Python peut désactiver assert en mode optimisé.

```python
assert verif_portefeuille['id_bien'].is_unique
assert np.isclose(verif_portefeuille['valeur_estimee_euros'].sum(), total_portefeuille, atol=0.01 * len(portefeuille), rtol=0)
```

### Chemins Path et opérateur /

Avec des objets Path, / joint des éléments de chemin ; avec des nombres, / effectue une division. Le type de l’objet change donc le sens de cet opérateur. DOSSIER_RESULTATS est un chemin, pas une chaîne de caractères contenant des résultats.

```python
DOSSIER_RESULTATS = RACINE / 'livrables'
DOSSIER_FIGURES = DOSSIER_RESULTATS / 'figures'
DOSSIER_FIGURES.mkdir(parents=True, exist_ok=True)
```

### Boucles, zip et décomposition

for répète le bloc indenté pour chaque élément. zip associe les éléments de plusieurs séquences, ici les objets graphiques et leurs libellés. La décomposition place chaque paire dans handle et label.

```python
    for ax in fig.axes:
        for handle, label in zip(*ax.get_legend_handles_labels()):
            if label not in labels:
                handles.append(handle)
                labels.append(label)
```

### Argument nommé et valeur par défaut

Un argument nommé rend explicite le rôle d’une valeur dans un appel. n_clusters=2 demande deux groupes ; n_init=20 demande vingt initialisations et ne signifie pas vingt groupes. Une valeur par défaut de fonction n’est utilisée que si l’appel ne la remplace pas.

```python
kmeans = KMeans(n_clusters=2, n_init=20, random_state=GRAINE)
echantillon['cluster'] = kmeans.fit_predict(X_kmeans)
```

## Annexe D — Corrigés

### QP.1

Le calcul emploie une proportion entre 0 et 1 : 0.33. Pour l’écrire en pourcentage, on la multiplie par 100. L’affichage du symbole % ne remplace pas cette conversion.

### QP.2

Non. Les espaces et la virgule produisent du texte destiné à la lecture. On conserve la colonne numérique pour les calculs et on applique fr au moment de l’affichage.

### QP.3

Son parent est C:\Windows, pas le projet. Il faut retrouver un emplacement confirmé par le notebook ou demander le chemin du projet. Deviner à partir d’un dossier système produirait de nouveaux chemins faux et pourrait envoyer les exports au mauvais endroit.

### Q1.1

Conserver une copie brute permet de distinguer ce qui venait du fichier de ce qui a été transformé. On peut contrôler les changements, rechercher une erreur de conversion et comparer les données sans devoir relire le classeur.

### QQualité

Si deux copies d’une observation passent chacune dans un jeu différent, le modèle est évalué sur une observation qu’il a déjà vue. Les retirer avant la séparation réduit ce risque de fuite entre apprentissage et test.

### Q1.2

Chaque ligne reçoit le même poids dans la moyenne. Comme les appartements sont beaucoup plus nombreux, ils pèsent beaucoup plus que les locaux dans une moyenne globale.

### Q1.3

Le masque serait [True, False, True]. Sa somme vaut 2 : deux lignes sont des appartements.

### Q1.4

Leurs prix totaux sont différents, mais leurs prix au m² sont identiques : 5 000 €/m². C’est précisément ce que permet de distinguer le ratio.

### Q1.5

Les comparaisons n’ont pas la même année de départ. Le niveau de 2021 est inférieur à celui de 2020, mais reste supérieur à celui de 2017.

### Q1.6A

Cela sélectionne les vingt moyennes de l’année 2021. Les étiquettes de colonnes sont des entiers créés à partir des années ; la chaîne de texte '2021' est une étiquette différente et ne correspond pas à cette colonne.

### Q1.6B

Une petite variation pourrait alors remplir toute la hauteur d’un panneau et sembler aussi forte qu’une grande variation ailleurs. Des limites communes conservent une comparaison visuelle honnête.

### Q1.6C

Le notebook mesure combien le prix moyen le plus élevé dépasse le plus faible. La moyenne du 19e est donc la base de comparaison. Une autre base répondrait à une autre question et donnerait un autre pourcentage.

### Q1.7

Cela montre que les biens vendus à une période proche n’ont pas tous le même prix au m². La date peut être associée au niveau des prix sans expliquer à elle seule l’ensemble des différences entre biens.

### Q1.8

Non. Le périmètre demandé est celui des appartements du 6e. Une corrélation globale mélangerait arrondissements et éventuellement types de biens ; elle répondrait à une autre question et pourrait être très différente.

### Q1.9

Non. Les fonctions de calcul ont reçu les colonnes originales. L’échelle logarithmique modifie seulement la façon de placer les points sur la figure ; il faudrait calculer explicitement les logarithmes pour analyser d’autres variables.

### Q1.10

Le code 4 inclut des locaux industriels, commerciaux ou assimilés. Le terme « commerces » seul exclurait à tort une partie de la catégorie. Le libellé court « locaux et assimilés » garde une définition plus fidèle.

### Q2.1

Parce que les caractéristiques et le prix réel d’un même bien doivent toujours rester ensemble. Un découpage commun préserve cette association et évite de comparer une prédiction au prix d’un autre bien.

### Q2.2

Parce que le test doit rester inconnu pendant la construction du modèle, y compris pendant sa préparation. Le pipeline apprend son schéma sur l’apprentissage, puis applique exactement ce schéma au test.

### Q2.3

Non. Elle signifie que la moyenne des écarts absolus rapportés aux prix réels vaut 9,14 % sur ce test. Elle ne compte pas des prédictions « bonnes » ou « mauvaises » selon un seuil et ne garantit aucun écart maximal.

### Q2.4

Il l’a surestimé : son ordonnée, la valeur prédite, est supérieure à son abscisse, la valeur réelle. Cette lecture reste vraie avec les axes logarithmiques.

### Q2.5

Parce que le tirage aléatoire mélange les années connues. Prévoir une année future impose un changement de période que ce tirage ne reproduit pas. Le test chronologique révèle déjà une erreur plus forte et une surestimation sur 2021 ; 2022 reste sans prix réels pour être évalué.

### Q3.1

Non, pas sans revoir et réévaluer le modèle. L’apprentissage a utilisé la surface réelle ; les actifs doivent être décrits avec une définition cohérente. Remplacer cette entrée par Carrez changerait la signification des nombres transmis au modèle.

### Q3.2

Les deux moments ont des rôles différents. Pendant l’évaluation, 2021 sert à tester une prévision sans être vue à l’apprentissage. Après l’évaluation, le modèle final utilise l’historique complet pour produire les estimations. Les anciens scores ne deviennent pas une nouvelle validation indépendante de ce modèle final.

### Q3.3

Non. Le résultat compare des valeurs estimées, pas des revenus ni une rentabilité. Pour mesurer ce qu’un segment rapporte, il faudrait notamment ses loyers, ses charges, ses coûts et ses prix d’acquisition, ainsi qu’une segmentation métier confirmée.

### Q4.1

Le notebook choisit de regrouper selon le seul niveau de prix au m². Ajouter prix et surface changerait la question et la géométrie des distances : la surface pourrait alors participer aux groupes. Ce serait une autre analyse à justifier et à vérifier.

### Q4.2

Non. K-means a seulement reçu les prix au m², sans les types réels. La silhouette dit que les groupes de prix sont compacts et séparés. Pour mesurer le pourcentage de types correctement proposés, il faudrait comparer chaque proposition au type réel de ce même bien.

### Q4.3

Parce que le numéro 0 est arbitraire. Le notebook trouve d’abord quel centre est bas, puis utilise l’ordre des prix historiques locaux pour proposer un nom. Même ainsi, le type réel reste inconnu : le lien entre groupe de prix et nature du bien demeure à valider.

### Q4.4

Les 20 correspondent à l’effectif du groupe de prix auquel le notebook a attribué ce nom par hypothèse. Le type n’a pas été observé dans le fichier. Il faut les réponses de Louise pour connaître le nombre réel d’appartements.

### Q4.5

L’exactitude compte les 17 bonnes réponses sur les 20 biens. La précision locaux ne regarde que les 5 biens proposés locaux : 3 sont réellement des locaux et 2 sont des fausses alertes. Changer le dénominateur change la question mesurée. Aucun de ces scores fictifs n’est disponible pour Louise tant que ses types réels manquent.

### Q4.conclusion

« Les 40 opportunités se répartissent en deux groupes de prix bien séparés. Leur correspondance supposée avec appartements et locaux reste à confirmer avec les types réels et les dates fournis par Louise. »

### Q5.1

La f-string utilise les mêmes objets que les calculs. Après une exécution complète, elle suit donc les résultats et limite les erreurs de recopie. Elle n’empêche toutefois pas une mauvaise interprétation : les mots, unités, périodes et limites doivent aussi être relus.

### Q5.2

Non. Le total estimé est plus élevé sous une convention de segmentation, mais l’étude ne mesure ni rendement, ni coûts, ni risque commercial. La conclusion correcte porte sur la valeur estimée de ce portefeuille ; une décision de développement nécessiterait d’autres données et une analyse adaptée.

### Q5.3

Il montre ce qui se passe lorsque le modèle prédit une période future : l’erreur augmente et une surestimation apparaît. Le public comprend ainsi les limites qui accompagnent naturellement l’estimation de 2022, au lieu de les découvrir après avoir retenu le seul total.

### Q5.4

Les empreintes indiquent d’abord si les fichiers sources sont identiques. Les versions aident ensuite à comparer les environnements logiciels. Cela oriente le diagnostic avant de chercher un écart de paramètres ou de code ; aucune empreinte ne prouve cependant que la méthode choisie est pertinente.

### Q5.5

Non. Les contrôles vérifient notamment que chaque ligne a une proposition et que les exports sont cohérents. Ils n’ont aucun type réel auquel comparer ces propositions. La vérité métier nécessite les labels de Louise ; aucune assertion de présence ou de cohérence ne peut les remplacer.

## Sources

- [Parcours Business Intelligence Analyst — page publique OpenClassrooms](https://openclassrooms.com/fr/paths/805-business-intelligence-analyst) : Le programme public 805 identifie ce travail comme Projet 8 et confirme son titre. Les sous-consignes ne sont pas affichées dans cette page.
- [Page du projet 1591](https://openclassrooms.com/fr/paths/805/projects/1591) : Aucun contenu de mission détaillée validé par cette page. Le 403 ne suffit pas à établir si une connexion résoudrait le problème.
- [BIA_P8_Student_Version.ipynb — gabarit officiel OpenClassrooms](https://s3.eu-west-1.amazonaws.com/course.oc-static.com/projects/Business+Intelligence+Analyst/BIA_project+8/BIA_P8_Student_Version.ipynb) : Les cinq jalons, leurs sous-consignes et le code à compléter ont été lus directement dans la ressource officielle.
- [Syllabus officiel Business Intelligence Analyst — version du 15 octobre 2025](https://static.oc-static.com/syllabus/592-business-intelligence-analyst-fr-fr-standard.pdf) : Mission globale : aider une évolution stratégique en étudiant les tendances immobilières. Compétences : corrélation, analyse multivariée, régression, prédiction, argumentation méthodologique. Identifiant de syllabus 592 : ne pas le présenter comme la fiche détaillée actuelle du projet 1591/path805.
- [Échantillon officiel à classer](https://s3.eu-west-1.amazonaws.com/course.oc-static.com/projects/Business+Intelligence+Analyst/BIA_project+8/echantillon_a_classer2.xlsx) : 40 lignes et 4 colonnes : valeur_fonciere, code_postal, nom_commune, surface_reelle. Uniquement le code postal 75019. Aucune date ni étiquette de type réel. Empreinte identique à celle de la source du dépôt.
- [Notebook du projet P8 de Steve Bell — version analysée](https://github.com/steve57000/p8/blob/af488358e791cddcb36e55713c9d54b4d59e80b6/livrables/Bell_Steve_1_Notebook_102026.ipynb) : Structure actuelle 71 cellules, 32 cellules de code. Les références de sections ci-dessous correspondent aux titres présents ; les numéros de cellules sont des indices à partir de zéro. Cette source décrit notre travail, elle ne constitue pas une consigne officielle.