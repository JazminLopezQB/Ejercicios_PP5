# Problema 2: Órdenes de trabajo de un taller mecánico

## Enunciado Práctico

Un taller mecánico recibe vehículos, arma una orden de trabajo por cada visita y le va agregando ítems de trabajo (mano de obra, repuestos) a medida que el mecánico revisa el auto. El taller tiene una plantilla de mecánicos disponibles, pero no todos están asignados a una orden en un momento dado.

Implementá las clases de tu tabla en `solucion/`. La implementación debe proteger activamente al menos una invariante derivada de una relación de composición: por ejemplo, un `ItemDeTrabajo` no puede pertenecer a dos órdenes de trabajo al mismo tiempo. Python no rechaza esto solo — tu código sí tiene que hacerlo, con una excepción, no con un `if` que el llamador puede ignorar.
```
orden_1 = OrdenDeTrabajo(numero=1, vehiculo=Vehiculo("AB123CD"))
item = ItemDeTrabajo("Cambio de pastillas", costo=8000)

orden_1.agregar_item(item)
assert orden_1.presupuesto() == 8000

orden_2 = OrdenDeTrabajo(numero=2, vehiculo=Vehiculo("XY987ZW"))
# el ítem ya pertenece a orden_1: esto debe rechazarse
# orden_2.agregar_item(item)  -> ValueError
```

- Escribí tests en `tests/` que cubran:
    - Camino feliz: armar una orden, agregarle ítems, asignarle un mecánico, calcular el presupuesto.
    - Rechazo: intentar violar la invariante protegida (por ejemplo, agregar el mismo ítem a dos órdenes).
    - Que el rechazo no deja estado a medias: después de la excepción, verificá explícitamente que la segunda orden no quedó con el ítem a medio agregar y que el ítem sigue apuntando a su orden original.

## Enuncidados Teórico

### Análisis del Dominio

- Antes de escribir una línea de código, respondé por escrito:
    - Qué conceptos del enunciado aparecen (orden de trabajo, ítem de trabajo, vehículo, mecánico, taller, presupuesto...).
    - Cuáles de esos conceptos NO se convierten en clase, y por qué. Por ejemplo: si "presupuesto" es simplemente un número que se calcula a partir de los ítems y nunca se guarda ni viaja con estado propio, puede que no merezca ser una clase — pero justificá tu decisión, no la copies de acá.

#### Conceptos del Enunciado

- Taller Mecánico
- Vehiculos
- Orden de trabajo
- Visita
- Items de trabajo
- Mano de obra
- Repuestos
- Mecánico
- Plantilla de Mecanicos disponibles

#### Conceptos que No se Convierten en Clases

- **Visita**: No se convierte en clase ya que se ve representada por una orden de trabajo.
- **Mano de Obra**: No tiene una responsabilidad, puede abstraerse como un atributo de OrdenDeTrabajo.
- **Repuestos**: Idem a la mano de obra.
- **Plantilla de Mecanicos disponibles**: Es la relación entre los mecánicos y el taller, no una clase en sí al no tener comportamientos propios.

### Tarjetas CRC

Escribí una tarjeta CRC (Clase, Responsabilidades, Colaboradores) para cada clase central que hayas identificado. Como mínimo se espera OrdenDeTrabajo, ItemDeTrabajo, Vehiculo, Mecanico y Taller, pero el conjunto final es tu decisión de diseño.

```
Clase: OrdenDeTrabajo
Responsabilidades: agregar ítems, calcular presupuesto, saber si está cerrada
Colaboradores: ItemDeTrabajo, Vehiculo
```

| Clase | Responsabilidades | Colaboradores |
| ----- | ----------------- | ------------- |
| OrdenDeTrabajo | Identificar al vehiculo, mecánico e items de trabajo necesarios. | Vehiculo, Mecanico, ItemDeTrabajo. |
| ItemDeTrabajo | Resgistrar el identificador y costo de un item de trabajo. | OrdenDeTrabajo. |
| Vehiculo | Regisatrar las caracteristicas de un vehiculo en reparación. | OrdenDeTrabajo. |
| Mecanico | Registrar los datos de un mecánico del taller. | OrdenDeTrabajo, Taller.|
| Taller | Registrar los mecanicos asociados y las ordenes de trabajo aceptadas. | Mecanico, OrdenDeTrabajo. |

### Tabla de Relaciones

Completá esta tabla para cada relación entre clases que tu diseño tenga. La columna "por qué no es otro tipo" es la parte que más se evalúa: no alcanza con nombrar el tipo correcto, hay que argumentar por qué las otras tres opciones no aplican.

| Relación | Tipo | Justificación | Por qué no es otro tipo |
| -------- | ---- | ------------- | ----------------------- |
| `OrdenDeTrabajo` – `ItemDeTrabajo`  | Composición | No tiene sentido un item de trabajo sin una orden de trabajo ya que se pierde su proposito (Por ejemplo no tiene sentido cobrar por "mano de obra" si no trabajó en una orden de trabajo)|	Por qué no es agregación: Por que de eliminarse la `OrdenDeTrabajo` se perdería también el `ItemDeTrabajo` |
| `Taller` – `Mecanico` | Agregación | Los mecánicos se afilian a un taller para trabajar, a la vez que un taller necesita mecánicos para operar. | Por qué no es composición: Si se elimina un `Taller` un `Mecanico` asociado debería seguir existiendo y poder asociarse a otro taller |
| `OrdenDeTrabajo` – `Vehiculo` | Asociación |	La orden de trabajo debe poder conocer de que vehículo se encarga. | Por qué no es composición ni agregación: Un `Vehiculo` debería ser independiente de una `OrdenDeTrabajo`, si estas se eliminan debería ser capaz de iniciar nuevas mientras necesite reparaciones por lo que no podría ser una relación de composición. A su vez una `OrdenDeTrabajo` sin un `Vehiculo` asociado no tiene proposito, por lo que no podría tratarse de una agregación.
| Cálculo del presupuesto | Dependencia | Es un método que por definición depende de la información de cada ItemDeTrabajo | Por qué no es asociación: Sería sobreingeniería definir una clase "CalculoDePresupuesto" ya que no tendría otro proposito que llamar a un metodo que calcule el presupuesto, y el presupuesto es un dato asociado a una OrdenDeTrabajo. La información sobre los items de trabajo de una orden de trabajo se encuentra presisamente en la clase OrdenDeTrabajo, lo más eficiente sería agregár el método de calculo en la misma directamente.|