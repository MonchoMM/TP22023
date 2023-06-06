REMERAS_CATEGORIA = ['españolas', 'francesas',"inglesas","holandesas","alemanas","italianas"]

class Contenido:
        
    def __init__(self, club, descripcion, año, nombre, color,talle,categoria):
        self.club= club
        self.descripcion = descripcion
        self.año =año
        self.nombre = nombre
        self.color = color
        self.talle= talle
        if categoria not in REMERAS_CATEGORIA:
            raise Exception('Debe ingresar una categoría correcta')
        self.categoria = categoria
        

class Nueva(Contenido):
    def __init__(self, club, descripcion, año, nombre, color,talle,categoria, tipo='nueva'):
        self.tipo = tipo
        super().__init__(club,nombre, descripcion, año, color,talle, categoria)
    def __str__(self):
        return (f'Club: {self.club}\nDescripción: {self.descripcion}\nNombre Dorsal: {self.nombre}\
        \nAño: {self.año}\nColor: {self.color}\nCategoría:{self.categoria}\nTalle: {self.talle}\nTipo: {self.tipo}')
    
    
class Retro(Contenido):
    def __init__(self,club, descripcion, año, nombre, color,talle,categoria,uso,estado,tipo='retro'):
        self.uso = uso
        self.estado = estado
        self.tipo=tipo
        super().__init__(club,nombre, descripcion, año, color,talle, categoria)
    def agregar_temp(self):
        self.stock+=1
    def __str__(self):
        return (f'Club: {self.club}\nDescripción: {self.descripcion}\nNombre Dorsal: {self.nombre}\
        \nAño: {self.año}\nColor: {self.color}\nCategoría:{self.categoria}\nTalle:{self.talle}\nTipo{self.tipo}\nUso:{self.uso}\nEstado: {self.estado}' )
  