import requests

URL = "https://www.imdb.com/robots.txt"


def fetch_robots_txt(url):
    #Faz o download do conteúdo do arquivo robots.txt de um site.#
    response = requests.get(url, timeout=10)
    return response.text


def check_keywords(content, keywords):
    #Verifica se alguma das palavras-chave está presente no conteúdo.#
    return any(word in content for word in keywords)


if __name__ == "__main__":
    robots = fetch_robots_txt(URL)
    keywords = {"top", "charts"}
    print(check_keywords(robots, keywords))