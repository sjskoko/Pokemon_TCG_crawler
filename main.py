import requests
from bs4 import BeautifulSoup as bs

page = requests.get(
    "https://www.pokemon.com/us/pokemon-tcg/pokemon-cards/?cardName=&cardText=&evolvesFrom=&format=unlimited&hitPointsMin=0&hitPointsMax=340&retreatCostMin=0&retreatCostMax=5&totalAttackCostMin=0&totalAttackCostMax=5&particularArtist=&sort=name&sort=name"
    )


soup = bs(page.text, "html.parser")


pokemon_structure = soup.find('ul', class_='cards-grid clear').find_all('a')

pokemon_link = [pokemon_structure[i]['href'] for i in range(len(pokemon_structure))]

next_link = soup.find('div', id='cards-load-more').find_all('a')[1]['href']
now_link = soup.find('div', id='cards-load-more').find_all('span')[1].text
print(pokemon_link)

main_address = 'https://www.pokemon.com/'


for _ in range(1064):
    print('d')
    page = requests.get(main_address + next_link)
    soup = bs(page.text, 'html.parser')
    pokemon_structure = soup.find('div', class_='column-12 push-1 card-results-anchor').find('ul', class_='cards-grid clear').find_all('a')
    pokemon_link.append([pokemon_structure[i]['href'] for i in range(len(pokemon_structure))])
    next_link = soup.find('div', id='cards-load-more').find_all('a')[0]['href']
    now_page_text = soup.find('div', id='cards-load-more').find_all('span')[1].text
    print(now_page_text)
    print()


len(pokemon_link)


