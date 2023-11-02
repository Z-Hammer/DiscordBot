import requests
from bs4 import BeautifulSoup

# https://nhentai.to
def haven(search):
    url = f'https://nhentai.to/search?q={search}'
    response = requests.get(url)
    
    # hh random
    if response.status_code == 200:
        links = []
        results_number = 0
        together = ''
        soup = BeautifulSoup(response.content, 'html.parser')
        results = soup.find_all("a")
        for result in results:
            if result.get('href')[0:3] == '/g/':
                links.append(f"https://nhentai.to{result.get('href')}")
                links.append(result.text.replace('\n', ''))
        for i in range(0, len(links)//2, 2):
            together = together + (f"{links[i]}, {links[i + 1]}\n")
            results_number += 1
        return (f"Search: {search}\n{together}Results: {results_number}")
    else:
        return(response.status_code)

#print(haven(search="boob"))