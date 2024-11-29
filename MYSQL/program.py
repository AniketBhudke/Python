import mysql.connector # Step-1
def tablecreate():
    try:
        con=mysql.connector.connect(host="localhost",
                                    user="root",
                                    passwd="12345") # Step-2
        cur=con.cursor() #Step-3
        #Step-4
        dc="create database school"
        cur.execute(dc)
        print("Database created in MySQL Sucessfully--verify")  # Step-5 
    except mysql.connector.DatabaseError as db:
        print("Probem with MySQL:", db)

#Main Program
tablecreate() # Funcion Call