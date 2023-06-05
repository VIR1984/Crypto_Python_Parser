
import requests
from bs4 import BeautifulSoup
import json
import re

coin_url_list = []

data_title_dict = {}

for i in range(1, 10, 1):  # 333
    url = f"https://coindataflow.com/ru/%D1%82%D0%BE%D1%80%D0%B3%D0%BE%D0%B2%D1%8B%D0%B5-%D0%BF%D0%B0%D1%80%D1%8B/page/{i}"
    # print(url)

    q = requests.get(url)
    result = q.content

    soup = BeautifulSoup(result, 'lxml')
    results = soup.find_all(name='a', attrs={'data-title': True})

    for res in results:
        data_title = res['data-title']
        format_data_key = re.sub(r'\bUSD\b', 'USDT', data_title.replace('/', ''))

        format_data_value = re.sub(r'\bUSD\b', 'USDT', data_title.replace('/', '-'))

        data_title_dict[format_data_key] = format_data_value

with open('data_coin_titles.json', 'w') as file:
    json.dump(data_title_dict, file, indent=4)
