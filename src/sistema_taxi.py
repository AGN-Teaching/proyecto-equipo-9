from base_datos import BaseDatos

class Sistema:
    def __init__(self):
        self.__base_datos = BaseDatos()
        self.__promociones = 0.5

    def tiempo_origen_destino(self,origen,destino):
        if (origen == "Tacubaya" or origen== "UAM-C") and (destino== "UAM-C" or destino== "Tacubaya"):
            kilometro_recorrido= 13
            tiempo_minutos= 45
        elif (origen == "Coacalco" or origen== "UAM-C") and (destino== "UAM-C" or destino== "Coacalco"):
            kilometro_recorrido = 50 
            tiempo_minutos = 90
        elif (origen== "Pueblo de Santa Fe" or origen== "UAM-C") and (destino== "UAM-C" or destino== "Pueblo de Santa Fe"):
            kilometro_recorrido= 7
            tiempo_minutos= 30 
        else:
            (origen== "Zocalo" or origen== "UAM-C") and (destino=="UAM-C" or destino== "Zocalo")  
            kilometro_recorrido= 35
            tiempo_minutos= 90   

        return kilometro_recorrido, tiempo_minutos     

    def obtener_unidad(self,eco_num):
        unidades= self.__base_datos.get_unidades()

    def reservacion(self,origen,destino,hora_viaje,eco_num): 
        
        




    def unidades_disponibles(self):
        unidades = BaseDatos.get_unidades()
        for no_eco, unidad in unidades.items():
            disponible = unidad.get_en_mantenimiento()
            if not disponible:
                print(f'No.economico: {no_eco}')

    def mantenimiento(self, unidad):
        if unidad.viajes % 15 == 0:
            unidad.mandar_mantenimiento()