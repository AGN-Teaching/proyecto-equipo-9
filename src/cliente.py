class SistemaDeTaxis:
    def __init__(self):
        self.rutas = {
            ("Tacubaya", "UAM-C"): (13, 45),
            ("Coacalco", "UAM-C"): (50, 90),
            ("Pueblo de Santa Fe", "UAM-C"): (7, 30),
            ("Zocalo", "UAM-C"): (35, 90)
        }

    def tiempo_distancia_viaje(self, origen, destino):
        # Verifica si la ruta está en el diccionario
        if (origen, destino) in self.rutas:
            distancia, tiempo = self.rutas[(origen, destino)]
            return distancia, tiempo

sistema = SistemaDeTaxis()
origen = "Zocalo"
destino = "UAM-C"
distancia, tiempo = sistema.tiempo_distancia_viaje(origen, destino)
if distancia is not None:
    print(f"Distancia: {distancia} km, Tiempo: {tiempo} minutos")
