import mysql.connector
import os
from sql import config_file


conn = mysql.connector.connect(host="localhost",
                               database="APIDevelop",
                               user=os.environ["user"],
                               password=os.environ["password"])
print(conn.is_connected())  # True if connected
cursor = conn.cursor()
cursor.execute("select * from CustomerInfo")
# fetching the one record from the cursor position
# first_row = cursor.fetchone()
# print(first_row)    # ('selenium', datetime.date(2021, 2, 6), 120, 'Africa')
# print(first_row[3])     # Africa

# fetch all the records from cursor position
all_records = cursor.fetchall()
print(all_records)

sum_amount = 0
for record in all_records:
    sum_amount += record[2]

print(sum_amount)

conn.close()
