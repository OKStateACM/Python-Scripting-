import requests 
from bs4 import BeautifulSoup 
import sqlite3, sql

URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib')

pokemon_list = []
table = soup.find('table', attrs = {'align':'center'}) 
pokemon_info = table.findAll('tr', attrs = {'style': 'background:#FFF'})



for row in pokemon_info:
    pokemon = {'RegionalDex': "", 'NationalDex': "",
                'Name': "", 'Primary Type': "", 'Secondary Type': ""}

    count = 1

    for indiv_info in row.findAll('td'):
        if count == 1:
            pokemon['RegionalDex'] = indiv_info.text
        if count == 2:
            pokemon['NationalDex'] = indiv_info.text
        if count == 4:
            pokemon['Name'] = indiv_info.text
        if count == 5:
            pokemon['Primary Type'] = indiv_info.text
        if count == 6:
            pokemon['Secondary Type'] = indiv_info.text
        count = count +1
    pokemon_list.append(pokemon)    

sql.insert_pokemon(pokemon_list)
