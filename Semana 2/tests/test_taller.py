import os
import sys
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solucion.taller import Taller, OrdenDeTrabajo, ItemDeTrabajo, Vehiculo, Mecanico

@pytest.fixture
def taller():
    return Taller("Taller Central")

@pytest.fixture
def mecanico():
    return Mecanico("Juan Pérez", 101)

@pytest.fixture
def vehiculo1():
    return Vehiculo("AB123CD", "Carlos")

@pytest.fixture
def vehiculo2():
    return Vehiculo("XY987ZW", "Ana")

@pytest.fixture
def item_pastillas():
    return ItemDeTrabajo("Cambio de pastillas", 8000)

@pytest.fixture
def item_alineacion():
    return ItemDeTrabajo("Alineación y balanceo", 5000)

@pytest.fixture
def item_aceite():
    return ItemDeTrabajo("Cambio de aceite", 10000)

@pytest.fixture
def orden_con_item(vehiculo1, item_aceite):
    orden = OrdenDeTrabajo(1, vehiculo1, None)
    orden.agregar_item(item_aceite)
    return orden, item_aceite

def test_camino_feliz(taller, mecanico, vehiculo1, item_pastillas, item_alineacion):
    taller.contratar_mecanico(mecanico)
    orden = OrdenDeTrabajo(1, vehiculo1, None)
    taller.asociar_orden(orden)
    orden.asignar_mecanico(mecanico)
    
    orden.agregar_item(item_pastillas)
    orden.agregar_item(item_alineacion)
    
    assert orden.presupuesto() == 13000
    assert orden.mecanico == mecanico
    assert item_pastillas.orden == orden
    assert item_alineacion.orden == orden


def test_rechazo_por_item_duplicado(orden_con_item, vehiculo2):
    orden1, item_aceite = orden_con_item
    orden2 = OrdenDeTrabajo(2, vehiculo2, None)
    
    with pytest.raises(ValueError):
        orden2.agregar_item(item_aceite)


def test_estado_luego_de_rechazo(orden_con_item, vehiculo2):
    orden1, item_aceite = orden_con_item
    orden2 = OrdenDeTrabajo(2, vehiculo2, None)
    
    with pytest.raises(ValueError):
        orden2.agregar_item(item_aceite)
    
    assert item_aceite not in orden2.lista_items
    assert len(orden2.lista_items) == 0
    assert item_aceite.orden == orden1
    assert orden1.presupuesto() == 10000
    assert orden2.presupuesto() == 0


def test_rechazo_vehiculo_con_orden_activa(vehiculo1):
    _orden1 = OrdenDeTrabajo(1, vehiculo1, None)
    
    with pytest.raises(ValueError):
        OrdenDeTrabajo(2, vehiculo1, None)