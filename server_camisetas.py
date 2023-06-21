from flask import Flask, jsonify, request
import camiseta_controller_poo
from db_camisetas import create_tables
from exchange_rate import get_xr

app = Flask(__name__)


@app.route('/camiseta', methods=["GET"])
def get_camiseta():
    camisetas = camiseta_controller_poo.get_camiseta()
    camiseta_list=[]
    for camisa in camisetas:
        elem = camisa.serialize()
        camiseta_list.append(elem)
    return jsonify(camiseta_list)

@app.route("/camiseta/create", methods=["POST"])
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


@app.route("/camiseta/modify", methods=["PUT"])
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


@app.route("/camiseta/eliminate/<string:camiseta_code>", methods=["DELETE"])
def delete_camiseta(camiseta_code):
    result = camiseta_controller_poo.delete_camiseta(camiseta_code)
    return jsonify(result)


@app.route("/game/<game_code>", methods=["GET"])
def get_game_by_id(camiseta_code):
    camiseta = camiseta_controller_poo.get_by_id(camiseta_code)
    return jsonify(camiseta)

@app.route("/game/usd/<game_code>", methods=["GET"])
def get_camiseta_by_id_usd(camiseta_code):
    camiseta = camiseta_controller_poo.get_by_id(camiseta_code)
    xr = get_xr()
    price_usd = camiseta['price']/xr
    camiseta['price'] = round(price_usd,2)
    return jsonify(camiseta)

create_tables()

app.run()