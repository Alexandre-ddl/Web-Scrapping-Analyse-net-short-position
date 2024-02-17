from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Process
import pickle
import time



def search_tickers(holder,dic_tikers): 
    options = ChromeOptions()
    #options.add_argument('--headless') 
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.fr/')

    button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "W0wltc"))
    )
    button.click()

    search_box = driver.find_element(By.CLASS_NAME, 'gLFyf')
    search_box.send_keys(f'{holder} yahoo')
    search_box.submit()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3'))
    )

    first_result = driver.find_element(By.CSS_SELECTOR, 'h3')

    result_text = first_result.text

    dic_tikers[holder] = result_text

    driver.quit()

    pass
 
if __name__ == '__main__':
    
    holders = ['REXEL', 'CGG' ,'CASINO GUICHARD-PERRACHON' ,'TECHNICOLOR',
 'EUTELSAT COMMUNICATIONS', 'BOURBON' ,'RENAULT', 'CELLECTIS' ,'ELIS', 'GENFIT',
 'ATOS SE', 'AIR FRANCE-KLM' ,'ORPEA' ,'GAZTRANSPORT ET TECHNIGAZ' ,'VALEO',
 'SEB S.A.' ,'CAPGEMINI' ,'ARKEMA', 'EUROFINS SCIENTIFIC SE' ,'SOCIETE BIC',
 'EIFFAGE' ,'SOLOCAL GROUP' ,'KORIAN' ,'ELIOR GROUP', 'PEUGEOT S.A.', 'NOVACYT',
 'MAISONS DU MONDE' ,'SES IMAGOTAG', 'VALLOUREC', 'ALSTOM' ,'FAURECIA',
 'REMY COINTREAU', 'CLARIANE SE', 'ERAMET' ,'BOURBON CORPORATION',
 'GENSIGHT BIOLOGICS S.A.' ,'NAVYA', 'SMCP' ,'SOITEC', 'SPIE SA', 'GECINA',
 'WORLDLINE' ,'TELEVISION FRANCAISE 1', 'NEOEN' ,'DBV TECHNOLOGIES',
 'TELEPERFORMANCE' ,'CHARGEURS' ,'EUROPCAR MOBILITY GROUP',
 'PUBLICIS GROUPE SA' ,'AKKA TECHNOLOGIES' ,'KAUFMAN & BROAD SA',
 'UBISOFT ENTERTAINMENT' ,'SRP GROUPE', 'GAUSSIN S.A.', 'ALTEN' ,'RALLYE',
 'NEXANS', 'EUROAPI', 'LAGARDERE SCA' ,'NACON', 'MC PHY ENERGY', 'NEXITY',
 'SCOR SE' ,'JCDECAUX SA', 'KLEPIERRE', 'ERYTECH PHARMA', 'TECHNIPFMC PLC',
 'COMPAGNIE PLASTIC OMNIUM SE' ,'LEGRAND', 'SOCIETE GENERALE' ,'VERGNET SA',
 'FNAC SA' ,'ESSILORLUXOTTICA' ,'PERNOD RICARD', 'CARREFOUR', 'NEOPOST',
 'CARBIOS', 'SOLUTIONS 30 SE' ,'BONDUELLE', "LA FRANCAISE DE L'ENERGIE",
 'ACCOR' ,'ADOCIA' ,'SES', 'GETLINK SE', 'QUADIENT S.A.' ,'GROUPE FNAC',
 'INGENICO','KERING' ,'ACTIA GROUP' ,'ARTPRICE.COM' ,'EDENRED',
 'PIXIUM VISION', 'IMERYS', 'ABIVAX', 'SODEXO', 'INNATE PHARMA',
 'EURONEXT NV', 'ORANGE', 'ICADE', 'RUBIS', 'SUEZ',
 "COMPAGNIE INDUSTRIELLE ET\nFINANCIERE D'ENTREPRISES" ,'BOLLORE', "L'OREAL",
 'MERCIALYS' ,'ENGIE', 'TOTAL S.A.' ,'VIVENDI' ,'BOOSTHEAT' ,'AMOEBA',
 'CYBERGUN' ,'ILIAD', 'COMPAGNIE DE SAINT-GOBAIN', 'FORVIA' ,'NEOVACS',
 'ALBIOMA' ,'TECHNIP', 'CARMILA']

    # Nombre d'URLs à traiter en parallèle

    nb_urls_par_lot = 20
    dic_tikers =  dict()

    for i in range(0, len(holders), nb_urls_par_lot):
        lot_urls = holders[i:i + nb_urls_par_lot]
        processes = []

        for holder in lot_urls:

            p = Process(target=search_tickers, args=(holder,dic_tikers,))
            p.start()
            processes.append(p)

        for p in processes:
            p.join()  # Attendre la fin du traitement pour chaque processus

        print(f"Traitement de {nb_urls_par_lot} URLs terminé. Passage au lot suivant.")
    
    with open("dictionnaire_tikers.pkl","wb") as fichier :
        pickle.dump(dic_tikers,fichier)

    
    with open("dictionnaire_tikers.pkl","rb") as fichier :
        dictionnaire = pickle.load(fichier) 

    print(dictionnaire)
