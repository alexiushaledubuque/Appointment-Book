import sqlite3 as sql

print "Opened database successfully";

def populate_db():
    conn = sqlite3.connect('apex.db')
    c = conn.cursor()

    c.execute( "INSERT INTO apptTable VALUES('May 2', '11:00am', 'Something')")
    c.execute( "INSERT INTO apptTable VALUES('May 2', '12:00pm', 'Something else')")
    c.execute( "INSERT INTO apptTable VALUES('May 4', '8:00am', 'Meet foo')")
    c.execute( "INSERT INTO apptTable VALUES('May 5', '3:00pm', 'Meet Sue')")
    c.execute( "INSERT INTO apptTable VALUES('September 1', '10:45pm', 'Code Python')")
    conn.commit()

    print "Records created successfully"

populate_db()

c.close()
conn.close()
