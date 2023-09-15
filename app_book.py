from flask import Flask, request, jsonify
import json
import pymysql

app = Flask(__name__)

def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
    host='sql11.freesqldatabase.com',
    database='sql11645932',
    user='sql11645932',
    password='99vXfGaGUQ',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)
    except pymysql.Error as e:
        print(e)
    return conn


@app.route('/book', methods=['GET','POST'])
def book():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book")
        books = [
            dict(id=row['id'], pageCount=row['pageCount'], title=row['title'])
            for row in cursor.fetchall()
        ]
        if books is not None:
            return jsonify(books)

    if request.method == 'POST':
        new_title = request.form['title']
        new_pageCount = request.form['pageCount']
        sql = """INSERT INTO book(title,pageCount) VALUES (%s,%s)"""
        cursor.execute(sql,(new_title,new_pageCount))
        conn.commit()
        return "Book with the id: 0 created successfully"

    
@app.route('/book/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
    conn = db_connection()
    cursor = conn.cursor()
    book = None

    if request.method == 'GET':
        cursor.execute("SELECT * FROM book WHERE id=%s",(id,))
        book = cursor.fetchone()
        if book is not None:
            return jsonify(book), 200
        else:
            return "Livre introuvable", 404
            
    if request.method == 'PUT':
        sql = """UPDATE book SET pageCount=%s,title=%s WHERE id=%s"""
        
        new_pageCount = request.form['pageCount']
        new_title = request.form['title']

        updated_object = {
            "id" : id,
            "title" : new_title,
            "pageCount" : new_pageCount
            }
        cursor.execute(sql,(new_pageCount,new_title,id))
        conn.commit()
        return jsonify(updated_object)
                
            
    if request.method == 'DELETE':
        conn = db_connection()
        cursor = conn.cursor()
        sql = """DELETE FROM book WHERE id=%s"""
        cursor.execute(sql,(id,))
        conn.commit()
        return "The Book with id: {} has been deleted.".format(id), 200
                
if __name__ == '__main__':
    app.run(debug=True)