import sqlite3
DATABASE_NAME = "camisetas.db"


def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    tables = [
        """CREATE TABLE IF NOT EXISTS camisetas(
                camiseta_code TEXT PRIMARY KEY,
                equipo TEXT NOT NULL,
                talle TEXT NOT NULL,
                price REAL NOT NULL,
                año INTEGER NOT NULL,
                estado TEXT NOT NULL,
                pais TEXT NOT NULL
            )
            """
    ]
    db = get_db()
    cursor = db.cursor()
    for table in tables:
        cursor.execute(table)