
class Taller: # Un taller tiene una plantilla de mecanicos, una lista de ordenes y un nombre identificador
    def __init__(self, nombre):
        self.nombre = nombre
    
    def contratar_mecanico(self, mecanico):
        self.plantilla.append(mecanico)

    def despedir_mecanico(self, mecanico):
        self.plantilla.pop(mecanico)
    
    def iniciar_orden(self, orden):
        self.ordenes.append(orden)
    
    def ver_detalles(self):
        print("Mecanicos Afiliados:\n")
        for m in self.plantilla:
            print(f"- {self.plantilla[m].nombre} ({self.plantilla[m].id})\n\t- Ordenes:\n")
            for o in self.plantilla[m].ordenes:
                print(f"{self.plantilla[m].ordenes[o].numero}\n")

class ParteOrden:
    def __init__(self, nombre):
        self.nombre = nombre
        self.orden = None

    def asociar_orden(self, orden):
        self.orden.append(orden)

class Mecanico(ParteOrden): # Los mecanicos se identifican por su id y nombre
    def __init__(self, identificador):
        self.id = identificador

class Vehiculo(ParteOrden): # Un vehiculo tiene una patente que lo identifica, un dueño y una orden de trabajo asociada
    def __init__(self, conductor):
        self.conductor = conductor

class ItemDeTrabajo(ParteOrden): # Un item de trabajo tiene un nombre que lo identifica, un costo y una orden de trabajo asociada
    def __init__(self, nombre, costo):
        self.orden = orden_trabajo
        self.costo = costo

class OrdenDeTrabajo:
    def __init__(self, numero, vehiculo, mecanico):
        self.numero = numero
        if vehiculo.orden != None:
                raise ValueError("El vehiculo ya está asociado a otra orden de trabajo.")
        self.vehiculo = vehiculo
        self.mecanico = mecanico

    def agregar_item(self, item):
        if item.orden != None:
            raise ValueError("El item ya está asociado a otra orden de trabajo.")
        self.lista_items.append(item)

    def asignar_mecanico(self, mecanico):
        self.mecanico = mecanico

    def presupuesto():
        for item in self.lista_items:
            presupuesto += self.lista_items[i].costo
        return presupuesto