from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from multiprocessing import Process, Manager
import pickle
import time



def search_tickers(holder, dic_tikers,recherche): 
    options = ChromeOptions()
    # options.add_argument('--headless') 
    driver = webdriver.Chrome(options=options)
    driver.get('https://www.google.fr/')

    button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ID, "W0wltc"))
    )
    #driver.execute_script("arguments[0].scrollIntoView(true);", button)

    button.click()

    search_box = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'gLFyf'))
    )
    #driver.execute_script("arguments[0].scrollIntoView(true);", search_box)
    recherche
    search_box.send_keys(recherche)
    search_box.submit()

    WebDriverWait(driver, 20).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'h3'))
    )

    first_result = driver.find_element(By.CSS_SELECTOR, 'h3')
    result_text = first_result.text

    dic_tikers[holder] = result_text
    driver.quit()
 
if __name__ == '__main__':

        dic_tikers = dict()
        holders = ['REXEL', 'CGG' ,'CASINO GUICHARD-PERRACHON' ,'TECHNICOLOR']

        for holder in holders:
            search_tickers(holder, dic_tikers, f'{holder} yahoo')
           

        # Sauvegarder le dictionnaire dans un fichier si nécessaire
        with open("dictionnaire_tikers.pkl", "wb") as fichier:
            # Notez que vous devez convertir dic_tickers en un dictionnaire normal pour le sauvegarder avec pickle
            pickle.dump(dict(dic_tikers), fichier)

        
        with open("dictionnaire_tikers.pkl","rb") as fichier :
            dictionnaire = pickle.load(fichier) 

        print(dictionnaire)
