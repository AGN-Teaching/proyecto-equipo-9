from unidad import Unidad
class Diamond(Unidad):
    def __init__(self, eco_num):
        """
        Inicializa una unidad de tipo Diamond con su número económico y tarifas por kilómetro y minuto.
        Args:
            eco_num (int): Número económico de la unidad.
        """
        super().__init__(eco_num) 
        self.__tarifa_km = 2.0
        self.__tarifa_min = 2.0

    def get_tarifa_km(self):
        """
        Devuelve la tarifa por kilómetro para las unidades de tipo Diamond.
        """
        return self.__tarifa_km
    
    def get_tarifa_min(self):
        """
        Devuelve la tarifa por minuto para las unidades de tipo Diamond.
        """
        return self.__tarifa_min
    