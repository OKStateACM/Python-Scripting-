# Python Scripting

## Web Scraping
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites. Web scraping software may access the World Wide Web directly using the Hypertext Transfer Protocol, or through a web browser. For this project, we will be using the following python packages: requests, html5lib, and bs4.

###Setting up the project
```python3
import requests 
from bs4 import BeautifulSoup 
import sqlite3, sql

URL = "https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number"
r = requests.get(URL) 
soup = BeautifulSoup(r.content, 'html5lib')
```

This code retrieves all of the HTML data from Bulbapedia's list of Pokemon and formats it for us.

So how do we parse through the webpage to only get the data that we need?
```python3
pokemon_list = []
table = soup.find('table', attrs = {'align':'center'}) 
pokemon_info = table.findAll('tr', attrs = {'style': 'background:#FFF'})
```
And finally, we need to clean up the data. We'll do this iteratively.
```python3
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
```

##sqlite3
SQLite is a C library that provides a lightweight disk-based database that doesn’t require a separate server process and allows accessing the database using a nonstandard variant of the SQL query language. sqlite3 is a Python package that allows us to us SQLite's features from within our code.

The first step is to create our database and the table that the Pokemon information will go into.
```python3
import sqlite3

conn = sqlite3.connect('test.db')
crsr = conn.cursor() 


sql_command = '''CREATE TABLE IF NOT EXISTS pokemon(  
national_dex VARCHAR(4),
regional_dex VARCHAR(4),
name VARCHAR(20),  
primary_type VARCHAR(30),  
secondary_type VARCHAR(30));'''

crsr.execute(sql_command)
```
Now that we have created the "pokemon" table, we need to insert our data into the table.
```python3
def insert_pokemon(pokemon_list):
    conn = sqlite3.connect('test.db')
    c = conn.cursor()

    sql = ''' INSERT INTO pokemon(national_dex,regional_dex,
                name,primary_type,secondary_type)
              VALUES(?,?,?,?,?) '''

    for pokemon in pokemon_list:
        c.execute(sql, (pokemon['NationalDex'], pokemon['RegionalDex'], 
                pokemon['Name'], pokemon['Primary Type'], pokemon['Secondary Type']))
    conn.commit()  
```

Now that we have all of the individual parts completed, all we need to do is call the insert_pokemon function from our scripting file.
```python3
sql.insert_pokemon(pokemon_list)
```
