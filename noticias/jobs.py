import requests
from bs4 import BeautifulSoup
from .models import NoticiaWeb, Genero

def scrape_economia():
    try:
        url = "https://g1.globo.com/economia"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        genero_economia, _ = Genero.objects.get_or_create(name="Economia")

        noticias = soup.find_all('div', class_='feed-post-body')
        print(f"Total de notícias encontradas: {len(noticias)}")

        for noticia in soup.find_all('div', class_='feed-post-body'):
            try:
                titulo = noticia.find('a', class_='feed-post-link').text.strip()
                link = noticia.find('a', class_='feed-post-link')['href']
                corpo = ""

                # Extração do corpo da notícia
                response_noticia = requests.get(link)
                response_noticia.raise_for_status()
                soup_noticia = BeautifulSoup(response_noticia.text, 'html.parser')
                corpo_elements = soup_noticia.find_all(class_="content-text__container")
                for element in corpo_elements:
                    corpo += element.get_text().strip() + "\n"
                
                if NoticiaWeb.objects.filter(title=titulo).exists():
                    print(f"Noticia: ({titulo}) já existe.")
                else:
                    NoticiaWeb.objects.create(title=titulo, genero=genero_economia, corpo=corpo)
                    print(f"Noticia: ({titulo}) adicionada.")

            except Exception as e:
                print(f"Erro ao pegar dados da noticia: {titulo}\n{e}")

    except Exception as e:
        print(f"Erro ao acessar a notícia: {e}")


def scrape_tecnologia():
    try:
        url = "https://g1.globo.com/tecnologia/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        genero_tecnologia, _ = Genero.objects.get_or_create(name="Tecnologia")

        noticias = soup.find_all('div', class_='feed-post-body')
        print(f"Total de notícias encontradas: {len(noticias)}")

        for noticia in soup.find_all('div', class_='feed-post-body'):
            try:
                titulo = noticia.find('a', class_='feed-post-link').text.strip()
                link = noticia.find('a', class_='feed-post-link')['href']
                corpo = ""

                # Extração do corpo da notícia
                response_noticia = requests.get(link)
                response_noticia.raise_for_status()
                soup_noticia = BeautifulSoup(response_noticia.text, 'html.parser')
                corpo_elements = soup_noticia.find_all(class_="content-text__container")
                for element in corpo_elements:
                    corpo += element.get_text().strip() + "\n"
                
                if NoticiaWeb.objects.filter(title=titulo).exists():
                    print(f"Noticia: ({titulo}) já existe.")
                else:
                    NoticiaWeb.objects.create(title=titulo, genero=genero_tecnologia, corpo=corpo)
                    print(f"Noticia: ({titulo}) adicionada.")

            except Exception as e:
                print(f"Erro ao pegar dados da noticia: {titulo}\n{e}")

    except Exception as e:
        print(f"Erro ao acessar a notícia: {e}")


def scrape_ciencias():
    try:
        url = "https://g1.globo.com/ciencia/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        genero_ciencias, _ = Genero.objects.get_or_create(name="Ciências")

        noticias = soup.find_all('div', class_='feed-post-body')
        print(f"Total de notícias encontradas: {len(noticias)}")

        for noticia in soup.find_all('div', class_='feed-post-body'):
            try:
                titulo = noticia.find('a', class_='feed-post-link').text.strip()
                link = noticia.find('a', class_='feed-post-link')['href']
                corpo = ""

                response_noticia = requests.get(link)
                response_noticia.raise_for_status()
                soup_noticia = BeautifulSoup(response_noticia.text, 'html.parser')
                corpo_elements = soup_noticia.find_all(class_="content-text__container")
                for element in corpo_elements:
                    corpo += element.get_text().strip() + "\n"
                
                if NoticiaWeb.objects.filter(title=titulo).exists():
                    print(f"Noticia: ({titulo}) já existe.")
                else:
                    NoticiaWeb.objects.create(title=titulo, genero=genero_ciencias, corpo=corpo)
                    print(f"Noticia: ({titulo}) adicionada.")

            except Exception as e:
                print(f"Erro ao pegar dados da noticia: {titulo}\n{e}")

    except Exception as e:
        print(f"Erro ao acessar a notícia: {e}")


def scrape_meio_ambiente():
    try:
        url = "https://g1.globo.com/meio-ambiente/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        genero_meio_ambiente, _ = Genero.objects.get_or_create(name="Meio Ambiente")

        noticias = soup.find_all('div', class_='feed-post-body')
        print(f"Total de notícias encontradas: {len(noticias)}")

        for noticia in soup.find_all('div', class_='feed-post-body'):
            try:
                titulo = noticia.find('a', class_='feed-post-link').text.strip()
                link = noticia.find('a', class_='feed-post-link')['href']
                corpo = ""

                # Extração do corpo da notícia
                response_noticia = requests.get(link)
                response_noticia.raise_for_status()
                soup_noticia = BeautifulSoup(response_noticia.text, 'html.parser')
                corpo_elements = soup_noticia.find_all(class_="content-text__container")
                for element in corpo_elements:
                    corpo += element.get_text().strip() + "\n"
                
                if NoticiaWeb.objects.filter(title=titulo).exists():
                    print(f"Noticia: ({titulo}) já existe.")
                else:
                    NoticiaWeb.objects.create(title=titulo, genero=genero_meio_ambiente, corpo=corpo)
                    print(f"Noticia: ({titulo}) adicionada.")

            except Exception as e:
                print(f"Erro ao pegar dados da noticia: {titulo}\n{e}")

    except Exception as e:
        print(f"Erro ao acessar a notícia: {e}")
