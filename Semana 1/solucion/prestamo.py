
class Prestamo:

    def __init__(self, titulo, nombre_socio, dias_transcurridos):
            self.validar_prestamo(titulo, nombre_socio, dias_transcurridos)
            self.titulo = titulo
            self.nombre_socio = nombre_socio
            self.dias_transcurridos = dias_transcurridos

    def validar_prestamo(self, titulo, nombre_socio, dias_transcurridos):
        if ((not titulo) or (not nombre_socio) or (dias_transcurridos < 0)):
            raise ValueError("Los datos de creación del préstamo son inválidos.")

    def esta_vencido(self) :
        return self.dias_transcurridos > 7

    def dias_de_retraso(self) :
        if (not self.esta_vencido()):
            return 0
        return self.dias_transcurridos - 7

    def resumen(self) :
        if (not self.esta_vencido()):
            return (f"{self.titulo} — {self.nombre_socio} — en término")
        else:
            return (f"{self.titulo} — {self.nombre_socio} — vencido ({self.dias_de_retraso()} días)")