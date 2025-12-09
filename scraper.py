# scraper.py
from requests import get
from bs4 import BeautifulSoup as bs
import pandas as pd

# Nombre de pages disponibles par catégorie
max_pages_available = {
    "chiens": 11,
    "moutons": 16,
    "poules-lapins-et-pigeons": 10,
    "autres-animaux": 6
}

# URLs par catégorie
category_urls = {
    "chiens": "https://sn.coinafrique.com/categorie/chiens?page=",
    "moutons": "https://sn.coinafrique.com/categorie/moutons?page=",
    "poules-lapins-et-pigeons": "https://sn.coinafrique.com/categorie/poules-lapins-et-pigeons?page=",
    "autres-animaux": "https://sn.coinafrique.com/categorie/autres-animaux?page="
}

def scrape_category(category, max_pages):
    """Scrape une catégorie CoinAfrique sur plusieurs pages"""

    data = pd.DataFrame()
    base_url = category_urls[category]

    for index_page in range(1, max_pages + 1):

        url = f"{base_url}{index_page}"
        res = get(url)

        # sécuriser la requête
        if res.status_code != 200:
            print("Erreur chargement page", url)
            continue

        soup = bs(res.content, 'html.parser')

        containers = soup.find_all('div', 'col s6 m4 l3')
        items = []

        for container in containers:
            try:
                name = container.find('p', 'ad__card-description').a.text  
                price = container.find('p', 'ad__card-price').text.replace("CFA", "").replace(" ", "")
                address = container.find('p', 'ad__card-location').text.replace("location_on", "")
                image_link = container.find('img', 'ad__card-img')['src']

                items.append({
                    "name": name,
                    "price": price,
                    "address": address,
                    "image_link": image_link
                })

            except:
                pass

        df = pd.DataFrame(items)
        data = pd.concat([data, df], axis=0).reset_index(drop=True)

    return data
