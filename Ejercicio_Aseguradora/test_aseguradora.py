import pytest

from auto import Auto
from hogar import Hogar
from aseguradora import Aseguradora


@pytest.fixture()
def aseguradora():
    a = Aseguradora()
    a.agregar(Auto(1, "NADIA", 5, 100000, 5, False))
    a.agregar(Auto(2, "OSCAR", 0, 120000, 1, True))
    a.agregar(Hogar(3, "PAULA", 3, 90000, 150, False))
    a.agregar(Hogar(4, "QUIQUE", 2, 80000, 90, True))
    return a


def test_prima_auto_sin_recargos():
    auto = Auto(1, "NADIA", 5, 100000, 5, False)
    # vehiculo viejo, gama baja: sin recargos
    assert auto.prima() == 100000


def test_prima_auto_vehiculo_nuevo():
    auto = Auto(2, "RAMIRO", 5, 100000, 1, False)
    # 100000 + 80000
    assert auto.prima() == 180000


def test_prima_auto_gama_alta():
    auto = Auto(3, "SILVIA", 5, 100000, 5, True)
    # 100000 + 150000
    assert auto.prima() == 250000


def test_prima_auto_nuevo_y_gama_alta():
    auto = Auto(2, "OSCAR", 0, 120000, 1, True)
    # 120000 + 80000 + 150000
    assert auto.prima() == 350000


def test_prima_hogar_grande_sin_alarma():
    hogar = Hogar(3, "PAULA", 3, 90000, 150, False)
    # 90000 + 60000
    assert hogar.prima() == 150000


def test_prima_hogar_chica_con_alarma():
    hogar = Hogar(4, "QUIQUE", 2, 80000, 90, True)
    # 80000 - 40000
    assert hogar.prima() == 40000


def test_prima_hogar_grande_con_alarma():
    hogar = Hogar(5, "TOMAS", 1, 100000, 200, True)
    # 100000 + 60000 - 40000
    assert hogar.prima() == 120000


def test_prima_hogar_chica_sin_alarma():
    hogar = Hogar(6, "URSULA", 1, 70000, 80, False)
    # sin recargos ni descuentos
    assert hogar.prima() == 70000


def test_aseguradora_comienza_vacia():
    a = Aseguradora()
    assert a.prima_total() == 0
    assert a.cantidad_polizas_riesgo() == 0
    assert a.promedio_primas_hogar() is None
    assert a.asegurado_prima_mas_alta() is None


def test_agregar_polizas(aseguradora):
    assert len(aseguradora.polizas) == 4


def test_prima_total(aseguradora):
    # 100000 + 350000 + 150000 + 40000
    assert aseguradora.prima_total() == 640000


def test_cantidad_polizas_riesgo(aseguradora):
    # solo OSCAR: vehiculo < 3 años, gama alta y cliente con < 1 año
    assert aseguradora.cantidad_polizas_riesgo() == 1


def test_riesgo_no_cuenta_vehiculo_viejo():
    a = Aseguradora()
    a.agregar(Auto(1, "RAMIRO", 0, 100000, 5, True))
    assert a.cantidad_polizas_riesgo() == 0


def test_riesgo_no_cuenta_gama_baja():
    a = Aseguradora()
    a.agregar(Auto(1, "SILVIA", 0, 100000, 1, False))
    assert a.cantidad_polizas_riesgo() == 0


def test_riesgo_no_cuenta_cliente_antiguo():
    a = Aseguradora()
    a.agregar(Auto(1, "VICTOR", 5, 100000, 1, True))
    assert a.cantidad_polizas_riesgo() == 0


def test_riesgo_no_cuenta_hogares():
    a = Aseguradora()
    a.agregar(Hogar(1, "URSULA", 0, 100000, 200, True))
    assert a.cantidad_polizas_riesgo() == 0


def test_promedio_primas_hogar(aseguradora):
    # (150000 + 40000) / 2
    assert aseguradora.promedio_primas_hogar() == 95000.0


def test_promedio_primas_hogar_sin_hogares():
    a = Aseguradora()
    a.agregar(Auto(1, "WALTER", 5, 100000, 5, False))
    assert a.promedio_primas_hogar() is None


def test_asegurado_prima_mas_alta(aseguradora):
    # OSCAR (350000) supera a los demas
    assert aseguradora.asegurado_prima_mas_alta() == "OSCAR"


def test_prima_mas_alta_considera_ambos_tipos():
    a = Aseguradora()
    a.agregar(Auto(1, "BARATO", 5, 10000, 5, False))
    a.agregar(Hogar(2, "CARO", 5, 500000, 200, False))
    # el hogar de CARO (560000) supera al auto
    assert a.asegurado_prima_mas_alta() == "CARO"
