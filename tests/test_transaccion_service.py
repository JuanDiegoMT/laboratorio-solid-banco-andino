from cuenta_ahorros import CuentaAhorros
from transaccion_service import TransaccionService
from validador_transaccion import ValidadorTransaccion
from calculador_comision import CalculadorComision


class RepositorioFalso:
    def __init__(self):
        self.transacciones = []

    def guardar_transaccion(
        self,
        origen,
        destino,
        monto,
        comision
    ):
        self.transacciones.append({
            "origen": origen,
            "destino": destino,
            "monto": monto,
            "comision": comision
        })


class SmsFalso:
    def __init__(self):
        self.mensajes = []

    def enviar(self, destinatario, mensaje):
        self.mensajes.append(
            (destinatario, mensaje)
        )


class ComprobanteFalso:
    def imprimir(
        self,
        origen,
        destino,
        monto,
        comision
    ):
        pass


class AuditoriaFalsa:
    def registrar(
        self,
        tipo,
        origen,
        destino,
        monto
    ):
        pass


def test_otro_banco_cobra_7500():

    repositorio = RepositorioFalso()
    sms = SmsFalso()

    servicio = TransaccionService(
        repositorio,
        sms,
        ValidadorTransaccion(),
        CalculadorComision(),
        ComprobanteFalso(),
        AuditoriaFalsa()
    )

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

    servicio.transferir(
        ana,
        luis,
        50_000,
        "OTRO_BANCO"
    )

    assert ana.get_saldo() == 942_500

    assert len(
        repositorio.transacciones
    ) == 1

    assert (
        repositorio.transacciones[0]["comision"]
        == 7_500
    )

    assert len(sms.mensajes) == 1