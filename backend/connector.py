import datetime
import mysql.connector

__cnx = None

#create an sql connection to our database

def get_sql_connection():
  print("Opening mysql connection")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='root', database='grocery_store')

  return __cnx
