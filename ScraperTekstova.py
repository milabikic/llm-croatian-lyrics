import requests
from bs4 import BeautifulSoup
import re
import os
from urllib.parse import urljoin
from unidecode import unidecode

url = "https://cuspajz.com/tekstovi-pjesama/sve-pjesme/"
response = requests.get(url)
pattern = r'/tekstovi-pjesama/pjesma/[\w/]+'


if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    links = soup.find_all('a')
    os. makedirs("tekstovi", exist_ok=True)

    for link in links:
        if re.search(pattern, str(link)):
            link_url = link.get('href')
            link_response = requests.get(urljoin(url, link_url))

            if link_response.status_code == 200:
                link_soup = BeautifulSoup(link_response.text, "html.parser")
                stop_symbols = "/\\:?*<>:|\"\'"
                title = link_soup.find('title').get_text(strip=True)
                title = ''.join(char if char not in stop_symbols else '_' for char in title)
                title = unidecode(title[:-8])
                p_text = link_soup.find('p', class_='text clearfix').get_text()

                filename = f'tekstovi\\{title}.txt'

                try:
                    with open(filename, 'w', encoding='utf-8') as file:
                        file.write(f"{title}\n\n{p_text}\n")
                        print(f"Scraped and saved content from {link_url} to {filename}")
                except Exception as e:
                    print(f"An unexpected error occurred for {link}: {e}")
                    pass

            else:
                print(f"Failed to retrieve content from {link_url}. Status code: {link_response.status_code}")

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
