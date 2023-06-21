from db_camisetas import get_db
from clase_camiseta import Camiseta


def insert_camiseta(camiseta_code, equipo,talle,price, año, estado, pais):
    db = get_db()
    cursor = db.cursor()
    statement = "INSERT INTO camisetas (camiseta_code, equipo,talle,price, año, estado, pais) \
    VALUES ( ?, ?, ?, ? ,?, ?, ?)"
    cursor.execute(statement, [camiseta_code, equipo,talle,price, año, estado, pais])
    db.commit()
    return True

def update_camiseta(camiseta_code, equipo,talle,price, año, estado, pais):
    db = get_db()
    cursor = db.cursor()
    statement = "UPDATE camisetas SET equipo = ?, talle = ?, price= ?, año= ?, estado= ?, pais= ? \
    WHERE camiseta_code = ?"
    cursor.execute(statement, [equipo,talle,price, año, estado, pais, camiseta_code])
    db.commit()
    return True


def delete_camiseta(camiseta_code):
    db = get_db()
    cursor = db.cursor()
    statement = "DELETE FROM camisetas WHERE camiseta_code = ?"
    cursor.execute(statement, [camiseta_code])
    db.commit()
    return True


def get_by_id(camiseta_code):
    db = get_db()
    cursor = db.cursor()
    statement = "SELECT camiseta_code, equipo,talle,price, año, estado, pais FROM camisetas \
    WHERE camiseta_code = ?"
    cursor.execute(statement, [camiseta_code])
    single_camiseta = cursor.fetchone()
    camiseta_code = single_camiseta[0]
    equipo = single_camiseta[1]
    talle = single_camiseta[2]
    price = single_camiseta[3]
    año = single_camiseta[4]
    estado = single_camiseta[5]
    pais = single_camiseta[6]
    camiseta = Camiseta (camiseta_code, equipo,talle,price, año, estado, pais) 
    return camiseta.serialize_details()


def get_camiseta():
    db = get_db()
    cursor = db.cursor()
    query = "SELECT camiseta_code, equipo,talle,price, año, estado, pais FROM camisetas"
    cursor.execute(query)
    camisetas_list = cursor.fetchall()
    list_of_camisetas=[]
    for camiseta in camisetas_list:
        camiseta_code = camiseta[0]
        equipo = camiseta[1]
        talle = camiseta[2]
        price = camiseta[3]
        año = camiseta[4]
        estado = camiseta[5]
        pais = camiseta[6]
        camiseta_to_add = Camiseta(camiseta_code, equipo,talle,price, año, estado, pais)
        list_of_camisetas.append(camiseta_to_add)
    return list_of_camisetas