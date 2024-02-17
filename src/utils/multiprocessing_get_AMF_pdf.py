from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Process
import pickle
import time

def fonction_parallel(url):
    options = ChromeOptions()
    chemin_dossier_telechargement = "/Users/sacha/Desktop/Finance Short net/pdf_amf"
    options.add_experimental_option("prefs", {
        "download.default_directory": chemin_dossier_telechargement,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True
    })

    driver = webdriver.Chrome(options=options)
    driver.get(url)
    wait = WebDriverWait(driver, 20)

    try:
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".details-box-data.document-regulateur-download-container")))
        element.click()
        #print(f"Le bouton de téléchargement a été cliqué pour l'URL : {url}")
        time.sleep(5)  # Attendre pour s'assurer que le téléchargement démarre
    except Exception as e:
        print(f"Erreur pour l'URL {url} : {e}")
    finally:
        driver.quit()

if __name__ == '__main__':
    with open('url_amf_pos_court_net.pkl', 'rb') as fichier:
        urls = pickle.load(fichier)

    # Nombre d'URLs à traiter en parallèle
    nb_urls_par_lot = 10

    for i in range(0, len(urls), nb_urls_par_lot):
        lot_urls = urls[i:i + nb_urls_par_lot]
        processes = []

        for url in lot_urls:
            #print(f"Lancement du traitement pour l'URL : {url}")
            p = Process(target=fonction_parallel, args=(url,))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()  # Attendre la fin du traitement pour chaque processus

        print(f"Traitement de {nb_urls_par_lot} URLs terminé. Passage au lot suivant.")
