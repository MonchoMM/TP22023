class Camiseta:

    def __init__(self, camiseta_code, equipo,talle,price, año, estado, pais) -> None:
        self.camiseta_code = camiseta_code
        self.equipo = equipo
        self.talle = talle
        self.price = price
        self.año = año
        self.estado = estado
        self.pais = pais


    def serialize(self):
        return {
            'camiseta_code': self.camiseta_code,
            'equipo': self.equipo,
            'estado': self.estado,
            'price': self.price
        }

    def serialize_details(self):
        return {
            'camiseta_code': self.camiseta_code,
            'equipo': self.equipo,
            'talle': self.talle,
            'price': self.price,
            'año': self.año,
            'estado': self.estado,
            'pais': self.pais
        }