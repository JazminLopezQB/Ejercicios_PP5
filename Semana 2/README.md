# Ejercicio de la Semana 2 de PP5

## Enunciado

Un taller mecánico recibe vehículos, arma una orden de trabajo por cada visita y le va agregando ítems de trabajo (mano de obra, repuestos) a medida que el mecánico revisa el auto. El taller tiene una plantilla de mecánicos disponibles, pero no todos están asignados a una orden en un momento dado.

Realizar:
- Análisis del Dominio
- Tarjetas CRC
- Código funcional

## Análisis del Dominio

### Conceptos del Enunciado

- Taller Mecánico
- Vehiculos
- Orden de trabajo
- Visita
- Items de trabajo
- Mano de obra
- Repuestos
- Mecánico
- Plantilla de Mecanicos disponibles

### Conceptos que No se Convierten en Clases

- **Visita**: No se convierte en clase ya que se ve representada por una orden de trabajo.
- **Mano de Obra**: No tiene una responsabilidad, puede abstraerse como un atributo de OrdenDeTrabajo.
- **Repuestos**: Idem a la mano de obra.
- **Plantilla de Mecanicos disponibles**: Es la relación entre los mecánicos y el taller, no una clase en sí al no tener comportamientos propios.

## Tarjetas CRC

| Clase | Responsabilidades | Colaboradores |
| ----- | ----------------- | ------------- |
| OrdenDeTrabajo | | |
| ItemDeTrabajo | | |
| Vehiculo | | |
| Mecanico | | |
| Taller | | |