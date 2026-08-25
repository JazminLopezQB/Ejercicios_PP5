"""
TODO: Hacer test que cubran
Camino feliz: armar una orden, agregarle ítems, asignarle un mecánico, calcular el presupuesto.
Rechazo: intentar violar la invariante protegida (por ejemplo, agregar el mismo ítem a dos órdenes).
Que el rechazo no deja estado a medias: después de la excepción, verificá explícitamente que la
segunda orden no quedó con el ítem a medio agregar y que el ítem sigue apuntando a su orden original.
"""