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