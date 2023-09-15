import pymysql

conn = pymysql.connect(
    host='sql11.freesqldatabase.com',
    database='sql11645932',
    user='sql11645932',
    password='99vXfGaGUQ',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor=conn.cursor()

tables_to_drop = ["Note", "Eleve", "Matiere", "Classe"]

for table in tables_to_drop:
    try:
        cursor.execute(f"DROP TABLE IF EXISTS {table}")
        print(f"Succès lors de la suppression de la table {table}")
    except Exception as e:
        print(f"Erreur lors de l'exécution de la requête SQL pour la table {table}: {e}")
        # Annulez la transaction en cas d'erreur
        conn.rollback()


sql_query_create_classe = """CREATE TABLE Classe (
    nom VARCHAR(255) PRIMARY KEY,
    nbEleve INT,
    profPrincipal VARCHAR(255),
    emailProfPrincipal VARCHAR(255)
)"""

sql_query_create_eleve = """CREATE TABLE Eleve (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    dateNaissance DATE,
    idClasse VARCHAR(255),  -- Clé étrangère vers la table Classe
    FOREIGN KEY (idClasse) REFERENCES Classe(nom)
)"""

sql_query_create_matiere = """CREATE TABLE Matiere (
    nom VARCHAR(255) PRIMARY KEY
)"""

sql_query_create_note ="""CREATE TABLE Note (
    id INT AUTO_INCREMENT PRIMARY KEY,
    idEleve INT,
    idMatiere VARCHAR(255),
    valeur DECIMAL(5, 2),
    FOREIGN KEY (idEleve) REFERENCES Eleve(id),
    FOREIGN KEY (idMatiere) REFERENCES Matiere(nom)
)"""

try:
    cursor.execute(sql_query_create_classe)
    print(f"Succes lors de la creation de la table Classe")
    cursor.execute(sql_query_create_eleve)
    print(f"Succes lors de la creation de la table Eleve")
    cursor.execute(sql_query_create_matiere)
    print(f"Succes lors de la creation de la table Matiere")
    cursor.execute(sql_query_create_note)
    print(f"Succes lors de la creation de la table Note")
    # Validez la transaction si nécessaire (pour les requêtes INSERT, UPDATE, DELETE)
    conn.commit()

except Exception as e:
    print(f"Erreur lors de l'exécution de la requête SQL : {e}")
    # Annulez la transaction en cas d'erreur
    conn.rollback()



sql_query_add_data_classe = """
INSERT INTO Classe (nom, nbEleve, profPrincipal, emailProfPrincipal)
VALUES
    ('Classe A', 25, 'M. Dupont', 'dupont@example.com'),
    ('Classe B', 30, 'Mme. Martin', 'martin@example.com'),
    ('Classe C', 22, 'M. Dubois', 'dubois@example.com');
"""

sql_query_add_data_eleve = """INSERT INTO Eleve (nom, prenom, dateNaissance, idClasse)
VALUES
    ('Smith', 'John', '2005-02-10', 'Classe A'),
    ('Johnson', 'Mary', '2006-04-15', 'Classe A'),
    ('Brown', 'David', '2005-08-20', 'Classe B'),
    ('Davis', 'Emily', '2006-01-05', 'Classe B'),
    ('Jones', 'Michael', '2005-03-30', 'Classe C'),
    ('Wilson', 'Olivia', '2006-07-18', 'Classe C');
"""

sql_query_add_data_matiere = """INSERT INTO Matiere (nom)
VALUES
    ('Mathématiques'),
    ('Français'),
    ('Histoire'),
    ('Sciences'),
    ('Anglais');
"""

sql_query_add_data_note = """INSERT INTO Note (idEleve, idMatiere, valeur)
VALUES
    (1, "Mathématiques", 9.5),
    (1, "Français", 8.0),
    (2, "Mathématiques", 9.0),
    (2, "Français", 8.5),
    (3, "Mathématiques", 7.5),
    (3, "Français", 6.5),
    (4, "Histoire", 7.0),
    (4, "Sciences", 9.0),
    (5, "Histoire", 8.0),
    (5, "Anglais", 7.5),
    (6, "Français", 8.5),   
    (6, "Sciences", 9.5);   
"""

try:
    cursor.execute(sql_query_add_data_classe)
    cursor.execute(sql_query_add_data_eleve)
    cursor.execute(sql_query_add_data_matiere)
    cursor.execute(sql_query_add_data_note)
    print(f"Succes lors de l'ajout des données initiales'")

    # Validez la transaction si nécessaire (pour les requêtes INSERT, UPDATE, DELETE)
    conn.commit()

except Exception as e:
    print(f"Erreur lors de l'exécution de la requête SQL : {e}")
    # Annulez la transaction en cas d'erreur
    conn.rollback()

finally:
    # Fermez le curseur et la connexion lorsque vous avez terminé
    cursor.close()
    conn.close()

