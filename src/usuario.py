class Usuario:
    def __init__(self, nombre, tdc):
        self.__nombre = nombre
        self.__tdc = tdc
        self.__viajes_count = 0
        self.__aplicable_descuento = False
        self.__reservaciones = []

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

    def get_reservaciones(self):
        return self.__reservaciones

    def set_reservacion(self, reservacion):
        if len(self.__reservaciones) >= 5:
            # Si ya hay 5 reservaciones, elimina la más antigua (la primera)
            self.__reservaciones.pop(0)
        self.__reservaciones.append(reservacion)

    def delete_reservacion(self, reservacion):
        self.__reservaciones.pop(int(reservacion))
