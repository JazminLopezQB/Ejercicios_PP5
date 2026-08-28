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