import requests
from bs4 import BeautifulSoup


def scrape_amazon_basic_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.3'
    }
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('span', {'id': 'productTitle'}).text().strip()
    price = soup.find('span', {'class': 'a-offscreen'}).text().strip()

    return {
        'title': title,
        'price': price
    }


url = "https://www.amazon.com/dp/B00UXG4WR8"
print(scrape_amazon_basic_info(url))