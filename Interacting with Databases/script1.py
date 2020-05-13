import sqlite3

def create_table():
    #connect to database
    conn = sqlite3.connect("lite.db")

    #create cursor object
    cur=conn.cursor()

    #write SQL query
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    #commit changes
    conn.commit()

    #close databse connection
    conn.close()

def insert(item,quantity,price):
    #create a connection with the database
    conn = sqlite3.connect("lite.db")
    cur=conn.cursor()
    
    cur.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))

    #close the database connection
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()

    #dont need to commit because just selecting data from the database
    conn.close()
    
    return rows

def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=? ", (quantity,price,item))
    conn.commit()
    conn.close()

#insert("Coffee Cup",10,5)
#delete("Wine Glass")
update(11,6,"Water Glass")
print(view())


    
