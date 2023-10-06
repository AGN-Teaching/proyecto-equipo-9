from base_datos import BaseDatos

class Sistema:
    def __init__(self):
        self.__base_datos = BaseDatos()
        self.__promociones = 0.5

    def unidades_disponibles(self):
        unidades = BaseDatos.get_unidades()
        for no_eco, unidad in unidades.items():
            disponible = unidad.get_en_mantenimiento()
            if not disponible:
                print(f'No.economico: {no_eco}')

    def mantenimiento(self, unidad):
        if unidad.viajes % 15 == 0:
            unidad.mandar_mantenimiento()