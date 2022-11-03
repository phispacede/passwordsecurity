import mysql.connector
import hashlib
import names
import random
import string

charsetlist = [string.ascii_lowercase,
               string.ascii_uppercase,
               string.ascii_letters,
               string.digits,
               string.ascii_lowercase + string.digits,
               string.ascii_letters + string.digits ]

commonlist = []

def usergenerator():
    firstname = names.get_first_name()
    lastname = names.get_last_name()
    email = firstname + "." + lastname + "@phispace.de"
    pw = ""
    pwmethode = random.randint(0, 1)
    if pwmethode == 0:
        pw = ''.join(random.choices(random.choice(charsetlist), k = random.randint(4, 10)))
    if pwmethode == 1:
        pw = random.choice(commonlist)
    return (email, hashlib.sha512(pw.encode()).hexdigest())

with open("common10000.txt") as file:
    commonlist = [line.rstrip() for line in file]

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="pwd",
  database="db_hacking"
)

mycursor = mydb.cursor()

sql = "DELETE FROM users"

mycursor.execute(sql)

sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
val = []

for i in range(100):
    val.append(usergenerator())

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")
