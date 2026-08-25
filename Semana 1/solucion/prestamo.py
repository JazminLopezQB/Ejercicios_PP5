
"""
¿Qué regla quedó dentro de Prestamo y qué problema habría si la calculara quien usa el objeto?
Prestamo sigue la regla del encapsulamiento.
Resguarda sus datos del entorno exterior y el código que implementa las instancias solo realiza llamados
a sus métodos.
Si no se aplicara encapsulamiento
"""
class Prestamo:

    def __init__(self, titulo, nombre_socio, dias_transcurridos):
            self.validar_prestamo(titulo, nombre_socio, dias_transcurridos)
            self.titulo = titulo
            self.nombre_socio = nombre_socio
            self.dias_transcurridos = dias_transcurridos

    def validar_prestamo(self, titulo, nombre_socio, dias_transcurridos):
        if titulo != None and nombre_socio != None and dias_transcurridos >= 0:
            return titulo
        else:
            raise ValueError("Los datos de creacion del prestamo son invalidos.")

    def esta_vencido(self) :
        if (self.dias_transcurridos > 7):
            return True
        return False

    def dias_de_retraso(self) :
        return self.dias_transcurridos - 7

    def resumen(self) :
        if (not self.esta_vencido()):
            return (f"{self.titulo} — {self.nombre_socio} — en término")
        else:
            return (f"{self.titulo} — {self.nombre_socio} — vencido ({self.dias_de_retraso()} días)")