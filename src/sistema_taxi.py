from black import Black
from express import Express
from diamond import Diamond
from usuario import Usuario
from random import choice
from pickle import load, dump


class Sistema:
    def __init__(self):
        self.__usuarios = {}
        self.__unidades = {'Express': [], 'Black': [], 'Diamond': []}
        self.__contador = 1000  # [express, black, diamond, id]
        self.__descuento = 0.15
        self.__rutas = {
            ("Tacubaya", "UAM-C"): (13, 45),
            ("Coacalco", "UAM-C"): (50, 90),
            ("Pueblo de Santa Fe", "UAM-C"): (7, 30),
            ("Zocalo", "UAM-C"): (35, 90),
            ("UAM-C", "Tacubaya"): (13, 45),
            ("UAM-C", "Coacalco"): (50, 90),
            ("UAM-C", "Pueblo de Santa Fe"): (7, 30),
            ("UAM-C", "Zocalo"): (35, 90)
        }

    def tiempo_distancia_viaje(self, origen, destino):
        # Verifica si la ruta está en el diccionario
        if (origen, destino) in self.__rutas:
            distancia, tiempo = self.__rutas[(origen, destino)]
            return distancia, tiempo

    def add_unidad_express(self):
        no_eco = self.__contador
        self.__unidades['Express'].append(Express(no_eco))
        self.inc_contador()

    def add_unidad_black(self):
        no_eco = self.__contador
        self.__unidades['Black'].append(Black(no_eco))
        self.inc_contador()

    def add_unidad_diamond(self):
        no_eco = self.__contador
        self.__unidades['Diamond'].append(Diamond(no_eco))
        self.inc_contador()

    def add_usuario(self, nombre, tdc):
        self.__usuarios[nombre] = Usuario(nombre, tdc)

    def _eliminar_unidad(self, no_eco):
        unidades = self.__unidades
        for clasificacion_taxi, lista_taxis in unidades.items():
            for unidad in lista_taxis:
                if unidad.get_numero_economico() == int(no_eco):
                    self.__unidades[clasificacion_taxi].remove(unidad)

    def inc_contador(self):
        self.__contador += 1

    def listar_unidades(self):
        unidades = self.__unidades
        for clasificacion, lista_unidades in unidades.items():
            for unidad in lista_unidades:
                print(f'{unidad.__str__()} \t {clasificacion}')

    def listar_usuarios(self):
        usuarios = self.__usuarios
        for nombre, usuario in usuarios.items():
            print(f'~~~')
            print(f'~ Nombre usuario:{nombre}')
            print(f'~ Viajes realizados:{usuario.get_viajes_count()}')

    def get_unidad(self, clasificacion_taxi):
        unidades = self.__unidades[clasificacion_taxi]
        unidad = choice(unidades)
        if unidad.get_en_mantenimiento():
            unidad = choice(unidades)
        unidad.viaje_hecho()
        unidad.mantenimiento()
        return unidad

    def precio_parcial_viaje(self, origen, destino, unidad):
        tarifa_distancia = unidad.get_tarifa_km()
        tarifa_tiempo = unidad.get_tarifa_min()
        tarifa_base = unidad.get_tarifa_base()
        distancia, tiempo = self.tiempo_distancia_viaje(origen, destino)
        total = tarifa_base + (distancia * tarifa_distancia) + (tarifa_tiempo * tiempo)
        return total

    def aplicar_promocion(self, total):
        return total - (total * self.__descuento)

    def obtener_total_viaje(self, origen, destino, unidad, usuario):
        total = self.precio_parcial_viaje(origen, destino, unidad)
        if not Usuario.get_status_aplicable_descuento(usuario):
            print(f'El total a pagar es de {total}')
        else:
            total = self.aplicar_promocion(total)
            print(f'Fue elegido para una promocion y el total es de {total}')
        return total

    def reservacion(self, origen, destino, clasificacion_taxi, usuario, fecha, hora):
        # {'Tipo de unidad': tipo de unidad, 'Origen': origen, 'destino', 'fecha': fecha, 'hora':hora}
        reservacion = {}
        reservacion['Tipo Unidad'] = clasificacion_taxi
        reservacion['Origen'] = origen
        reservacion['Destino'] = destino
        reservacion['Fecha'] = fecha
        reservacion['Hora'] = hora
        Usuario.set_reservacion(usuario, reservacion)
        unidad = self.get_unidad(clasificacion_taxi)
        total = self.obtener_total_viaje(origen, destino, unidad, usuario)
        reservacion['Total'] = total
        usuario.change_staus_aplicable_descuento()

    def sacar_unidad_taller(self, no_eco):
        unidad = self.__unidades[no_eco]
        unidad.mantenimiento_finalizado()

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
        for nombre, usuario in usuarios.items():
            if Usuario.get_nombre(usuario) == nombre:
                return True, usuario
            else:
                return False, None

    def set_contador(self):
        data_base_unidades = self.__unidades
        contador = 1000
        for tipo_unidad, lista_unidades in data_base_unidades.items():
            for unidad in lista_unidades:
                no_eco = Express.get_numero_economico(unidad)
                if no_eco > contador:
                    contador = no_eco
        self.__contador = contador + 1

    def load_database_unidades(self):
        try:
            with open('database_unidades', "rb") as file:
                self.__unidades = load(file)
        except FileNotFoundError:
            self.__unidades = {'Express': [], 'Black': [], 'Diamond': []}
            print('Base de datos no encontrada, se ha inicializado con valores vacíos.')
        else:
            self.set_contador()
            print('Base de datos de unidades cargada con exito!')

    def load_database_usuarios(self):
        try:
            with open('database_usuarios', "rb") as file:
                self.__usuarios = load(file)
        except FileNotFoundError:
            self.__usuarios = {}
            print('Base de datos no encontrada, se ha inicializado con valores vacíos.')
        else:
            print('Base de datos de usuarios cargado con exito!')

    def save_database_unidades(self):
        try:
            with open('database_unidades', "wb") as file:
                dump(self.__unidades, file)
        except Exception as e:
            print(f'Error al guardar la base de datoss de unidades: {e}')
        else:
            print('Base de datos de unidades guardada con exito.')

    def save_database_usuarios(self):
        try:
            with open('database_usuarios', "wb") as file:
                dump(self.__usuarios, file)
        except Exception as e:
            print(f'Error al guardar la base de datos de usuarios : {e}')
        else:
            print("Base de datos de usuarios guardada con exito.")

    def enlistar_reservaciones(self, usuario):
        reservaciones = Usuario.get_reservaciones(usuario)
        for i, reservacion in enumerate(reservaciones):
            print(f'Reservacion: {i + 1}')
            for key, value in reservacion.items():
                print(f'    {key}: {value}')

    def cancelar_reservacion(self, usuario):
        no_reservacion = input('Ingrese la reservacion a cancelar (num): ')
        Usuario.delete_reservacion(usuario, no_reservacion)
