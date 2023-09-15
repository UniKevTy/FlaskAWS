from flask import Flask, request, jsonify, render_template
import pymysql

app = Flask(__name__, static_folder='static')

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/stat')
def stat():
    return render_template('stat.html')

@app.route('/ACP')
def ACP():
    return render_template('ACP.html')

@app.route('/addData', methods=['POST','GET'])
def addData():
    if request.method == 'GET':
        # Gérer l'affichage de la page avec les formulaires (méthode GET)
        return render_template('addData.html')
    
    conn = db_connection()
    cursor = conn.cursor()

    formulaire = request.form['formulaire']  # Récupérez la valeur du champ caché

    if formulaire == 'eleve':
        # Traitez les données du formulaire d'ajout d'élève
        new_nom = request.form['nom']
        new_prenom = request.form['prenom']
        new_dateNaissance = request.form['dateNaissance']
        new_idClasse = request.form['idClasse']
        sql = """INSERT INTO Eleve(nom, prenom, dateNaissance, idClasse) VALUES (%s, %s, %s, %s)"""
        cursor.execute(sql, (new_nom, new_prenom, new_dateNaissance, new_idClasse))
        conn.commit()
        return render_template('addData.html')

    elif formulaire == 'note':
        # Traitez les données du formulaire d'ajout de note
        new_idEleve = request.form['idEleve']
        new_idMatiere = request.form['idMatiere']
        new_valeur = request.form['valeur']
        sql = """INSERT INTO Note(idEleve, idMatiere, valeur) VALUES (%s, %s, %s)"""
        cursor.execute(sql, (new_idEleve, new_idMatiere, new_valeur))
        conn.commit()
        return render_template('addData.html')

    conn.close()
    return "Formulaire non reconnu"

@app.route('/classes', methods=['GET','POST'])
def classes():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Classe")
        classes = [
            dict(nom=row['nom'], nbEleve=row['nbEleve'], profPrincipal=row['profPrincipal'],emailProfPrincipal=row['emailProfPrincipal'])
            for row in cursor.fetchall()
        ]
        if classes is not None:
            return jsonify(classes)

    if request.method == 'POST':
        new_nom = request.form['nom']
        new_nbEleve= request.form['nbEleve']
        new_profPrincipal = request.form['profPrincipal']
        new_emailProfPrincipal = request.form['emailProfPrincipal']
        sql = """INSERT INTO Classe(nom,nbEleve,profPrincipal,emailProfPrincipal) VALUES (%s,%s,%s,%s)"""
        cursor.execute(sql,(new_nom,new_nbEleve,new_profPrincipal,new_emailProfPrincipal))
        conn.commit()
        return "Classe with the id: 0 created successfully"

@app.route('/eleves', methods=['GET','POST'])
def eleves():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Eleve")
        eleves = [
            dict(id=row['id'], nom=row['nom'], prenom=row['prenom'],dateNaissance=row['dateNaissance'], idClasse=row['idClasse'])
            for row in cursor.fetchall()
        ]
        if eleves is not None:
            return jsonify(eleves)

    if request.method == 'POST':
        new_nom = request.form['nom']
        new_prenom = request.form['prenom']
        new_dateNaissance = request.form['dateNaissance']
        new_idClasse = request.form['idClasse']
        sql = """INSERT INTO Eleve(nom,prenom,dateNaissance,idClasse) VALUES (%s,%s,%s,%s)"""
        cursor.execute(sql,(new_nom,new_prenom,new_dateNaissance,new_idClasse))
        conn.commit()
        return "Eleve with the id: 0 created successfully"
    
@app.route('/matieres', methods=['GET','POST'])
def matieres():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Matiere")
        matieres = [
            dict(nom=row['nom'])
            for row in cursor.fetchall()
        ]
        if matieres is not None:
            return jsonify(matieres)

    if request.method == 'POST':
        new_nom = request.form['nom']
        sql = """INSERT INTO Matiere(nom) VALUES (%s)"""
        cursor.execute(sql,(new_nom))
        conn.commit()
        return "Matiere with the id: 0 created successfully"

@app.route('/notes', methods=['GET','POST'])
def notes():
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == 'GET':
        cursor.execute("SELECT * FROM Note")
        notes = [
            dict(id=row['id'], idEleve=row['idEleve'], idMatiere=row['idMatiere'],valeur=row['valeur'])
            for row in cursor.fetchall()
        ]
        if notes is not None:
            return jsonify(notes)

    if request.method == 'POST':
        new_idEleve = request.form['idEleve']
        new_idMatiere = request.form['idMatiere']
        new_valeur = request.form['valeur']
        sql = """INSERT INTO Note(idEleve,idMatiere,valeur) VALUES (%s,%s,%s)"""
        cursor.execute(sql,(new_idEleve,new_idMatiere,new_valeur))
        conn.commit()
        return "Note with the id: 0 created successfully"



if __name__ == '__main__':
    app.run()