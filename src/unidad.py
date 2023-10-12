class Unidad:
    def __init__(self, eco_num):
        self.__numero_economico = eco_num
        self.__count_viajes = 0
        self.__en_mantenimiento = False
        self.__tarifa_base = 15

    def get_numero_economico(self):
        return self.__numero_economico

    def get_en_mantenimiento(self):
        return self.__en_mantenimiento

    def __str__(self):
        return f'{self.__numero_economico} ~ Mantenimiento: {self.__en_mantenimiento}'

    def get_viajes(self):
        return self.__count_viajes

    def get_tarifa_base(self):
        return self.__tarifa_base

    def viaje_hecho(self):
        self.__count_viajes += 1

    def mantenimiento(self):
        if self.get_viajes() % 3 == 0:
            self.__en_mantenimiento = True

    def mantenimiento_finalizado(self):
        self.__en_mantenimiento = False

    def get_tarifa_km(self):
        pass

    def get_tarifa_min(self):
        pass
