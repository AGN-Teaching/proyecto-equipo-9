from unidad import Unidad
class Black(Unidad):
    def __init__(self, eco_num):
        super().__init__(eco_num)
        self.__tarifa_km = 1.0
        self.__tarifa_min = 1.0

    def get_tarifa_km(self):
        return self.__tarifa_km
    
    def get_tarifa_min(self):
        return self.__tarifa_min
    