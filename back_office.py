from flask import jsonify, request
import camiseta_controller_poo
from db_camisetas import create_tables
from exchange_rate import get_xr


def get_camiseta():
    camisetas = camiseta_controller_poo.get_camiseta()
    camiseta_list=[]
    for camisa in camisetas:
        elem = camisa.serialize()
        camiseta_list.append(elem)
    return jsonify(camiseta_list)

def insert_camisa():
    camiseta_details = request.get_json()
    camiseta_code = camiseta_details["camiseta_code"]
    equipo = camiseta_details["equipo"]
    talle =camiseta_details["talle"]
    price = camiseta_details["price"]
    año= camiseta_details["año"]
    estado= camiseta_details["estado"]
    pais =camiseta_details["pais"]
    result = camiseta_controller_poo.insert_camiseta(camiseta_code, equipo,talle, price,año,estado,pais)
    return jsonify(result)

def update_camiseta():
    camiseta_details = request.get_json()
    camiseta_code = camiseta_details["camiseta_code"]
    equipo = camiseta_details["equipo"]
    talle =camiseta_details["talle"]
    price = camiseta_details["price"]
    año= camiseta_details["año"]
    estado= camiseta_details["estado"]
    pais =camiseta_details["pais"]
    result = camiseta_controller_poo.update_camiseta_camiseta(camiseta_code, equipo,talle, price,año,estado,pais)
    return jsonify(result)

def delete_camiseta(camiseta_code):
    result = camiseta_controller_poo.delete_camiseta(camiseta_code)
    return jsonify(result)


def get_camiseta_by_id(camiseta_code):
    camiseta = camiseta_controller_poo.get_by_id(camiseta_code)
    return jsonify(camiseta)

def get_camiseta_by_id_usd(camiseta_code):
    camiseta = camiseta_controller_poo.get_by_id(camiseta_code)
    xr = get_xr()
    price_usd = camiseta['price']/xr
    camiseta['price'] = round(price_usd,2)
    return jsonify(camiseta)


while True:
    print("Bienvenido a @@@---CamisetasLoro---@@@")
    print("En que podemos ayudarte")
    print("""Seleccione una opcion: 
    1) Buscar camiseta
    2) Agregar camiseta
    3) Actualizar camiseta
    4) Eliminar camiseta
    5) Buscar camiseta con codigo de camiseta
    6) Camiseta con precio dolar
    7) Salir
             """)
    
    
    option=input()
    try:
        
      if int(option) < 1 or int(option) > 6:
          print("Debe seleccionar una opcion valida")
          continue
      if option=="1":
          get_camiseta()
      if option =="2":
          insert_camisa()
      if option =="3":
          update_camiseta()
      if option =="4":
          camiseta_code=input("Inserte codigo de camiseta a eliminar")
          delete_camiseta(camiseta_code)
      if option =="5":
          camiseta_code=input("Inserte codigo de camiseta a buscar")
          get_camiseta_by_id(camiseta_code)        
      if option =="6":
          camiseta_code=input("Inserte codigo de camiseta a buscar precio dolar")
          get_camiseta_by_id_usd(camiseta_code)
      if option =="7":
          print("Saliendo del sistema.....")
          break
    except ValueError:
        print("DEBE INGRESAR NUMEROS NO LETRAS")           
create_tables()

      