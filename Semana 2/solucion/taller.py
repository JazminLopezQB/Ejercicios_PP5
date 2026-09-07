"""
TODO:
Implementá las clases de tu tabla en solucion/. La implementación debe proteger activamente al menos
una invariante derivada de una relación de composición: por ejemplo, un ItemDeTrabajo no puede
pertenecer a dos órdenes de trabajo al mismo tiempo. Python no rechaza esto solo — tu código sí tiene
que hacerlo, con una excepción, no con un if que el llamador puede ignorar.

orden_1 = OrdenDeTrabajo(numero=1, vehiculo=Vehiculo("AB123CD"))
item = ItemDeTrabajo("Cambio de pastillas", costo=8000)

orden_1.agregar_item(item)
assert orden_1.presupuesto() == 8000

orden_2 = OrdenDeTrabajo(numero=2, vehiculo=Vehiculo("XY987ZW"))
# el ítem ya pertenece a orden_1: esto debe rechazarse
# orden_2.agregar_item(item)  -> ValueError

"""

class Taller:
    def __init__(self, nombre):
        self.nombre = nombre
    
    def contratar_mecanico(self, mecanico):
        self.plantilla.append(mecanico)

    def despedir_mecanico(self, mecanico):
        self.plantilla.pop(mecanico)
    
    def iniciar_orden(self, orden):
        self.ordenes.append(orden)

class Mecanico:
    def __init__(self, nombre):
        self.nombre = nombre

class Vehiculo:
    def __init__(self, patente, conductor, orden):
        self.patente = patente
        self.conductor = conductor
        self.orden = orden

class ItemDeTrabajo:
    def __init__(self, Orden_Trabajo, nombre, costo):
        self.orden = Orden_Trabajo
        self.nombre = nombre
        self.costo = costo

class OrdenDeTrabajo:
    def __init__(self, numero, vehiculo, mecanico):
        self.numero = numero
        if vehiculo.orden != None:
                raise ValueError("El vehiculo ya está asociado a otra orden de trabajo.")
        self.vehiculo = vehiculo
        self.mecanico = mecanico

    def agregar_item(self, item):
        self.lista_items.append(item)

    def asignar_mecanico(self, mecanico):
        self.mecanico = Mecanico

    def presupuesto():
        for item in self.lista_items:
            presupuesto += self.lista_items.i.costo
        return presupuesto