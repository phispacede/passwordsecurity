import mysql.connector
import hashlib

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pwd",
  database="db_hacking"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT username, password FROM users")

myresult = mycursor.fetchall()

res = []
for x in myresult:
  res.append(x[0] + ":" + x[1] + "\n")

f = open("users_hashed.txt", "w")
f.writelines(res)
f.close()
