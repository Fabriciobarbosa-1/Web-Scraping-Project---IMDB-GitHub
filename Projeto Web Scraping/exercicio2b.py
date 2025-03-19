import requests
from requests.exceptions import HTTPError
from bs4 import BeautifulSoup

# URL da página
URL = "https://www.imdb.com/chart/top/"

# Definição de headers para evitar bloqueios do servidor
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

conteudo = ""  # Inicializa a variável para evitar erro de escopo

try:
    resposta = requests.get(URL, headers=HEADERS)
    resposta.raise_for_status()  # Levanta erro se o status da resposta for ruim
    conteudo = resposta.text  # Captura o conteúdo HTML da página
except HTTPError as http_err:
    print(f"Erro HTTP: {http_err}")
except Exception as err:
    print(f"Outro erro: {err}")

# Se o conteúdo foi carregado corretamente, processa com BeautifulSoup
if conteudo:
    soup = BeautifulSoup(conteudo, "html.parser")
    linhas_filmes = soup.select("tbody.lister-list tr")[:10]  # Seleciona os 10 primeiros filmes
    print(f"Extraídos {len(linhas_filmes)} filmes com sucesso.")
else:
    print("Falha ao carregar a página.")
