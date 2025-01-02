import requests

url = "https://www.amazon.com/Magnesium-Oil-Feet-Absorb-Suitable/dp/B0DL3897NN/ref=sr_1_1?crid=KR1U36ZS0VIW&dib=eyJ2IjoiMSJ9.Jd6vO0mW5pM_1fki5BZPmApTx-3KyoBZztfVO-dZe3KsRVicx6yqKOeJyN0tB-60ACmK_wQE9QZ4I5exFFlpkzF5GNpfb_Rsk4ml4kShgBUG81wOOwgXvcV-GoJHQ1mMuhd4Ul6oNjk1SlJgUcoT5WPhjhCE4s6mU6k8wn5H4DJf1YJyXweCikLGoh9fyMoEvNVHUUDpu1dg0Hy6wa4YXUcsvzLX-GC4K3jlZ4aEXPg7DTFMYxhb4y9SwMglN6SYVL5GVyfdbung5abCNqHgyhWJL_Vyfp4ktAjJ5XC-CTwEU-pYHNd6bz6e9ER62SJZBfFuuHecA7JiQWph7Riw51d85QezDrb5y7cehScn6c96oSZEb6KrLA02iPRuTBHJHowY7tydrhC1-1hSK2jN6JmJ91nWgAJDPrHtlNgZXeUjOEa73hTigjfwWQQqGsoR.OmJxCSjIBd7FbsZwjhqfJlvsta-Oe-hGfeMs3wQPKzw&dib_tag=se&keywords=Magnesiums+Oil+For+Soothing+Massage+And+Easy+Absorption+60ml&qid=1734944865&sprefix=magnesiums+oil+for+soothing+massage+and+easy+absorption+60ml%2Caps%2C720&sr=8-1"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    print(r.text[1000:2000])
except:
    print("爬取失败")


