class Usuario:
    def __init__(self, nombre, tdc, id_unico):
        self.__nombre = nombre
        self.__tdc = tdc
        self.__id = id_unico
        self.__viajes_count = 0

    def get_tdc(self):
        return self.__tdc
    
    def get_nombre(self):
        return self.__nombre
    
    def get_id(self):
        return self.__id
    
    def get_viajes_count(self):
        return self.__viajes_count