import sqlite3

conn = sqlite3.connect('employees.db')

c = conn.cursor()
inp = int(input("""
\n1. Create Table.
\n2. Insert Values.
\n3. Print.
\n4. Delete Data.
\n4. Enter Value: """))

if(inp == 1):
    conn.execute("""CREATE TABLE Login(
    EID integer,
    FirstName text,
    LastName text
    )""")
elif(inp == 2):
    c.execute("INSERT INTO Login VALUES(132, 'Kevin', 'Jacob')")
elif(inp == 3):
    c.execute("select * from Login")
    print(c.fetchall())
elif(inp == 4):
    c.execute("DELETE from Login")
else:
    print("Wrong input")

conn.commit()
conn.close()