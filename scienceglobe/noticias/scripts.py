import requests
from bs4 import BeautifulSoup
from .models import NoticiaWeb

def scrape_noticias():
    url = "https://g1.globo.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    for noticia in soup.find_all('div', class_='feed-post-body'):
        
    
        titulo = noticia.find('a', class_='feed-post-link').text.strip()
        link = noticia.find('a', class_='feed-post-link')['href']
        corpo = ""

        # Extração do corpo da notícia
        response_noticia = requests.get(link)
        soup_noticia = BeautifulSoup(response_noticia.text, 'html.parser')
        corpo_elements = soup_noticia.find_all(class_="content-text__container")
        for element in corpo_elements:
            corpo += element.get_text().strip() + "\n"

        NoticiaWeb.objects.create(titulo=titulo, link=link, corpo=corpo)

            
