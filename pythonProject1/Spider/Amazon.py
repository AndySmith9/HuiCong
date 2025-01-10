from pyquery import PyQuery


def get_amazon(url1):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.3'
    }
    doc = PyQuery(url=url1, headers=headers)
    title1 = doc('#productTitle').text()
    key_feathers1 = doc('#feature-bullets .a-unordered-list a-vertical a-spacing-mini span').items()
    return title1, key_feathers1

def get_test(url1):
    doc = PyQuery(url=url1)
    title1 = doc('title').text()
    key_feathers1 = doc('p').items()
    return title1, key_feathers1
"""   
url = 'https://cloud.tencent.com/developer/article/2032018'
title, key_feathers = get_test(url)
"""
url = 'https://www.amazon.com/dp/B0B2LRRH1K'
title, key_feathers = get_amazon(url)


print(title)
for key_feather in key_feathers:
    print(key_feather.text())
