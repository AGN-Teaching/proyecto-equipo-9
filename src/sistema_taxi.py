from black import Black
from express import Express
from diamond import Diamond
from usuario import Usuario
from random import choice
class Sistema:
    def __init__(self):
        self.__usuarios = {}
        self.__unidades = {'Express':[], 'Black':[], 'Diamond':[]}
        self.__contador = [100,200,300,1] # [express, black, diamond, id]
        self.__descuento = 0.15
        self.__rutas = {
            ("Tacubaya", "UAM-C"): (13, 45),
            ("Coacalco", "UAM-C"): (50, 90),
            ("Pueblo de Santa Fe", "UAM-C"): (7, 30),
            ("Zocalo", "UAM-C"): (35, 90),
            ("UAM-C","Tacubaya"): (13,45),
            ("UAM-C","Coacalco"): (50,90),
            ("UAM-C","Pueblo de Santa Fe"): (7,30),
            ("UAM-C","Zocalo"): (35,90)
        }
        self.__reservacion = [] # [[id, no_eco, origen, destino, fecha, hora, total]]

    #Devuelve el diccionario de Base de datos
    def list_unidades_disponibles(self):
        self.__base_datos.get_unidades_disponibles()

    def tiempo_distancia_viaje(self, origen, destino):
        # Verifica si la ruta está en el diccionario
        if (origen, destino) in self.__rutas:
            distancia, tiempo = self.__rutas[(origen, destino)]
            return distancia, tiempo
        
    def add_unidad_express(self):
        no_eco = self.__contador[0]
        self.__unidades['Express'].append(Express(no_eco))
        self.inc_contador(0)

    def add_unidad_black(self):
        no_eco = self.__contador[1]
        self.__unidades['Black'].append(Black(no_eco))
        self.inc_contador(1)

    def add_unidad_diamond(self):
        no_eco = self.__contador[2]
        self.__unidades['Diamond'].append(Diamond(no_eco))
        self.inc_contador(2)
    
    def add_usuario(self, nombre, tdc):
        id_unico= self.__contador[3]
        self.__usuarios[id_unico] = Usuario(nombre, tdc)
        self.inc_contador(3)
        # def add_usuario(self, nombre, tdc):
        # id_unico= self.__contador[3]
        # self.__usuarios[id_unico] = Usuario(nombre, tdc)
        # self.inc_contador(3)

    def eliminar_unidad(self, no_eco):
        unidades = self.__unidades
        for clasificacion_taxi, lista_taxis in unidades.items():
            for unidad in lista_taxis:
                if Express.get_numero_economico(unidad) == int(no_eco):
                    self.__unidades[clasificacion_taxi].remove(unidad)            

    def inc_contador(self, contador):
        self.__contador[contador] += 1

    def listar_unidades(self):
        unidades = self.__unidades
        for clasificacion, lista_unidades in unidades.items():
            for unidad in lista_unidades:
                print(Express.get_numero_economico(unidad))

    def get_unidades_disponibles(self):
        total_unidades = self.__unidades
        for clasificacion, unidades in total_unidades.items():
            for unidad in unidades:
                    if not Express.get_en_mantenimiento(unidad):
                        print(f'{clasificacion} ~ {Express.get_numero_economico(unidad)}')  

    def get_unidad(self, clasificacion_taxi):
        unidades = self.__unidades[clasificacion_taxi]
        return choice(unidades)
        
    def precio_parcial_viaje(self, origen, destino, unidad):
        tarifa_distancia = Express.get_tarifa_km(unidad)
        tarifa_tiempo = Express.get_tarifa_min(unidad)
        tarifa_base= Express.get_tarifa_base(unidad)
        distancia, tiempo = self.tiempo_distancia_viaje(origen, destino)
        total = tarifa_base + (distancia*tarifa_distancia) + (tarifa_tiempo*tiempo)
        return total

    def aplicar_promocion(self, total):
        return total - (total*self.__descuento)
    
    def reservacion(self, origen, destino, clasificacion_taxi, usuario, fecha, hora):
        unidad = self.get_unidad(clasificacion_taxi)
        no_eco = Express.get_numero_economico(unidad)
        total = self.precio_parcial_viaje(origen, destino, unidad)
        nombre_usuario = Usuario.get_nombre(usuario)
        Express.viaje_hecho(unidad)
        if not Usuario.get_status_aplicable_descuento(usuario):
            self.__reservacion.append([nombre_usuario, no_eco, origen, destino, fecha, hora, total])
            return total, False
        else:
            total = self.aplicar_promocion(total)
            self.__reservacion.append([nombre_usuario, no_eco, origen, destino, fecha, hora, total])
            return total, True
        
    def enlistar_reservaciones(self):
        reservaciones = self.__reservacion
        print(reservaciones)

    def get_rutas(self):
        return self.__rutas
    
    def enlistar_rutas(self):
        rutas = self.__rutas
        for i, (origen, destino) in enumerate(rutas.keys()):
            print(f'{i + 1}. {origen} ~ {destino}')
    
    def get_origen_destino(self, opcion):
        rutas = list(self.__rutas.keys())
        if 1 <= int(opcion) <= len(rutas):
            origen, destino = rutas[int(opcion) - 1]
            return origen, destino
        else:
            return None, None
    
    def verificar_usuario(self, nombre):
        usuarios = self.__usuarios
        for id_unico, usuario in usuarios.items():
            if Usuario.get_nombre(usuario) == nombre:
                return True, usuario
            else:
                return False, None
        
        



# sistema = Sistema()
# # sistema.add_unidad_black()
# # sistema.add_unidad_diamond()
# # sistema.add_unidad_express()
# # sistema.add_unidad_black()
# # sistema.add_unidad_diamond()
# # sistema.add_unidad_express()
# sistema.add_unidad_black()
# sistema.add_unidad_diamond()
# sistema.add_unidad_express()
# # sistema.listar_unidades()
# # print('~~~~~~~~~~~~~~~~~~~')
# # sistema.eliminar_unidad(201)
# # sistema.listar_unidades()
# sistema.add_usuario('pepe', "1")
# _, user = sistema.verificar_usuario('pepe')
# sistema.reservacion('Tacubaya', 'UAM-C', 'Express', user, '10/8', '08:00')
# sistema.reservaciones()

# sistema.add_usuario('pepe')
# sistema.inc_contador(3)
# sistema.add_usuario('pepe2')
# sistema.inc_contador(3)
# sistema.add_usuario('pepe3')
# sistema.inc_contador(3)
# sistema.add_usuario('pepe4')
# sistema.inc_contador(3)
# sistema.reservacion('Tacubaya','UAM-C','Express', 1)
# diccionario = {
#     ("Tacubaya", "UAM-C"): (13, 45),
#     ("Coacalco", "UAM-C"): (50, 90),
#     ("Pueblo de Santa Fe", "UAM-C"): (7, 30),
#     ("Zocalo", "UAM-C"): (35, 90),
#     ("UAM-C", "Tacubaya"): (13, 45),
#     ("UAM-C", "Coacalco"): (50, 90),
#     ("UAM-C", "Pueblo de Santa Fe"): (7, 30),
#     ("UAM-C", "Zocalo"): (35, 90)
# }

# print("~Rutas~")
# for i, (origen, destino) in enumerate(diccionario.keys()):
#     print(f"{i + 1}. {origen} ~ {destino}")
