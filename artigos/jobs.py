import requests
from bs4 import BeautifulSoup
from .models import ArtigoWeb, Genero

def scrape_physical_sciences_and_engineering():
    try:
        url = "https://nautil.us/mind/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Supondo que você tenha um modelo chamado "ArtigoWeb" e um campo "genero" nele.
        # Você pode ajustar isso conforme necessário para o seu modelo real.
        genero_mind, _ = Genero.objects.get_or_create(name="Mind")

        # Encontrar os links para os artigos
        links = [a['href'] for a in soup.find_all('a', class_='card-block')]
        
        print(f"Total de links encontrados: {len(links)}")

        for link in links:
            try:
                # Acessar o link do artigo
                article_response = requests.get(link)
                article_response.raise_for_status()
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Pegar título do artigo
                titulo = article_soup.find('h1', class_='h1 article-title').text.strip()

                # Pegar corpo do texto
                corpo = ''
                paragraphs = article_soup.find_all('p')
                for p in paragraphs:
                    corpo += p.text.strip() + '\n'

                # Aqui você pode adicionar o código para salvar os dados no seu modelo.
                # ArtigoWeb.objects.create(title=titulo, genero=genero_mind, corpo=corpo)
                print(f"Artigo: ({titulo}) adicionado.")

            except Exception as e:
                print(f"Erro ao acessar o artigo: {e}")

    except Exception as e:
        print(f"Erro ao acessar a página: {e}")

def scrape_cultura():
    try:
        url = "https://nautil.us/culture/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Supondo que você tenha um modelo chamado "ArtigoWeb" e um campo "genero" nele.
        # Você pode ajustar isso conforme necessário para o seu modelo real.
        genero_mind, _ = Genero.objects.get_or_create(name="Mind")

        # Encontrar os links para os artigos
        links = [a['href'] for a in soup.find_all('a', class_='card-block')]
        
        print(f"Total de links encontrados: {len(links)}")

        for link in links:
            try:
                # Acessar o link do artigo
                article_response = requests.get(link)
                article_response.raise_for_status()
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Pegar título do artigo
                titulo = article_soup.find('h1', class_='h1 article-title').text.strip()

                # Pegar corpo do texto
                corpo = ''
                paragraphs = article_soup.find_all('p')
                for p in paragraphs:
                    corpo += p.text.strip() + '\n'

                # Aqui você pode adicionar o código para salvar os dados no seu modelo.
                # ArtigoWeb.objects.create(title=titulo, genero=genero_mind, corpo=corpo)
                print(f"Artigo: ({titulo}) adicionado.")

            except Exception as e:
                print(f"Erro ao acessar o artigo: {e}")

    except Exception as e:
        print(f"Erro ao acessar a página: {e}")

def scrape_saude():
    try:
        url = "https://nautil.us/topics/health/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Supondo que você tenha um modelo chamado "ArtigoWeb" e um campo "genero" nele.
        # Você pode ajustar isso conforme necessário para o seu modelo real.
        genero_mind, _ = Genero.objects.get_or_create(name="Mind")

        # Encontrar os links para os artigos
        links = [a['href'] for a in soup.find_all('a', class_='card-block')]
        
        print(f"Total de links encontrados: {len(links)}")

        for link in links:
            try:
                # Acessar o link do artigo
                article_response = requests.get(link)
                article_response.raise_for_status()
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Pegar título do artigo
                titulo = article_soup.find('h1', class_='h1 article-title').text.strip()

                # Pegar corpo do texto
                corpo = ''
                paragraphs = article_soup.find_all('p')
                for p in paragraphs:
                    corpo += p.text.strip() + '\n'

                # Aqui você pode adicionar o código para salvar os dados no seu modelo.
                # ArtigoWeb.objects.create(title=titulo, genero=genero_mind, corpo=corpo)
                print(f"Artigo: ({titulo}) adicionado.")

            except Exception as e:
                print(f"Erro ao acessar o artigo: {e}")

    except Exception as e:
        print(f"Erro ao acessar a página: {e}")


def scrape_meio_tec():
    try:
        url = "https://nautil.us/topics/technology/"
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        # Supondo que você tenha um modelo chamado "ArtigoWeb" e um campo "genero" nele.
        # Você pode ajustar isso conforme necessário para o seu modelo real.
        genero_mind, _ = Genero.objects.get_or_create(name="Mind")

        # Encontrar os links para os artigos
        links = [a['href'] for a in soup.find_all('a', class_='card-block')]
        
        print(f"Total de links encontrados: {len(links)}")

        for link in links:
            try:
                # Acessar o link do artigo
                article_response = requests.get(link)
                article_response.raise_for_status()
                article_soup = BeautifulSoup(article_response.text, 'html.parser')

                # Pegar título do artigo
                titulo = article_soup.find('h1', class_='h1 article-title').text.strip()

                # Pegar corpo do texto
                corpo = ''
                paragraphs = article_soup.find_all('p')
                for p in paragraphs:
                    corpo += p.text.strip() + '\n'

                # Aqui você pode adicionar o código para salvar os dados no seu modelo.
                # ArtigoWeb.objects.create(title=titulo, genero=genero_mind, corpo=corpo)
                print(f"Artigo: ({titulo}) adicionado.")

            except Exception as e:
                print(f"Erro ao acessar o artigo: {e}")

    except Exception as e:
        print(f"Erro ao acessar a página: {e}")