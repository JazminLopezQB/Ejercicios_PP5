import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from solucion.prestamo import Prestamo


def test_prestamo_en_termino():
    prestamo = Prestamo("El Aleph", "Carlos", 5)
    assert not prestamo.esta_vencido()
    assert prestamo.resumen() == "El Aleph — Carlos — en término"


def test_prestamo_vencido():
    prestamo = Prestamo("Cien años de soledad", "Ana", 10)
    assert prestamo.esta_vencido()
    assert prestamo.dias_de_retraso() == 3
    assert prestamo.resumen() == "Cien años de soledad — Ana — vencido (3 días)"


def test_retraso_cero():
    prestamo = Prestamo("Ficciones", "Lucía", 7)
    assert not prestamo.esta_vencido()
    assert prestamo.dias_de_retraso() == 0


def test_dato_invalido():
    with pytest.raises(ValueError):
        Prestamo("Rayuela", "Diego", -5)