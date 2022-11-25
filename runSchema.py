from dbStructure import db
from os import system

prefix = "proces_v."


cr = db.cursor
cr.execute("INSERT INTO VCS.dbCount () VALUES ();")
cr.execute("SELECT LAST_INSERT_ID();")
id = cr.fetchone()[0]
print(id)

dbName = prefix + str(id)
print(dbName)

cr.execute("CREATE DATABASE `"+ dbName +"` CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;")

system("mysql -u "+ db._user +" -p"+ db._pass +" -D "+ dbName +" --default-character-set=utf8mb4 < dbStructure\schema.sql")