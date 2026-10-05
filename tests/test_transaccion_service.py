from cuenta_ahorros import CuentaAhorros
from transaccion_service import TransaccionService


def test_otro_banco_cobra_7500():

    ana = CuentaAhorros(
        "001-1",
        "Ana",
        1_000_000
    )

    luis = CuentaAhorros(
        "001-2",
        "Luis",
        0
    )

    servicio = TransaccionService()

    servicio.transferir(
        ana,
        luis,
        50_000,
        "OTRO_BANCO"
    )

    assert ana.get_saldo() == 942_500