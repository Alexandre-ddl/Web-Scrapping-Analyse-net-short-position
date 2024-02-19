### Environnement

#### 1. Pour créer l'environnement
```
python -m venv env
```
#### 2. Activez l'environnement
```
.\env\Scripts\Activate.ps1
```
#### 3.Installez les modules
```
pip install -r requirements.txt
```

---

### Architecture du projet :

#### 1. scraper/
Description : Contient les scripts ou les modules dédiés à la collecte des données à partir de sources en ligne. Cela inclut des scripts Python utilisant Selenium.
#### 2. data/
raw/ : Stocke les données telles qu'elles sont collectées par les scripts de scraping, sans modification. Dans ce cas c'est principalement des pdfs.
processed/ : Contient les données qui ont été nettoyées, transformées, ou enrichies après le scraping, prêtes à être analysées, ici ce sont des CSV.
external/ : Pour les données supplémentaires obtenues à partir de sources externes, qui ne sont pas le résultat du scraping mais sont nécessaires pour l'analyse. Par exemple fichier de conversion Nom entreprise<>Ticker.
#### 3. notebooks/
Utilisé pour l'exploration de données, l'analyse exploratoire, et la visualisation. Les Jupyter Notebooks sont particulièrement utiles ici pour documenter le processus d'analyse étape par étape.
#### 4. src/
utils/ : Contient des fonctions utilitaires réutilisables, comme des fonctions de nettoyage de données, de transformation, ou des connecteurs à des bases de données.
analysis/ : Modules Python pour des analyses spécifiques, qui peuvent être exécutés de manière indépendante ou utilisés dans les notebooks.
#### 5. output/
results/ : Pour les résultats de l'analyse, comme des fichiers CSV.
figures/ : Pour les visualisations générées, comme des graphiques ou des cartes sauvegardées en format image.
#### 6. docs/
Pour la documentation du projet, y compris la méthodologie de scraping, les descriptions des données, et les conclusions de l'analyse.
#### 7. requirements.txt
Pour lister toutes les dépendances nécessaires à l'exécution du projet, facilitant la reproduction de l'environnement de développement.
#### 8. .gitignore
Pour exclure les fichiers sensibles ou volumineux (comme les données brutes scrapées) du contrôle de version.