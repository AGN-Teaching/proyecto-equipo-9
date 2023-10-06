from unidad import Unidad
class Black(Unidad):
    def __init__(self, eco_num):
        super().__init__(eco_num)
        self.__tarifa = 1

    def get_tarifa(self):
        return self.__tarifa
    