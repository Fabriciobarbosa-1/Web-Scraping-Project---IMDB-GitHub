import requests
from requests.exceptions import HTTPError

URL = "https://www.imdb.com/chart/top/"

# Definição dos cabeçalhos para simular um navegador real
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.5",
}

try:
    resposta = requests.get(URL, headers=HEADERS)
    resposta.raise_for_status()  # Verifica se houve erro HTTP
    conteudo = resposta.text  # Salva o HTML da página
    print("Página carregada com sucesso!")
except HTTPError as http_err:
    print(f"Erro HTTP: {http_err}")
except Exception as err:
    print(f"Outro erro: {err}")

# Exibir os primeiros caracteres do conteúdo para testar
print(conteudo[:500] if conteudo else "Falha ao carregar a página.")