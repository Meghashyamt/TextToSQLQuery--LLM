import sqlite3

connection=sqlite3.connect("student.db")

cursor=connection.cursor()

table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),SECTION VARCHAR(25),MARKS INT)

"""

cursor.execute(table_info)


cursor.execute('''INSERT INTO STUDENT VALUES('shyam','DS','A',90)''')
cursor.execute('''INSERT INTO STUDENT VALUES('ravi','DS','A',80)''')
cursor.execute('''INSERT INTO STUDENT VALUES('vijay','DS','A',70)''')
cursor.execute('''INSERT INTO STUDENT VALUES('saipavan','DS','A',60)''')
cursor.execute('''INSERT INTO STUDENT VALUES('gokul','DS','A',35)''')


print("The inserted row")

data=cursor.execute("""Select * FROM STUDENT""")
for row in data:
    print(row)

connection.commit()
connection.close()