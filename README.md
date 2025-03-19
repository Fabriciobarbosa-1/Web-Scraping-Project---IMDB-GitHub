# 📊 Web Scraping Project - IMDB & GitHub

This project utilizes Python, Requests, and BeautifulSoup to extract information from IMDB's top 10 movies and GitHub's 10 most popular repositories, saving the data in CSV files.

## 📌 Features
✅ Extraction of the 10 highest rated movies from IMDB 

✅ Extracting the 10 most popular GitHub repositories

✅ Generation of CSV files with the extracted data

✅ Use of headers to avoid blocking when accessing pages

## 🛠 Technologies Used
Python 3.x

Requests (to download web pages)

BeautifulSoup (to extract the data from the HTML)

CSV (to save the extracted data)
📂 Project Structure
```
📁 projeto-web-scraping
│── 📄 exercicio2a.py  # Faz a requisição ao IMDB
│── 📄 exercicio2b.py  # Extrai os 10 filmes mais populares do IMDB
│── 📄 exercicio2c.py  # Processa e estrutura os dados do IMDB
│── 📄 exercicio2d.py  # Salva os filmes extraídos no CSV
│── 📄 ProjetoGitHub.py  # Extrai os 10 repositórios mais populares do GitHub
│── 📄 robots.py  # Verifica regras de acesso do site IMDB
│── 📄 Filmes Top10 IMDB.csv  # Arquivo CSV com os filmes extraídos
│── 📄 Melhores Projetos GR.csv  # Arquivo CSV com os projetos do GitHub
```
## 🚀 How to Run
1. Clone the repository

```
git clone https://github.com/seu-usuario/projeto-web-scraping.git
cd projeto-web-scraping
Instale as dependências
```

2. Install the dependencies
```
pip install requests beautifulsoup4
```

3. Run the scripts

Extract the movies from IMDB
```
python exercicio2d.py
```
Pulling your GitHub repositories
```
python ProjetoGitHub.py
```
4. Check the generated CSV files!

## 📈 Findings
The extracted data will be saved in CSV files with the following format:

### Filmes IMDB (Filmes Top10 IMDB.csv)
```
ranking;titulo;ano;nota
1;The Shawshank Redemption;1994;9.2
2;The Godfather;1972;9.1
3;The Dark Knight;2008;9.0
...
```
### Projetos GitHub (Melhores Projetos GR.csv)
```
ranking;project;language;stars;stars_today;forks
1;the-book-of-secret-knowledge;;44502;692;4685
2;whynotwin11;autoit;2242;1585;117
3;lede;c;16732;66;14317
...
```

## 🔥 Future Improvements
🚀 Create an interactive dashboard to visualize the data

🚀 Schedule automatic data extraction on a daily basis

🚀 Add support for other data sources.

Create by Fabriciobarbosa-1
