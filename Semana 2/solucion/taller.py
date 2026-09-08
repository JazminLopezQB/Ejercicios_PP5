class ParteOrden:
    def __init__(self, nombre):
        self.nombre = nombre
        self.orden = None

class Mecanico(ParteOrden): # Los mecanicos se identifican por su id y nombre
    def __init__(self, nombre, identificador):
        super().__init__(nombre)
        self.id = identificador

    def detalles(self):
        print(f"- {self.nombre} (ID: {self.id})\n")

class Vehiculo(ParteOrden): # Un vehiculo tiene una patente que lo identifica, un dueño y una orden de trabajo asociada
    def __init__(self, patente, conductor):
        super().__init__(patente)
        self.conductor = conductor

class ItemDeTrabajo(ParteOrden): # Un item de trabajo tiene un nombre que lo identifica, un costo y una orden de trabajo asociada
    def __init__(self, nombre, costo):
        super().__init__(nombre)
        self.costo = costo

class OrdenDeTrabajo:
    def __init__(self, numero, vehiculo, mecanico):
        self.numero = numero
        if vehiculo.orden != None:
            raise ValueError("El vehiculo ya está asociado a otra orden de trabajo.")
        self.vehiculo = vehiculo
        self.vehiculo.orden = self
        self.mecanico = mecanico
        self.lista_items = []

    def agregar_item(self, item):
        if item.orden != None:
            raise ValueError("El item ya está asociado a otra orden de trabajo.")
        self.lista_items.append(item)
        item.orden = self

    def asignar_mecanico(self, mecanico):
        self.mecanico = mecanico

    def presupuesto(self):
        return sum(item.costo for item in self.lista_items)

    def detalles(self):
        print(f"--- N° {self.numero} ---\n")
        print(f"\tVehiculo: {self.vehiculo.nombre}\n\tMecanico: {self.mecanico.nombre}\n\tItems:\n")
        for i in self.lista_items:
            print(f"\t\t{i.nombre} - {i.costo}\n")
        print(f"\tPresupuesto: {self.presupuesto()}\n")

class Taller: # Un taller tiene una plantilla de mecanicos, una lista de ordenes y un nombre identificador
    def __init__(self, nombre):
        self.nombre = nombre
        self.plantilla = []
        self.ordenes = []
    
    def contratar_mecanico(self, mecanico):
        self.plantilla.append(mecanico)

    def despedir_mecanico(self, mecanico):
        if mecanico in self.plantilla:
            self.plantilla.remove(mecanico)
    
    def asociar_orden(self, orden):
        self.ordenes.append(orden)
    
    def ver_detalles(self):
        print(f"--- Taller {self.nombre} ---\nMecanicos Afiliados:\n")
        for m in self.plantilla:
            m.detalles()
        for o in self.ordenes:
            o.detalles()





