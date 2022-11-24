import mysql.connector
from getpass import getpass

_dbData = ["root", "localhost", ""]

_dbData[2] = getpass("Enter password for '"+ _dbData[0] +"'@'"+ _dbData[1] +"': ")

_database = mysql.connector.connect(
	user	 = _dbData[0],
	host	 = _dbData[1],
	password = _dbData[2]
)
cursor = _database.cursor()

_user = _dbData[0]
_pass = _dbData[2]