import mysql.connector
from mysql.connector import errorcode

try:
  host = 'database-web-app-test-01.cujs843lupsc.us-west-1.rds.amazonaws.com'
  cnx = mysql.connector.connect(user='admin', password='lucasliu1379',
                              host=host,
                              database='risk')
  print (f'established connectoin to {host}')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cnx.close()
