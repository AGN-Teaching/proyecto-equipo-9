class Unidad:
    def __init__(self, eco_num):
        self.__numero_economico =eco_num
        self.__count_viajes = 0
        self.__en_mantenimiento = False

    def get_numero_economico(self):
        return self.__numero_economico

    def get_en_mantenimiento(self):
        return self.__en_mantenimiento
    
    def mandar_mantenimiento(self):
        self.__en_mantenimiento = True

    def salida_mantenimiento(self):
        self.__en_mantenimiento = False

    def viajes(self):
        return self.__count_viajes