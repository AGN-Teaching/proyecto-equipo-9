from datetime import datetime, timedelta

class Usuario:
    def __init__(self, nombre, tdc):
        """
        Inicializa un objeto de usuario con su nombre, tarjeta de crédito, y otros atributos.
        Args:
            nombre (str): Nombre del usuario.
            tdc (str): Número de tarjeta de crédito del usuario.
        """
        self.__nombre = nombre
        self.__tdc = tdc
        self.__viajes_count = 0
        self.__aplicable_descuento = False
        self.__reservaciones = []

    def get_nombre(self):
        """
        Devuelve el nombre del usuario.
        """
        return self.__nombre

    def get_viajes_count(self):
        """
        Devuelve la cantidad de viajes realizados por el usuario.
        """
        return self.__viajes_count

    def change_status_aplicable_descuento(self):
        """
        Verifica si el usuario es aplicable para un descuento en base a su historial de reservaciones.
        """
        # Verificar si el número de viajes es mayor que 0 y es un múltiplo de 5
        if self.__viajes_count > 0 and self.__viajes_count % 5 == 0:
            # Verificar si hay exactamente 5 reservaciones (la capacidad máxima)
            if len(self.__reservaciones) == 5:
                # Ordenar las reservaciones por fecha
                reservaciones_ordenadas = sorted(self.__reservaciones, key=lambda x: datetime.strptime(x['Fecha'], '%d/%m'))

                # Obtener la fecha más antigua y la fecha más reciente
                fecha_mas_antigua = datetime.strptime(reservaciones_ordenadas[0]['Fecha'], '%d/%m')
                fecha_mas_reciente = datetime.strptime(reservaciones_ordenadas[-1]['Fecha'], '%d/%m')

                # Calcular la diferencia de tiempo entre la fecha más antigua y la fecha más reciente
                diferencia_tiempo = fecha_mas_reciente - fecha_mas_antigua

                # Verificar si la diferencia de tiempo es igual o menor a 7 días (1 semana)
                if diferencia_tiempo <= timedelta(days=7):
                    self.__aplicable_descuento = True
                else:
                    self.__aplicable_descuento = False
            else:
                self.__aplicable_descuento = False
        else:
            self.__aplicable_descuento = False

    def get_status_aplicable_descuento(self):
        """
        Devuelve el estado de aplicabilidad de descuento para el usuario.
        """
        return self.__aplicable_descuento

    def get_reservaciones(self):
        """
        Devuelve la lista de reservaciones del usuario.
        """
        return self.__reservaciones

    def set_reservacion(self, reservacion):
        """
        Agrega una nueva reservación a la lista del usuario y elimina la más antigua si se supera la capacidad máxima.
        Args:
            reservacion (dict): Datos de la reservación.
        """
        if len(self.__reservaciones) >= 5:
            # Si ya hay 5 reservaciones, elimina la más antigua (la primera)
            self.__reservaciones.pop(0)
        self.__reservaciones.append(reservacion)

    def add_count_viajes(self):
        """
        Incrementa el contador de viajes realizados por el usuario.
        """
        self.__viajes_count += 1

    def delete_reservacion(self, reservacion):
        """
        Elimina una reservación específica de la lista de reservaciones del usuario.
        Args:
            reservacion (int): Índice de la reservación a eliminar.
        """
        try:
            self.__reservaciones.pop(int(reservacion))
        except IndexError:
            print('No hay reservaciones por eliminar o ingreso un número fuera de rango')