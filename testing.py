import mysql.connector



try:
    connection = mysql.connector.connect(host='localhost', database='esxlegacy_61655b', user='root', password='3QT!4)$zc3Pq4Ad')
    if connection.is_connected():
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute("UPDATE vehicles SET vehicles.category = 'custom aston-martin' WHERE vehicles.model = 'amdbx';")
        #cursor.execute("SELECT * FROM vehicles WHERE vehicles.model = 'amdbx'")
        #car = cursor.fetchone()
        print(f'done ')
        
except mysql.connector.Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Conn closed")
