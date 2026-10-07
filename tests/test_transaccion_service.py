import pytest

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

    def __init__(self):
        self.comprobantes = []

    def imprimir(
        self,
        origen,
        destino,
        monto,
        comision
    ):
        self.comprobantes.append({
            "origen": origen.get_numero(),
            "destino": destino.get_numero(),
            "monto": monto,
            "comision": comision
        })


class AuditoriaFalsa:

    def __init__(self):
        self.registros = []

    def registrar(
        self,
        tipo,
        origen,
        destino,
        monto
    ):
        self.registros.append({
            "tipo": tipo,
            "origen": origen.get_numero(),
            "destino": destino.get_numero(),
            "monto": monto
        })


def crear_servicio_prueba():

    repositorio = RepositorioFalso()
    sms = SmsFalso()
    comprobante = ComprobanteFalso()
    auditoria = AuditoriaFalsa()

    servicio = TransaccionService(
        repositorio,
        [sms],
        ValidadorTransaccion(),
        CalculadorComision(),
        comprobante,
        auditoria
    )

    return (
        servicio,
        repositorio,
        sms,
        comprobante,
        auditoria
    )
# PRUEBA 1
def test_mismo_banco_no_cobra_comision_y_mueve_monto():

    servicio, repositorio, _, _, _ = (
        crear_servicio_prueba()
    )

    ana = CuentaAhorros(
        "001-1",
        "Ana",
        1_000_000
    )

    luis = CuentaAhorros(
        "001-2",
        "Luis",
        100_000
    )

    servicio.transferir(
        ana,
        luis,
        50_000,
        "MISMO_BANCO"
    )

    assert ana.get_saldo() == 950_000
    assert luis.get_saldo() == 150_000

    assert (
        repositorio.transacciones[0]["comision"]
        == 0
    )

# PRUEBA 2

def test_otro_banco_cobra_7500():

    servicio, repositorio, _, _, _ = (
        crear_servicio_prueba()
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
    assert luis.get_saldo() == 50_000

    assert (
        repositorio.transacciones[0]["comision"]
        == 7_500
    )
# PRUEBA 3

def test_saldo_insuficiente_no_guarda_ni_notifica():

    servicio, repositorio, sms, comprobante, auditoria = (
        crear_servicio_prueba()
    )

    ana = CuentaAhorros(
        "001-1",
        "Ana",
        10_000
    )

    luis = CuentaAhorros(
        "001-2",
        "Luis",
        0
    )

    with pytest.raises(RuntimeError):
        servicio.transferir(
            ana,
            luis,
            50_000,
            "MISMO_BANCO"
        )

    assert len(repositorio.transacciones) == 0
    assert len(sms.mensajes) == 0
    assert len(comprobante.comprobantes) == 0
    assert len(auditoria.registros) == 0

    assert ana.get_saldo() == 10_000
    assert luis.get_saldo() == 0
# PRUEBA 4

def test_transferencia_exitosa_guarda_y_notifica_una_vez():

    servicio, repositorio, sms, _, _ = (
        crear_servicio_prueba()
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
        "MISMO_BANCO"
    )

    assert len(repositorio.transacciones) == 1
    assert len(sms.mensajes) == 1
# PRUEBA 5

def test_tipo_desconocido_no_cambia_saldo():

    servicio, repositorio, sms, _, _ = (
        crear_servicio_prueba()
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

    saldo_inicial_ana = ana.get_saldo()
    saldo_inicial_luis = luis.get_saldo()

    with pytest.raises(ValueError):
        servicio.transferir(
            ana,
            luis,
            50_000,
            "TIPO_INEXISTENTE"
        )

    assert ana.get_saldo() == saldo_inicial_ana
    assert luis.get_saldo() == saldo_inicial_luis

    assert len(repositorio.transacciones) == 0
    assert len(sms.mensajes) == 0