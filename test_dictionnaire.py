from flask import Flask, request, jsonify

app = Flask(__name__)

books_list = [
  {
    "id": 1,
    "title": "Unlocking Android",
    "pageCount": 416
  },
  {
    "id": 2,
    "title": "Android in Action, Second Edition",
    "pageCount": 592
  },
  {
    "id": 3,
    "title": "Specification by Example",
    "pageCount": 0
  },
  {
    "id": 4,
    "title": "Specification 2",
    "pageCount": 10
  }
]
@app.route('/book', methods=['GET','POST'])
def book():
    if request.method == 'GET':
        if len(books_list)>0:
            return jsonify(books_list)
        else:
            return 'Nothing Found',404

    if request.method == 'POST':
        new_title = request.form['title']
        new_pageCount = request.form['pageCount']
        iD = books_list[-1]['id']+1

        # Vérifiez si la valeur existe et peut être convertie en entier
        if new_pageCount is not None:
            try:
                new_pageCount = int(new_pageCount)
            except ValueError:
                return "La valeur n'est pas un entier valide."
        else:
            return "Le champ n'existe pas dans le formulaire."

        new_object = {
            "id" : iD,
            "title" : new_title,
            "pageCount" : new_pageCount
        }

        books_list.append(new_object)
        return jsonify(books_list), 201
    
@app.route('/book/<int:id>', methods=['GET','PUT','DELETE'])
def single_book(id):
    
    if request.method == 'GET':
        for book in books_list:
            if book['id'] == id:
                return jsonify(book)
            
    if request.method == 'PUT':
        for book in books_list:
            if book['id'] == id:
                book['title'] = request.form['title']
                new_pageCount = request.form['pageCount']

                # Vérifiez si la valeur existe et peut être convertie en entier
                if new_pageCount is not None:
                    try:
                        new_pageCount = int(new_pageCount)
                    except ValueError:
                        return "La valeur n'est pas un entier valide."
                else:
                    return "Le champ n'existe pas dans le formulaire."
                book['pageCount'] = new_pageCount
                
                updated_object = {
                  "id" : book['id'],
                  "title" : book['title'],
                  "pageCount" : book['pageCount']
                }
                return jsonify(updated_object)
                
            
    if request.method == 'DELETE':
        for index,book in enumerate(books_list):
            if book['id'] == id:
                books_list.pop(index)
                return jsonify(books_list)
                
if __name__ == '__main__':
    app.run(debug=True)