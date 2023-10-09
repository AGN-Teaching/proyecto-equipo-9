class Usuario:
    def __init__(self, nombre, tdc):
        self.__nombre = nombre
        self.__tdc = tdc
        self.__viajes_count = 0
        self.__aplicable_descuento = False

    def get_tdc(self):
        return self.__tdc
    
    def get_nombre(self):
        return self.__nombre
    
    def get_viajes_count(self):
        return self.__viajes_count
    
    def change_staus_aplicable_descuento(self):
        viajes = self.__aplicable_descuento
        if viajes % 5 == 0:
            self.__aplicable_descuento = True
        else:
            self.__aplicable_descuento = False

    def get_status_aplicable_descuento(self):
        return self.__aplicable_descuento