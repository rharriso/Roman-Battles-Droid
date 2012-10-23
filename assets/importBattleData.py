#!/usr/bin/env python

import csv
import sqlite3

battleDataReader    = csv.reader(open('RomanBattles.csv'))
conn                = sqlite3.connect('romanBattles.sqlite') 
battleDBcursor      = conn.cursor()

for row in battleDataReader:
    Date            = row[0]
    Year            = row[1]
    BattleName      = row[2]
    Location        = row[3]
    Result          = row[4]
    Coordinates     = row[5]
    RomanCommanders = row[6]
    EnemyCommanders = row[7]
    RomanAllies     = row[8]
    EnemyAllies     = row[9]
    RomanStrength   = row[10]
    EnemyStrength   = row[11]
    RomanLosses     = row[12]
    EnemyLosses     = row[13]
    civil           = row[14]
    naval           = row[15]

    #insert battle
    battle_query = 'INSERT INTO Battles \
    (battle_name, year, date, Result, \
    coalition0_victory, location, \
    civil, naval, coordinates) \
    values  ("'+BattleName+'", "'+Year+'", \
    "'+Date+'", "'+Result+'", "1", "'+Location+'", \
    "'+civil+'", "'+naval+'", "'+Coordinates+'")'
    
    battleDBcursor.execute(battle_query)  
    battle_id = battleDBcursor.lastrowid
    
    #insert coalition 0
    coatlition0 = RomanAllies.split(";");
    for belligerant in coatlition0:
        
        #insert belligerant
        belligerant_query = 'INSERT INTO Belligerants (name) values ("'+belligerant+'")'
        battleDBcursor.execute(battle_query)
        belligerant_id = battleDBcursor.lastrowid
        
        #insert belligerant battle
        belligerant_battle_query = 'INSERT INTO BattleBelligerents (battle_id, belligerent_id, coalition0, strength, losses)\
        values ("'+str(battle_id)+'", "'+str(belligerant_id)+'", "true", "'+str(RomanStrength)+'", "'+str(EnemyStrength)+'")'
        
        battleDBcursor.execute(belligerant_battle_query)
        belligerant_battle_id = battleDBcursor.lastrowid
        
        coatlitionCommanders = RomanCommanders.split(";")
        for commander in coatlitionCommanders:
            
            if(commander != ""):
                commander_query = 'INSERT INTO Commanders (name) VALUES ("'+commander+'")'
                battleDBcursor.execute(commander_query)
                commander_id = battleDBcursor.lastrowid
                
                commander_battle_query = 'INSERT INTO CommanderBattles (commander_id, battle_belligerent_id)\
                values ("'+str(commander_id)+'", "'+str(belligerant_battle_id)+'")'
                battleDBcursor.execute(commander_battle_query)
                
    
    #insert coalition 1
    coatlition1 = EnemyAllies.split(";");
    for belligerant in coatlition1:
        
        #insert belligerant
        belligerant_query = 'INSERT INTO Belligerents (name) values ("'+belligerant+'")'
        battleDBcursor.execute(belligerant_query)
        belligerant_id = battleDBcursor.lastrowid
        print belligerant_query
        
        #insert belligerant battle
        belligerant_battle_query = 'INSERT INTO BattleBelligerents (battle_id, belligerent_id, coalition0, strength, losses)\
        values ("'+str(battle_id)+'", "'+str(belligerant_id)+'", "true", "'+str(EnemyStrength)+'", "'+str(EnemyStrength)+'")'
        battleDBcursor.execute(belligerant_battle_query)
        belligerant_battle_id = battleDBcursor.lastrowid
        
        coatlitionCommanders = EnemyCommanders.split(";")
        for commander in coatlitionCommanders:
            
            if(commander != ""):
                commander_query = 'INSERT INTO Commanders (name) VALUES ("'+commander+'")'
                battleDBcursor.execute(commander_query)
                commander_id = battleDBcursor.lastrowid
                
                commander_battle_query = 'INSERT INTO CommanderBattles (commander_id, battle_belligerent_id)\
                values ("'+str(commander_id)+'", "'+str(belligerant_battle_id)+'")'
                battleDBcursor.execute(commander_battle_query)
                

conn.commit()
battleDBcursor.close()
