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

# Processamento com BeautifulSoup
if conteudo:
    pagina = BeautifulSoup(conteudo, "html.parser")
    movies = pagina.find_all("li", class_="ipc-metadata-list-summary-item")

    conteudo_extraido = []

    for coluna in movies[:10]:
        textos_coluna = coluna.get_text(";").strip().split(";")
        ranking = textos_coluna[0].split(".")[0]  # Número do ranking
        titulo = textos_coluna[0].split(".")[1].strip()  # Título do filme
        ano = textos_coluna[1]  # Ano do filme
        nota = textos_coluna[4]  # Nota do filme

        conteudo_extraido.append([ranking, titulo, ano, nota])

    for filme in conteudo_extraido:
        print(filme)
else:
    print("Falha ao carregar a página.")
