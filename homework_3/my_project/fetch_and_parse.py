import requests
from bs4 import BeautifulSoup
def fetch_and_parse(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        print(f"Заголовок страницы: {soup.title.string}")
        links = soup.find_all('a')
        print("Ссылки на странице:")
        for link in links:
            print(link.get('href'))
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении данных: {e}")
url = "https://example.com"
fetch_and_parse(url)

