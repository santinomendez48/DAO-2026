import pytest

from individual import Individual
from familiar import Familiar
from gimnasio import Gimnasio


@pytest.fixture()
def gimnasio():
    g = Gimnasio()
    g.agregar(Individual(1, "SOFIA", 1, 200000, 3, False))
    g.agregar(Individual(2, "TOMAS", 3, 150000, 4, True))
    g.agregar(Familiar(3, "VALERIA", 5, 300000, 50000, 5))
    g.agregar(Familiar(4, "WALTER", 2, 250000, 40000, 2))
    return g


def test_cuota_individual_sin_personal_trainer():
    socio = Individual(1, "SOFIA", 1, 200000, 3, False)
    # 200000 + 3 * 30000
    assert socio.cuota() == 290000


def test_cuota_individual_con_personal_trainer():
    socio = Individual(2, "TOMAS", 3, 150000, 4, True)
    # 150000 + 4 * 30000 + 100000
    print(socio)
    assert socio.cuota() == 370000


def test_cuota_familiar_menos_de_cuatro_integrantes():
    socio = Familiar(4, "WALTER", 2, 250000, 40000, 2)
    # 250000 + 40000 + 20000
    assert socio.cuota() == 310000


def test_cuota_familiar_cuatro_integrantes_sin_extra():
    socio = Familiar(5, "XIMENA", 1, 180000, 30000, 4)
    # 180000 + 30000 (4 no es "menos de 4")
    assert socio.cuota() == 210000


def test_cuota_familiar_mas_de_cuatro_integrantes():
    socio = Familiar(6, "YAMIL", 4, 220000, 35000, 6)
    # 220000 + 35000
    assert socio.cuota() == 255000


def test_gimnasio_comienza_vacio():
    g = Gimnasio()
    assert g.suma_cuotas() == 0
    assert g.cantidad_socios_premium() == 0
    assert g.socio_cuota_mas_baja() is None


def test_agregar_socios(gimnasio):
    assert len(gimnasio.membresias) == 4


def test_suma_cuotas(gimnasio):
    # 290000 + 370000 + 350000 + 310000
    assert gimnasio.suma_cuotas() == 1320000


def test_cantidad_socios_premium(gimnasio):
    # solo TOMAS: más de 2 años, más de 3 clases grupales y personal trainer
    assert gimnasio.cantidad_socios_premium() == 1


def test_premium_no_cuenta_sin_personal_trainer():
    g = Gimnasio()
    g.agregar(Individual(1, "SOFIA", 5, 200000, 4, False))
    assert g.cantidad_socios_premium() == 0


def test_premium_no_cuenta_antiguedad_menor_o_igual_a_dos():
    g = Gimnasio()
    g.agregar(Individual(1, "ZOE", 2, 200000, 5, True))
    g.agregar(Individual(2, "ARIEL", 1, 200000, 5, True))
    assert g.cantidad_socios_premium() == 0


def test_premium_no_cuenta_tres_clases_o_menos():
    g = Gimnasio()
    g.agregar(Individual(1, "BRUNO", 5, 200000, 3, True))
    assert g.cantidad_socios_premium() == 0


def test_premium_no_cuenta_familiares():
    g = Gimnasio()
    familiar = Familiar(1, "CAMILA", 5, 200000, 30000, 2)
    g.agregar(familiar)
    assert g.cantidad_socios_premium() == 0


def test_socio_cuota_mas_baja(gimnasio):
    # el familiar de WALTER (310000) es el más barato
    assert gimnasio.socio_cuota_mas_baja() == "WALTER"


def test_socio_mas_bajo_considera_solo_familiares():
    g = Gimnasio()
    g.agregar(Individual(1, "UN SOCIO BARATO", 1, 50000, 1, False))
    g.agregar(Familiar(2, "EL FAMILIAR MAS CARO", 5, 900000, 100000, 5))
    assert g.socio_cuota_mas_baja() == "EL FAMILIAR MAS CARO"


def test_socio_mas_bajo_sin_familiares():
    g = Gimnasio()
    g.agregar(Individual(1, "DELFINA", 1, 200000, 3, False))
    assert g.socio_cuota_mas_baja() is None
