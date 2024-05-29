import mysql.connector

# should add three params, your host, password, username
mydb = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="root",
    password="password",
    database="db"
)
print(mydb)