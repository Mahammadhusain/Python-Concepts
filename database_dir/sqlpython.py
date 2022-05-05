# Make Connection with database
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

# print(mydb)
# """


# Show/Create Database 
"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
"""
import mysql.connector

# -------- Create database -----------
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
  
# )

# mycursor = mydb.cursor() # Mysql query executor

# try:
#   mycursor.execute("CREATE DATABASE demo") # Create new database
# except:
#   print('Database already exist')




# -------- Create table in database -----------
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
#   database="demo" # Add database name for adding table in it
# )

# mycursor = mydb.cursor()
# try:
#   mycursor.execute("CREATE TABLE customers (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), address VARCHAR(255))")
# except:
#   print('Table already exist')



# -------- Create table in database -----------
# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
#   database="demo" # Running database name
# )

# mycursor = mydb.cursor()

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)

# mydb.commit() # Save data in table

# print(mycursor.rowcount, "record inserted.")

# -------- Show data from table -----------
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
#   database="demo" # Running database name
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT * FROM customers")

# myresult = mycursor.fetchall() # fetch all data from customer table

# a= []
# for x in myresult:
#   print(a.append(x))

# -------- Show data with specific column -----------
# import mysql.connector

# mydb = mysql.connector.connect(
#   host="localhost",
#   user="root",
#   password="password",
#   database="demo" # Running database name
# )

# mycursor = mydb.cursor()

# mycursor.execute("SELECT name, address FROM customers") # only show data of (name, address) not (id)

# myresult = mycursor.fetchall()

# for x in myresult:
#   print(x)