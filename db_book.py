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

sql_query_delete = """DROP TABLE book"""

try:
    cursor.execute(sql_query_delete)
    print(f"Succes lors de la suppression de la table book")
    # Validez la transaction si nécessaire (pour les requêtes INSERT, UPDATE, DELETE)
    conn.commit()
except Exception as e:
    print(f"Erreur lors de l'exécution de la requête SQL : {e}")
    # Annulez la transaction en cas d'erreur
    conn.rollback()

sql_query_create = """CREATE TABLE book (
id integer AUTO_INCREMENT PRIMARY KEY,
pageCount integer NOT NULL,
title VARCHAR(255) NOT NULL
)"""

try:
    cursor.execute(sql_query_create)
    print(f"Succes lors de la création de la table book")
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
