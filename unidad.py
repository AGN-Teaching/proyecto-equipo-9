class Unidad:
    def __init__(self, eco_num):
        """
        Inicializa una unidad con su número económico y otros atributos.
        Args:
            eco_num (int): Número económico de la unidad.
        """
        self.__numero_economico = eco_num
        self.__count_viajes = 0
        self.__en_mantenimiento = False
        self.__tarifa_base = 15

    def get_numero_economico(self):
        """
        Devuelve el número económico de la unidad.
        """
        return self.__numero_economico

    def get_en_mantenimiento(self):
        """
        Verifica si la unidad está en mantenimiento.
        """
        return self.__en_mantenimiento

    def __str__(self):
        """
        Devuelve una representación en cadena de la unidad con su número económico y estado de mantenimiento.
        """
        return f'{self.__numero_economico} ~ Mantenimiento: {self.__en_mantenimiento}'

    def get_viajes(self):
        """
        Devuelve la cantidad de viajes realizados por la unidad.
        """
        return self.__count_viajes

    def get_tarifa_base(self):
        """
        Devuelve la tarifa base de la unidad.
        """
        return self.__tarifa_base

    def viaje_hecho(self):
        """
        Incrementa el contador de viajes realizados por la unidad.
        """
        self.__count_viajes += 1

    def mantenimiento(self):
        """
        Verifica si la unidad necesita mantenimiento después de cada tercer viaje.
        """
        if self.get_viajes() % 3 == 0:
            self.__en_mantenimiento = True

    def mantenimiento_finalizado(self):
        """
        Marca que el mantenimiento ha finalizado y pone la unidad de nuevo en servicio.
        """
        self.__en_mantenimiento = False

    def get_tarifa_km(self):
        """
        Método que debe ser implementado en clases hijas para obtener la tarifa por kilómetro.
        """
        pass

    def get_tarifa_min(self):
        """
        Método que debe ser implementado en clases hijas para obtener la tarifa por minuto.
        """
        pass