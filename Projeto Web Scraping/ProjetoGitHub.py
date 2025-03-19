import requests
from bs4 import BeautifulSoup
import csv

# URL da página de tendências do GitHub
URL = "https://github.com/trending"

# Definição de headers para evitar bloqueios
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

conteudo = ""

try:
    resposta = requests.get(URL, headers=HEADERS)
    resposta.raise_for_status()
    conteudo = resposta.text
except requests.RequestException as err:
    print(f"Erro na requisição: {err}")

# Processamento com BeautifulSoup
conteudo_extraido = []

if conteudo:
    pagina = BeautifulSoup(conteudo, "html.parser")
    projetos = pagina.select("article.Box-row")[:10]  # Seleciona os 10 primeiros projetos

    for i, projeto in enumerate(projetos, start=1):
        # Nome do projeto (usuário/repositorio)
        nome = projeto.h2.a.get_text(strip=True).replace("\n", "").replace(" ", "")

        # Linguagem do projeto
        linguagem = projeto.select_one("span[itemprop='programmingLanguage']")
        linguagem = linguagem.get_text(strip=True) if linguagem else ""

        # Número de estrelas
        estrelas = projeto.select("a.Link")[-2].get_text(strip=True).replace(",", "")

        # Estrelas recebidas hoje
        estrelas_hoje = projeto.select_one("span.d-inline-block.float-sm-right")
        estrelas_hoje = estrelas_hoje.get_text(strip=True).split(" ")[0].replace(",", "") if estrelas_hoje else "0"

        # Número de forks
        forks = projeto.select("a.Link")[-1].get_text(strip=True).replace(",", "")

        conteudo_extraido.append([i, nome, linguagem, estrelas, estrelas_hoje, forks])

    # Escrevendo no arquivo CSV
    with open("github.csv", "w", newline="", encoding="utf-8") as arquivo_csv:
        escritor = csv.writer(arquivo_csv, delimiter=";")
        escritor.writerow(["ranking", "project", "language", "stars", "stars_today", "forks"])
        escritor.writerows(conteudo_extraido)

    print("Arquivo github.csv criado com sucesso!")
else:
    print("Falha ao carregar a página.")
