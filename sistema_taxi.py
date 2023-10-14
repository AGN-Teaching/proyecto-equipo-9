from black import Black
from express import Express
from diamond import Diamond
from usuario import Usuario
from random import choice
from pickle import load, dump


class Sistema:
    def __init__(self):
        """
        Inicializa el sistema de gestión de taxis con listas de usuarios, unidades, un contador, descuento, y rutas predefinidas.
        """
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

    def _tiempo_distancia_viaje(self, origen, destino):
        """
        Obtiene la distancia y el tiempo de viaje entre dos ubicaciones (origen y destino) en función de las rutas predefinidas.
        Args:
            origen (str): Ubicación de origen del viaje.
            destino (str): Ubicación de destino del viaje.
        Returns:
            tuple: Tupla con la distancia (en km) y el tiempo estimado (en minutos) del viaje.
        """
        # Verifica si la ruta está en el diccionario
        if (origen, destino) in self.__rutas:
            distancia, tiempo = self.__rutas[(origen, destino)]
            return distancia, tiempo

    def add_unidad_express(self):
        """
        Agrega una nueva unidad de taxi de tipo "Express" al sistema.
        """
        no_eco = self.__contador
        self.__unidades['Express'].append(Express(no_eco))
        self._inc_contador()

    def add_unidad_black(self):
        """
        Agrega una nueva unidad de taxi de tipo "Black" al sistema.
        """
        no_eco = self.__contador
        self.__unidades['Black'].append(Black(no_eco))
        self._inc_contador()

    def add_unidad_diamond(self):
        """
        Agrega una nueva unidad de taxi de tipo "Diamond" al sistema.
        """
        no_eco = self.__contador
        self.__unidades['Diamond'].append(Diamond(no_eco))
        self._inc_contador()

    def add_usuario(self, nombre, tdc):
        """
        Agrega un nuevo usuario al sistema.
        Args:
            nombre (str): Nombre del usuario.
            tdc (dict): Información de la tarjeta de crédito (número, fecha de expiración, CVV, etc.).
        """
        self.__usuarios[nombre] = Usuario(nombre, tdc)

    def eliminar_unidad(self, no_eco):
        """
        Elimina una unidad de taxi del sistema por su número económico.
        Args:
            no_eco (int): Número económico de la unidad de taxi a eliminar.
        """
        unidades = self.__unidades
        for clasificacion_taxi, lista_taxis in unidades.items():
            for unidad in lista_taxis:
                if unidad.get_numero_economico() == int(no_eco):
                    self.__unidades[clasificacion_taxi].remove(unidad)

    def _inc_contador(self):
        """
        Incrementa el contador de números económicos para las unidades de taxi.
        """
        self.__contador += 1

    def listar_unidades(self):
        """
        Muestra la información de las unidades de taxi en el sistema.
        """
        unidades = self.__unidades
        for clasificacion, lista_unidades in unidades.items():
            for unidad in lista_unidades:
                print(f'{unidad.__str__()} \t {clasificacion}')

    def listar_usuarios(self):
        """
        Muestra la información de los usuarios registrados en el sistema.
        """
        usuarios = self.__usuarios
        for nombre, usuario in usuarios.items():
            print(f'~~~')
            print(f'~ Nombre usuario: {nombre}')
            print(f'~ Viajes realizados: {usuario.get_viajes_count()}')

    def _get_unidad(self, clasificacion_taxi):
        """
        Obtiene una unidad de taxi disponible al azar dentro de una clasificación específica.
        Args:
            clasificacion_taxi (str): Clasificación del taxi (Express, Black, Diamond).
        Returns:
            Unidad: Una unidad de taxi disponible.
        """
        try:
            unidades_disponibles = [unidad for unidad in self.__unidades[clasificacion_taxi] if not unidad.get_en_mantenimiento()]
    
            if not unidades_disponibles:
                return None
    
            unidad = choice(unidades_disponibles)
            unidad.viaje_hecho()
            unidad.mantenimiento()
            return unidad
        except IndexError:
            print(f'Disculpe las molestias')

    def _precio_parcial_viaje(self, origen, destino, unidad):
        """
        Calcula el precio parcial de un viaje en función de la unidad de taxi y la distancia/tiempo entre origen y destino.
        Args:
            origen (str): Ubicación de origen del viaje.
            destino (str): Ubicación de destino del viaje.
            unidad (Unidad): Una unidad de taxi.
        Returns:
            float: Precio parcial del viaje.
        """
        tarifa_distancia = unidad.get_tarifa_km()
        tarifa_tiempo = unidad.get_tarifa_min()
        tarifa_base = unidad.get_tarifa_base()
        distancia, tiempo = self._tiempo_distancia_viaje(origen, destino)
        total = tarifa_base + (distancia * tarifa_distancia) + (tarifa_tiempo * tiempo)
        return total

    def _aplicar_promoción(self, total):
        """
        Aplica un descuento de promoción al precio total de un viaje.
        Args:
            total (float): Precio total del viaje.
        Returns:
            float: Precio total del viaje con el descuento aplicado.
        """
        return total - (total * self.__descuento)

    def _obtener_total_viaje(self, origen, destino, unidad, usuario):
        """
        Calcula el precio total de un viaje, aplicando o no un descuento de promoción.
        Args:
            origen (str): Ubicación de origen del viaje.
            destino (str): Ubicación de destino del viaje.
            unidad (Unidad): Una unidad de taxi.
            usuario (Usuario): Un usuario que realiza el viaje.
        Returns:
            float: Precio total del viaje.
        """
        total = self._precio_parcial_viaje(origen, destino, unidad)
        if not usuario.get_status_aplicable_descuento():
            print(f'El total a pagar es de {total}')
        else:
            total = self._aplicar_promoción(total)
            print(f'Fue elegido para una promoción y el total es de {total}')
        return total

    def reservacion(self, origen, destino, clasificacion_taxi, usuario, fecha, hora):
        """
        Realiza una reservación de un viaje en una unidad de taxi.
        Args:
            origen (str): Ubicación de origen del viaje.
            destino (str): Ubicación de destino del viaje.
            clasificacion_taxi (str): Clasificación del taxi (Express, Black, Diamond).
            usuario (Usuario): Un usuario que realiza el viaje.
            fecha (str): Fecha de la reservación (en formato 'dd/mm').
            hora (int): Hora de la reservación (en minutos).
        """
        unidad = self._get_unidad(clasificacion_taxi)
        if unidad is None:
            print("No se pudo realizar la reservación debido a la falta de unidades disponibles.")
        else:
            reservacion = {
                'Tipo Unidad': clasificacion_taxi,
                'Origen': origen,
                'Destino': destino,
                'Fecha': fecha,
                'Hora': hora
            }
            usuario.set_reservacion(reservacion)
            total = self._obtener_total_viaje(origen, destino, unidad, usuario)
            reservacion['Total'] = total
            usuario.change_status_aplicable_descuento()
            usuario.add_count_viajes()

    def sacar_unidad_taller(self, no_eco):
        """
        Saca una unidad de taxi del taller después de un período de mantenimiento.
        Args:
            no_eco (int): Número económico de la unidad de taxi que sale del taller.
        """
        try:
            unidad = self.__unidades[no_eco]
            unidad.mantenimiento_finalizado()
        except KeyError:
            pass

    def enlistar_rutas(self):
        """
        Muestra una lista de las rutas disponibles en el sistema.
        """
        rutas = self.__rutas
        for i, (origen, destino) in enumerate(rutas.keys()):
            print(f'{i + 1}. {origen} ~ {destino}')

    def get_origen_destino(self, opcion):
        """
        Obtiene el origen y destino correspondientes a una opción de ruta seleccionada.
        Args:
            opcion (str): Opción de ruta seleccionada.
        Returns:
            str, str: Origen y destino de la ruta correspondiente a la opción seleccionada.
        """
        rutas = list(self.__rutas.keys())
        if 1 <= int(opcion) <= len(rutas):
            origen, destino = rutas[int(opcion) - 1]
            return origen, destino
        else:
            return None, None

    def get_rutas(self):
        """
        Obtiene la lista de rutas definidas en el sistema.
        Returns:
            dict: Diccionario con rutas y sus distancias/tiempos correspondientes.
        """
        return self.__rutas

    def verificar_usuario(self, nombre):
        """
        Verifica si un usuario con el nombre especificado existe en el sistema.
        Args:
            nombre (str): Nombre de usuario a verificar.
        Returns:
            bool: True si el usuario existe en el sistema, False si no.
            Usuario: El objeto de usuario si existe, None si no.
        """
        try:
            usuarios = self.__usuarios
            for key, usuario in usuarios.items():
                if usuario.get_nombre() == nombre:
                    return True, usuario
            return False, None
        except ArithmeticError:
            pass

    def _set_contador(self):
        """
        Establece el contador de números económicos para las unidades de taxi.
        """
        data_base_unidades = self.__unidades
        contador = 1000
        for tipo_unidad, lista_unidades in data_base_unidades.items():
            for unidad in lista_unidades:
                no_eco = unidad.get_numero_economico()
                if no_eco > contador:
                    contador = no_eco
        self.__contador = contador + 1

    def load_database_unidades(self):
        """
        Carga la base de datos de unidades de taxi desde un archivo pickle.
        """
        try:
            with open('database_unidades', "rb") as file:
                self.__unidades = load(file)
        except FileNotFoundError:
            self.__unidades = {'Express': [], 'Black': [], 'Diamond': []}
            print('Base de datos de Unidades no encontrada, se ha inicializado con valores vacíos.')
        else:
            self._set_contador()
            print('Base de datos de unidades cargada con éxito!')

    def load_database_usuarios(self):
        """
        Carga la base de datos de usuarios desde un archivo pickle.
        """
        try:
            with open('database_usuarios', "rb") as file:
                self.__usuarios = load(file)
        except FileNotFoundError:
            self.__usuarios = {}
            print('Base de datos de Usuarios no encontrada, se ha inicializado con valores vacíos.')
        else:
            print('Base de datos de usuarios cargado con éxito!')

    def save_database_unidades(self):
        """
        Guarda la base de datos de unidades de taxi en un archivo pickle.
        """
        try:
            with open('database_unidades', "wb") as file:
                dump(self.__unidades, file)
        except Exception as e:
            print(f'Error al guardar la base de datos de unidades: {e}')
        else:
            print('Base de datos de unidades guardada con éxito.')

    def save_database_usuarios(self):
        """
        Guarda la base de datos de usuarios en un archivo pickle.
        """
        try:
            with open('database_usuarios', "wb") as file:
                dump(self.__usuarios, file)
        except Exception as e:
            print(f'Error al guardar la base de datos de usuarios: {e}')
        else:
            print("Base de datos de usuarios guardada con éxito.")

    def enlistar_reservaciones(self, usuario):
        """
        Muestra la lista de reservaciones de un usuario.
        Args:
            usuario (Usuario): El usuario del que se mostrarán las reservaciones.
        """
        reservaciones = usuario.get_reservaciones()
        for i, reservacion in enumerate(reservaciones):
            print(f'Reservación: {i + 1}')
            for key, value in reservacion.items():
                print(f'    {key}: {value}')

    def cancelar_reservacion(self, usuario):
        """
        Cancela una reservación de un usuario.
        Args:
            usuario (Usuario): El usuario que cancelará una reservación.
        """
        no_reservacion = input('Ingrese la reservación a cancelar (num): ')
        usuario.delete_reservacion(no_reservacion)

    def agregar_ruta(self, origen, destino, distancia, tiempo):
        """
        Agrega una nueva ruta al sistema.
        Args:
            origen (str): Ubicación de origen de la ruta.
            destino (str): Ubicación de destino de la ruta.
            distancia (int): Distancia de la ruta en kilómetros.
            tiempo (int): Tiempo estimado de la ruta en minutos.
        """
        # Asegurarse de que la ruta no exista ya
        if (origen, destino) not in self.__rutas:
            self.__rutas[(origen, destino)] = (distancia, tiempo)
            print(f'Ruta agregada: {origen} ~ {destino}')
        else:
            print(f'La ruta {origen} ~ {destino} ya existe en el sistema.')