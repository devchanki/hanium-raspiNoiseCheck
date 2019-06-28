from mcp3208 import MCP3208
import time
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='hanium',
                             password='hanium',
                             db='hanium',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
adc=MCP3208()
while True:
    tmp= adc.read(0)
    if( tmp > 30 ):
        try:
            with connection.cursor() as cursor:
        # Create a new record
                sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
                cursor.execute(sql, ( str(tmp), str(time.ctime())))
                connection.commit()
                print("insert finish")
                time.sleep(0.1)
        except:
            print("error")

