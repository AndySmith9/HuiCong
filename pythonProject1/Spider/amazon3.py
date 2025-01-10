from urllib.error import HTTPError

import requests
from pyquery import PyQuery

def fetch_amazon_data(url):
    result = False
    title = ""
    price = []
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}

    response = requests.get(url, headers=headers)
    #soup = BeautifulSoup(response.content, 'html.parser')
    try:
        doc = PyQuery(url=url)
        # 提取商品标题
        # title = soup.find(id='productTitle').get_text(strip=True)
        title = doc('#productTitle').text()
        # 提取商品价格
        # price = soup.find('span', class_='a-price-whole').get_text(strip=True)
        # price = doc('#corePriceDisplay_desktop_feature_div .a-price-whole').text()
        price = doc('.a-unordered-list.a-vertical.a-spacing-mini span').items()
        result = True

    except HTTPError:
        print("HTTPError")
    return result, title, price



#url = "https://www.amazon.com/Wellness-Workbook-Exploration-Relaxation-Check-ins/dp/B07TJK2GBF/ref=hw_25_nyn_dag_b_0eec?pf_rd_p=072584ad-9485-4bf9-8ab6-a26e5abe7a18&pf_rd_r=78E2XAKJ34355Q8EJWVZ&sr=1-1-60d284ff-6ab2-4a43-be72-ccdccd088957&th=1"
#url = "https://www.amazon.com/Wellness-Workbook-Exploration-Relaxation-Check-ins/dp/B07TJK2GBF"
#url = "https://www.amazon.com/dp/B07TJK2GBF"
#url = "https://www.amazon.com/dp/B09PR9R9SL"
#url = "https://www.amazon.com/dp/B07YDDX4JL"
#url = "https://www.amazon.com/dp/B0CHTZD63Q"
#url = "https://www.amazon.com/dp/B0DDTHYKSW"
#url = "https://www.amazon.com/dp/B00UXG4WR8"
#
#
#
#上面url可以爬取
#下面url不可以爬取
#url = "https://www.amazon.com/dp/B0BXCHXFQ7"
#url = "https://www.amazon.com/dp/B09DXYNWQT"
#url = "https://www.amazon.com/dp/B07FNXPGLG"
#url = "https://www.amazon.com/dp/B0B2LRRH1K"
#
#

url = "https://www.amazon.com/dp/B0DDTHYKSW"
result, title, price = fetch_amazon_data(url)
if result:
    print(f"商品标题: {title}")
    print(f"商品价格: {price}"+",长度为"+f"{len(list(price))}")
    for item in price:
        print(item.text())
else:
    print("程序异常,请查询原因")


"""
TypeError: cannot unpack non-iterable NoneType object
TypeError: object of type 'generator' has no len()
python之generator详解
"""


