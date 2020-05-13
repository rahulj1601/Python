import psycopg2

def create_table():
    #connect to database
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")

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
    conn = psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    
    #cur.execute("INSERT INTO store VALUES ('%s','%s','%s')" % (item,quantity,price)) #more prone to SQL injection
    cur.execute("INSERT INTO store VALUES (%s,%s,%s)", (item,quantity,price))

    #close the database connection
    conn.commit()
    conn.close()

def view():
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()

    #dont need to commit because just selecting data from the database
    conn.close()
    
    return rows

def delete(item):
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("DELETE FROM store WHERE item=%s",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=psycopg2.connect("dbname='database 1' user='postgres' password='postgres123' host='localhost' port='5432'")
    cur=conn.cursor()
    cur.execute("UPDATE store SET quantity=%s, price=%s WHERE item=%s ", (quantity,price,item))
    conn.commit()
    conn.close()

create_table()
#insert("Orange",10,15)
#delete("Orange") #deletes all rows with item "Orange"
update(20,15.0,"Apple")
print(view())
