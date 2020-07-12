from mysql import connector as mc
from mysql.connector import errorcode as ec

from config import DB_DETAILS

db_details = DB_DETAILS['dev']

source_db = db_details['SOURCE_DB']
print(source_db)

print(source_db['DB_USER'],source_db['DB_PASS'],source_db['DB_HOST'], source_db['DB_NAME'])

connection = mc.connect(user=source_db['DB_USER'],password=source_db['DB_PASS'],host= source_db['DB_HOST'], database=source_db['DB_NAME'])

cursor = connection.cursor()

