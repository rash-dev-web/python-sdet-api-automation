import mysql.connector
from sql.config_file import read_config


host = read_config()["SQL"]["host"]
print(host)
conn = mysql.connector.connect(host=host,
                               database="APIDevelop",
                               user="root",
                               password="oi87^uey%648)lkOI")
conn.is_connected()

