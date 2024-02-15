import requests
from bs4 import BeautifulSoup


def get_nombre_total_titre(tickers) : 

    url = f'https://www.boursorama.com/cours/societe/profil/1rP{tickers}/'
    #print(url)


    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    titre_li = soup.find("p", class_="c-list-info__heading", string=lambda t: "Nombre de titres" in t).find_parent("li")


    nombre_de_titres_value = titre_li.find("p", class_="c-list-info__value").text.strip()

    return int('_'.join(nombre_de_titres_value.split(' ')))




if __name__ == '__main__':

    tickers ='CO'
    nombre_de_titres_value = get_nombre_total_titre(tickers)
    print('nombre_de_titres : ' ,nombre_de_titres_value )

    