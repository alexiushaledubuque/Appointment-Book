from flask import Flask, render_template, request, jsonify, g
import sqlite3

app = Flask(__name__)

app.database = 'apex.db'

@app.route('/')
def main():

    g.db = connect_db()
    cur = g.db.execute('select * from apptTable')
    appts = [dict(apptDate=row[0], apptTime=row[1], description=row[2]) for row in cur.fetchall()]
    g.db.close()
    return render_template('index.html', appts=appts)

# @app.route('/process', methods=['POST', 'GET'])
# def process():
#     con = sqlite3.connect('apex.db')
#     con.row_factory = sql.row_factory
#
#     cur = con.cursor()
#     cur.execute('select * from apptTable')
#
#     rows = cur.fetchall();
#     return render_template('index.html', rows = rows)

def connect_db():
    return sqlite3.connect(app.database)

if __name__ == "__main__":
    app.run()
