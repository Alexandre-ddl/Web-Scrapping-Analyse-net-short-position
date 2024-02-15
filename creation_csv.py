import pdfplumber
import pandas as pd
import os

# Spécifiez le chemin du dossier
chemin_dossier = 'pdf_amf'

# Liste tous les fichiers et dossiers dans le chemin spécifié
fichiers = os.listdir(chemin_dossier)

# Filtre pour n'afficher que les fichiers, en excluant les dossiers
fichiers = [f for f in fichiers if os.path.isfile(os.path.join(chemin_dossier, f))]

def save_to_csv(products, save_path, csv_filename="product_images.csv"):
    # Chemin complet du fichier CSV
    csv_path = os.path.join(save_path, csv_filename)
    
    # Crée un DataFrame à partir des produits
    df = pd.DataFrame(products)
    
    # Vérifie si le fichier existe déjà pour décider de l'en-tête
    header = not os.path.exists(csv_path)
    
    # Ajoute les données au fichier CSV, 'a' pour append, ajout à la fin
    df.to_csv(csv_path, mode='a', index=False, header=header, encoding='utf-8')
    #print(f'Les données ont été ajoutées dans {csv_path}')


for f in fichiers : 
    try:
        chemin_fichier_pdf = f"pdf_amf/{f}"

        # Initialiser une liste pour stocker le contenu des tableaux
        contenu_tableaux = []
        
        with pdfplumber.open(chemin_fichier_pdf) as pdf:
            # Parcourir chaque page du PDF
            for page in pdf.pages:
                # Extraire les tableaux de la page courante
                tableaux = page.extract_tables()
                # Parcourir chaque tableau extrait
                for tableau in tableaux:
                    # Ajouter chaque tableau à notre liste de contenu
                    contenu_tableaux.append(tableau)

        # Pour cet exemple, affichons simplement les premières lignes du premier tableau extrait
        if contenu_tableaux:
            product = dict()
            products = []
            # print("Contenu du premier tableau extrait :")
            if len(contenu_tableaux[0])==5:
                for ligne in contenu_tableaux[0]:
                    product[ligne[0]] = ligne[1]     
                    # print(ligne)
                products.append(product)
                save_to_csv(products,"")
 
    except Exception as e:
        # Ce code est exécuté pour toute autre exception non capturée spécifiquement par les blocs except précédents
        print(f"Une erreur inattendue est survenue pour le pdf: {chemin_fichier_pdf}")

    finally:
        continue