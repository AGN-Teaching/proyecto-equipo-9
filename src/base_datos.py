from black import Black
from express import Express
from diamond import Diamond
from usuario import Usuario
class BaseDatos:
    def __init__(self):
        self.__usuarios = {}
        self.__unidades = {'Express':[], 'Black':[], 'Diamond':[]}
        self.__contador = [100,200,300,1] # [express, black, diamond, id]

    def add_unidad_express(self):
        no_eco = self.__contador[0]
        self.__unidades['Express'].append(Express(no_eco))
        return 0

    def add_unidad_black(self):
        no_eco = self.__contador[1]
        self.__unidades['Black'].append(Black(no_eco))
        return 1

    def add_unidad_diamond(self):
        no_eco = self.__contador[2]
        self.__unidades['Diamond'].append(Diamond(no_eco))
        return 2
    
    def add_usuario(self, nombre, tdc):
        id_unico= self.__count_id
        self.__usuarios[id_unico] = Usuario(nombre, tdc)
        return 3

    def inc_contador(self, contador):
        self.__contador[contador] += 1

    def get_unidades_disponibles(self):
        total_unidades = self.__unidades
        print('Unidades disponibles')
        for clasificacion, unidades in total_unidades.items():
            for unidad in unidades:
                    if not Express.get_en_mantenimiento(unidad):
                        print(f'{clasificacion} ~ {Express.get_numero_economico(unidad)}')
                             

pruebas = BaseDatos()
pruebas.add_unidad_black()
pruebas.add_unidad_express()
pruebas.add_unidad_diamond()
pruebas.add_unidad_diamond()
pruebas.get_unidades_disponibles()