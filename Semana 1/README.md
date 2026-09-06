# Problema 1: Préstamo de biblioteca

## Enunciado Práctico

Una biblioteca presta ejemplares por 7 días. Necesitamos representar un préstamo sin diccionarios ni funciones que calculen reglas por afuera.

Creá la clase Prestamo en solucion/prestamo.py. Al crearla recibe titulo, nombre_socio y dias_transcurridos. Un préstamo es válido solo si el título y el socio no están vacíos, y los días transcurridos no son negativos. Para datos inválidos, lanzá ValueError.

Su protocolo público debe ser:

```
prestamo = Prestamo("El principito", "Ana", 9)

assert prestamo.esta_vencido() is True
assert prestamo.dias_de_retraso() == 2
assert prestamo.resumen() == "El principito — Ana — vencido (2 días)"
```

- Reglas:
    - `esta_vencido()` devuelve `True` solo si pasaron más de 7 días.
    - `dias_de_retraso()` devuelve `0` si todavía está en término.
    - `resumen()` devuelve `"<título> — <socio> — en término"` o `"<título> — <socio> — vencido (<n> días)".`
    - El código que usa el préstamo no debe calcular si venció ni sus días de retraso leyendo atributos.

## Enunciado Teórico

- ¿Qué regla quedó dentro de Prestamo y qué problema habría si la calculara quien usa el objeto?
    - Prestamo sigue la regla del encapsulamiento.
    - Resguarda sus datos del entorno exterior y el código que implementa las instancias solo realiza llamados a sus métodos.
    - Si no se aplicara encapsulamiento alterar el comportamiento de Prestamo sería complejo al estar distribuido por todo el programa.