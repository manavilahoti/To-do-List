import mysql.connector

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="Imperial@07",
        auth_plugin='mysql_native_password',  
    )

    my_cursor = mydb.cursor()

    my_cursor.execute("CREATE DATABASE IF NOT EXISTS our_task")

    my_cursor.execute("SHOW DATABASES")

    for db in my_cursor:
        print(db)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if 'my_cursor' in locals() and my_cursor:
        my_cursor.close()
    if 'mydb' in locals() and mydb:
        mydb.close()
