from sistema_taxi import Sistema


class Menu:
    def __init__(self):
        self.__sistema = Sistema()

    def _opciones_menu(self, opcion):
        """ 
        Método para obtener las opciones de menú según la elección del usuario.
        Args:
            opcion (int): Número de opción de menú.
        """
        list_menu = [['~ M E N U   P R I N C I P A L~', '\t1. Administrador', '\t2. Usuario', '\t3. Salir'],
                     ['~ MENU ADMINISTRADOR ~', '\t1. Agregar unidad', '\t2. Eliminar unidad',
                      '\t3. Mostrar unidades', '\t4. Sacar del taller', '\t5. Guardar base de datos',
                      '\t6. Dar alta usuario', '\t7. Mostar usuarios', '\t8. Agregar ruta',
                      '\t9. Regresar'],
                     ['~ Seleccionar unidad ~', '\t1. Express', '\t2. Black', '\t3. Diamond'],
                     ['~ Menu cliente ~', '\t1. Reservar viaje', '\t2. Mostrar reservaciones',
                      '\t3. Cancelar reservacion', '\t4. Regresar', ]]
        return list_menu[opcion]

    def _print_opciones_menu(self, lista_opciones):
        """ 
        Método para imprimir las opciones de menú en la pantalla.
        Args:
            lista_opciones (list): Lista de opciones de menú.
        """
        for i in lista_opciones:
            print(i)

    def _seleccion_opcion(self, lista_opciones):
        """ 
        Método para seleccionar una opción de menú y obtener la clasificación de taxi correspondiente.
        Args:
            lista_opciones (list): Lista de opciones de menú.
        Returns:
            int: Opción seleccionada.
            str: Clasificación de taxi.
        """
        opcion_valida = False
        while not opcion_valida:
            seleccion = input('Seleccione una opcion (num): ')
            if seleccion.isdigit() and int(seleccion) >= 0 and int(seleccion) < len(lista_opciones):
                opcion_valida = True
            else:
                print('Opcion invalida, intente de nuevo')
        opcion_escogida = int(seleccion)
        tipo_taxi = lista_opciones[opcion_escogida].split()[-1]
        return opcion_escogida, tipo_taxi
    
    def _solicitar_ruta(self):
        """ 
        Método para solicitar al usuario que ingrese el número de ruta deseada.
        Returns:
            int: Número de ruta seleccionada.
        """
        valid = False
        while not valid:
            ruta = input('Ingrese la ruta deseada (num): ')
            if ruta.isdigit() and int(ruta) <= len(self.__sistema.get_rutas()):
                valid = True
            else:
                print('Ruta invalida, intente de nuevo')
        return ruta
    
    def _agregar_nueva_ruta(self):
        """ 
        Método para agregar una nueva ruta al sistema.
        """
        print("~~~ AGREGAR RUTA ~~~")
        origen = input("Origen: ")
        destino = input("Destino: ")
        distancia = input("Distancia (en km): ")
        tiempo = input("Tiempo (en minutos): ")

        if origen and destino and distancia.isdigit() and tiempo.isdigit():
            self.__sistema.agregar_ruta(origen, destino, int(distancia), int(tiempo))
            print("Ruta agregada exitosamente.")
        else:
            print("Error: Asegúrate de ingresar valores válidos para la ruta.")

    def _informacion_reservacion(self, usuario):
        """ 
        Método para obtener información de una reservación y realizarla.
        Args:
            usuario: Usuario que realiza la reservación.
        """
        try:
            self.__sistema.enlistar_rutas()
            ruta = self._solicitar_ruta()
            origen, destino = self.__sistema.get_origen_destino(ruta)
            lista_opciones = self._opciones_menu(2)
            self._print_opciones_menu(lista_opciones)
            _, clasificacion_taxi = self._seleccion_opcion(lista_opciones)
            fecha = self._solicitar_fecha_reservacion()
            hora = self._solicitar_hora_reservacion()
        except Exception as e:
            print('Disuclpe las molestias :c')
        else:
            self.__sistema.reservacion(origen, destino, clasificacion_taxi, usuario, fecha, hora)

    def _menu_agregar_unidad(self):
        """ 
        Método para mostrar y gestionar el menú de agregar una unidad al sistema.
        """
        opciones_menu = self._opciones_menu(2)
        self._print_opciones_menu(opciones_menu)
        seleccion, clasificacion_taxi = self._seleccion_opcion(opciones_menu)
        if seleccion == 1:
            self.__sistema.add_unidad_express()
        elif seleccion == 2:
            self.__sistema.add_unidad_black()
        else:
            self.__sistema.add_unidad_diamond()

    def _eliminar_unidad(self):
        """ 
        Método para eliminar una unidad del sistema.
        """
        no_eco = input('Ingrese el numero economico de la unidad a eliminar: ')
        self.__sistema.eliminar_unidad(no_eco)

    def _informacion_bancaria(self):
        """ 
        Método para obtener la información bancaria de un usuario.
        Returns:
            dict: Información bancaria (número de tarjeta, fecha de expiración, CVV).
        """
        tdc_num = self._solicitar_numero_tarjeta()
        tdc_exp_date = self._solicitar_fecha_expiracion()
        tdc_cvv = self._solicitar_cvv()
        return {'tdc': tdc_num, 'exp': tdc_exp_date, 'cvv': tdc_cvv}

    def _solicitar_numero_tarjeta(self):
        """ 
        Método para solicitar al usuario que ingrese el número de tarjeta de crédito.
        Returns:
            str: Número de tarjeta de crédito.
        """
        while True:
            tdc_num = input("Ingrese el número de tarjeta de crédito: ")
            if tdc_num.isdigit() and len(tdc_num) == 16:
                return tdc_num
            else:
                print("Número de tarjeta inválido. Debe contener solo dígitos y tener la longitud adecuada.")

    def _solicitar_fecha_expiracion(self):
        """ 
        Método para solicitar al usuario que ingrese la fecha de expiración de la tarjeta de crédito.
        Returns:
            str: Fecha de expiración (en el formato AA/MM).
        """
        while True:
            tdc_exp_date = input("Ingrese la fecha de expiración (AA/MM): ")
            if len(tdc_exp_date) == 5 and tdc_exp_date[:2].isdigit() and tdc_exp_date[2] == '/' and \
                    tdc_exp_date[3:].isdigit():
                return tdc_exp_date
            else:
                print("Fecha de expiración inválida. Debe estar en el formato adecuado (AA/MM).")

    def _solicitar_cvv(self):
        """ 
        Método para solicitar al usuario que ingrese el CVV de la tarjeta de crédito.
        Returns:
            str: CVV de la tarjeta de crédito.
        """
        while True:
            tdc_cvv = input("Ingrese los 3 dígitos de la tarjeta: ")
            if tdc_cvv.isdigit() and len(tdc_cvv) == 3:
                return tdc_cvv
            else:
                print("CVV inválido. Debe contener exactamente 3 dígitos.")

    def _solicitar_fecha_reservacion(self):
        """ 
        Método para solicitar al usuario que ingrese la fecha de reservación.
        Returns:
            str: Fecha de reservación (en el formato DD/MM).
        """
        while True:
            reservacion_date = input("Ingrese la fecha de reservacion (DD/MM): ")
            if len(reservacion_date) == 5 and reservacion_date[:2].isdigit() and reservacion_date[2] == '/' and \
                    reservacion_date[3:].isdigit():
                return reservacion_date
            else:
                print("Fecha de reservacion inválida. Debe estar en el formato adecuado (AA/MM).")

    def _solicitar_hora_reservacion(self):
        """ 
        Método para solicitar al usuario que ingrese la hora de reservación.
        Returns:
            str: Hora de reservación (en el formato HH:MM).
        """
        while True:
            reservacion_hora = input("Ingrese la hora del viaje (HH:MM): ")
            if len(reservacion_hora) == 5 and reservacion_hora[:2].isdigit() and reservacion_hora[2] == ':' and \
                    reservacion_hora[3:].isdigit():
                return reservacion_hora
            else:
                print("Fecha de reservacion inválida. Debe estar en el formato adecuado de 24 hrs (HH:MM).")

    def _dar_alta_usuario(self):
        """ 
        Método para dar de alta a un nuevo usuario en el sistema.
        """
        nombre = input("Ingrese el nombre del usuario: ")
        tdc = self._informacion_bancaria()
        self.__sistema.add_usuario(nombre, tdc)

    def _menu_usuario(self, usuario):
        """ 
        Método para mostrar y gestionar el menú del usuario.
        Args:
            usuario: Usuario que realiza las acciones.
        """
        opciones_menu = self._opciones_menu(3)
        self._print_opciones_menu(opciones_menu)
        seleccion, _ = self._seleccion_opcion(opciones_menu)
        if seleccion == 1:
            self._informacion_reservacion(usuario)
            self._menu_usuario(usuario)
        elif seleccion == 2:
            self.__sistema.enlistar_reservaciones(usuario)
            self._menu_usuario(usuario)
        elif seleccion == 3:
            self.__sistema.enlistar_reservaciones(usuario)
            self.__sistema.cancelar_reservacion(usuario)
            self._menu_usuario(usuario)
        else:
            self._menu_principal()

    def _menu_principal(self):
        """ 
        Método para mostrar y gestionar el menú principal del sistema.
        """
        menu_opciones = self._opciones_menu(0)
        self._print_opciones_menu(menu_opciones)
        seleccion, _ = self._seleccion_opcion(menu_opciones)
        if seleccion == 1:
            self._menu_admin()
        elif seleccion == 2:
            nombre = input('Ingrese el nombre: ')
            encontrado, usuario = self.__sistema.verificar_usuario(nombre)
            if encontrado:
                self._menu_usuario(usuario)
            else:
                print(
                    'Usuario no encontrado. Verifique que esta bien escrito el nombre \n o Comuniquese con el administrador para darle de alta')
                self._menu_principal()
        else:
            return

    def _menu_admin(self):
        """ 
        Método para mostrar y gestionar el menú del administrador.
        """
        opciones__menu_admin = self._opciones_menu(1)
        self._print_opciones_menu(opciones__menu_admin)
        seleccion, _ = self._seleccion_opcion(opciones__menu_admin)
        if seleccion == 1:
            self._menu_agregar_unidad()
            self._menu_admin()
        elif seleccion == 2:
            self._eliminar_unidad()
            self._menu_admin()
        elif seleccion == 3:
            self.__sistema.listar_unidades()
            self._menu_admin()
        elif seleccion == 4:
            no_eco = input('Ingrese el numero economico de la unidad: ')
            self.__sistema.sacar_unidad_taller(no_eco)
            self._menu_admin()
        elif seleccion == 5:
            self.__sistema.save_database_unidades()
            self.__sistema.save_database_usuarios()
            self._menu_admin()
        elif seleccion == 6:
            self._dar_alta_usuario()
            self._menu_admin()
        elif seleccion == 7:
            self.__sistema.listar_usuarios()
            self._menu_admin()
        elif seleccion == 8:
            self._agregar_nueva_ruta()
            self._menu_admin()
        else:
            self._menu_principal()

    def iniciar_sistema(self):
        """ 
        Método para iniciar el sistema y cargar datos desde la base de datos.
        """
        self.__sistema.load_database_unidades()
        self.__sistema.load_database_usuarios()
        self._menu_principal()