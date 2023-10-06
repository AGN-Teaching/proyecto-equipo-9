from black import Black
from usuario import Usuario
class BaseDatos:
    def __init__(self):
        self.__usuarios = {}
        self.__unidades = {}
        self.__count_no_eco_black = 1000
        self.__count_no_eco_diamond = 2000
        self.__count_no_eco_express = 3000
        self.__count_id = 1

    def agregar_unidad(self, tipo_unidad):
        if tipo_unidad == 'Black':
            no_eco = self.__count_no_eco_black
            unidad = Black(no_eco)
            self.__unidades[no_eco] = unidad
            self.__count_no_eco_black += 1
    
    def agregar_usuario(self, nombre, tdc, id_unico):
        usuario = Usuario(nombre, tdc, id_unico)
        self.__usuarios[id_unico] = usuario
        self.__count_id += 1

    def get_unidades(self):
        return self.__unidades
