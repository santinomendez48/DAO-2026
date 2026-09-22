import pytest

from estandar import Estandar
from express import Express
from transportadora import Transportadora


@pytest.fixture()
def transportadora():
    t = Transportadora()
    t.agregar(Estandar(1, "ANDREA", 10, 50000, 15, False))
    t.agregar(Estandar(2, "BRUNO", 5, 40000, 25, True))
    t.agregar(Express(3, "CARLA", 80, 60000, 2, 10000))
    t.agregar(Express(4, "DIEGO", 30, 55000, 6, 5000))
    return t


def test_importe_estandar_sin_recargos():
    envio = Estandar(1, "ANDREA", 10, 50000, 15, False)
    # peso <= 20 y no fragil: sin recargos
    assert envio.importe() == 50000


def test_importe_estandar_peso_excede_veinte():
    envio = Estandar(2, "ELISA", 5, 40000, 30, False)
    # 40000 + (30 - 20) * 5000
    assert envio.importe() == 90000


def test_importe_estandar_fragil_sin_exceso_de_peso():
    envio = Estandar(3, "FACUNDO", 5, 40000, 10, True)
    # 40000 + 8000
    assert envio.importe() == 48000


def test_importe_estandar_fragil_y_excede_peso():
    envio = Estandar(4, "BRUNO", 5, 40000, 25, True)
    # 40000 + (25 - 20) * 5000 + 8000
    assert envio.importe() == 73000


def test_importe_express_sin_recargo_de_urgencia():
    envio = Express(5, "GABRIELA", 20, 60000, 4, 5000)
    # 4 horas no es "menos de 4": sin recargo, solo se suma el seguro
    assert envio.importe() == 65000


def test_importe_express_con_recargo_de_urgencia():
    envio = Express(3, "CARLA", 80, 60000, 2, 10000)
    # 60000 + 15000 + 10000
    assert envio.importe() == 85000


def test_transportadora_comienza_vacia():
    t = Transportadora()
    assert t.importe_total() == 0
    assert t.cantidad_envios_prioritarios() == 0
    assert t.promedio_importe_estandar() is None
    assert t.cliente_envio_mas_barato() is None


def test_agregar_envios(transportadora):
    assert len(transportadora.envios) == 4


def test_importe_total(transportadora):
    # 50000 + 73000 + 85000 + 60000
    assert transportadora.importe_total() == 268000


def test_cantidad_envios_prioritarios(transportadora):
    # solo CARLA: urgencia < 4 horas y distancia > 50 km
    assert transportadora.cantidad_envios_prioritarios() == 1


def test_prioritarios_no_cuenta_urgencia_mayor_o_igual_a_cuatro():
    t = Transportadora()
    t.agregar(Express(1, "HERNAN", 100, 50000, 4, 5000))
    assert t.cantidad_envios_prioritarios() == 0


def test_prioritarios_no_cuenta_distancia_menor_o_igual_a_cincuenta():
    t = Transportadora()
    t.agregar(Express(1, "IVANA", 50, 50000, 2, 5000))
    assert t.cantidad_envios_prioritarios() == 0


def test_prioritarios_no_cuenta_estandar():
    t = Transportadora()
    t.agregar(Estandar(1, "JULIAN", 100, 50000, 30, True))
    assert t.cantidad_envios_prioritarios() == 0


def test_promedio_importe_estandar(transportadora):
    # (50000 + 73000) / 2
    assert transportadora.promedio_importe_estandar() == 61500.0


def test_promedio_importe_estandar_sin_estandar():
    t = Transportadora()
    t.agregar(Express(1, "KARINA", 20, 50000, 6, 5000))
    assert t.promedio_importe_estandar() is None


def test_cliente_envio_mas_barato(transportadora):
    # ANDREA (50000) es el mas barato
    assert transportadora.cliente_envio_mas_barato() == "ANDREA"


def test_envio_mas_barato_considera_ambos_tipos():
    t = Transportadora()
    t.agregar(Estandar(1, "UN ENVIO CARO", 5, 300000, 40, True))
    t.agregar(Express(2, "EL ENVIO MAS BARATO", 5, 10000, 10, 0))
    assert t.cliente_envio_mas_barato() == "EL ENVIO MAS BARATO"
