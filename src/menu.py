from sistema_taxi import Sistema
from usuario import Usuario
class Menu():
    def __init__(self):
        self.__sistema = Sistema()

    def _opciones_menu(self, opcion):
        list = [['~ M E N U   P R I N C I P A L~', '\t1. Administrador', '\t2. Usuario', '\t3. Salir'],
                ['~ MENU ADMINISTRADOR ~', '\t1. Agregar unidad', '\t2. Eliminar unidad', '\t3. Mostrar unidades', '\t4. Cargar base de datos','\t5. Guardar base de datos', '\t6. Dar alta usuario','\t7. Enlistar reservaciones', '\t8. Regresar'],
                ['~ Seleccionar unidad ~', '\t1. Express', '\t2. Black', '\t3. Diamond'],
                ['~ Menu cliente ~', '\t1. Reservar viaje', '\t2. Regresar']]
        return list[opcion]
    
    def _print_opciones_menu(self, lista_opciones):
        for i in lista_opciones:
            print(i)

    def _seleccion_opcion(self, lista_opciones):
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
    
    def _informacion_reservacion(self, usuario):
        self.__sistema.enlistar_rutas()
        ruta = input("Ingrese la ruta deseada (num):")
        origen,destino = self.__sistema.get_origen_destino(ruta)
        lista_opciones = self._opciones_menu(2) 
        self._print_opciones_menu(lista_opciones)
        _, clasificacion_taxi = self._seleccion_opcion(lista_opciones)
        fecha = input("Ingrese la fecha(DD/MM): ")
        hora = input('Ingrese la hora(HH:MM):')
        self.__sistema.reservacion(origen, destino, clasificacion_taxi, usuario, fecha, hora)

    def menu_agregar_unidad(self):
        opciones_menu = self._opciones_menu(2)
        self._print_opciones_menu(opciones_menu)
        seleccion, clasificacion_taxi = self._seleccion_opcion(opciones_menu)
        if seleccion == 1:
            self.__sistema.add_unidad_express()
        elif seleccion == 2:
            self.__sistema.add_unidad_black()
        else:
            self.__sistema.add_unidad_diamond()
            
    def eliminar_unidad(self):
        no_eco = input('Ingrese el numero economico de la unidad a eliminar: ')
        self.__sistema.eliminar_unidad(no_eco)

    def dar_alta_usuario(self):
        nombre= input ("Ingrese el nombre del usuario: ")
        tdc= input ("Ingrese el numero de tarjeta de credito: ")
        self.__sistema.add_usuario(nombre, tdc)

    def menu_usuario(self, usuario):
        opciones_menu = self._opciones_menu(3)
        self._print_opciones_menu(opciones_menu)
        seleccion, _ = self._seleccion_opcion(opciones_menu)
        if seleccion == 1:
            self._informacion_reservacion(usuario)
            self.menu_principal()
        else:
            self.menu_principal
        
    def menu_principal(self):
        menu_opciones = self._opciones_menu(0)
        self._print_opciones_menu(menu_opciones)
        seleccion, _ = self._seleccion_opcion(menu_opciones)
        if seleccion == 1:
            self.menu_admin()
        elif seleccion == 2:
            nombre = input('Ingrese el nombre: ')
            encontrado, usuario = self.__sistema.verificar_usuario(nombre)
            if encontrado:
                self.menu_usuario(usuario)
            else:
                print('Usuario no encontrado. Verifique que esta bien escrito el nombre \n O Comuniquese con el administrador para darle de alta')
        else:
            return

    def menu_admin(self):
        opciones_menu_admin= self._opciones_menu(1)
        self._print_opciones_menu(opciones_menu_admin)
        seleccion, _= self._seleccion_opcion(opciones_menu_admin)
        if seleccion == 1:
            self.menu_agregar_unidad()
            self.menu_admin()
        elif seleccion==2:
            self.eliminar_unidad()
            self.menu_admin()
        elif seleccion==3:
            self.__sistema.listar_unidades()
            self.menu_admin()
        elif seleccion==4:
            return 
        elif seleccion==5:
            return
        elif seleccion==6:
            self.dar_alta_usuario()
            self.menu_admin()
        elif seleccion ==7:
            self.__sistema.enlistar_reservaciones()
            self.menu_admin()
        else:
            self.menu_principal()
    

    def iniciar_sistema(self):
        while True:
            self.menu_principal()

menu = Menu()
menu.menu_principal()
