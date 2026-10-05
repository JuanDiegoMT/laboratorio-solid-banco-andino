from oracle_repositorio import OracleRepositorio
from sms_gateway import SmsGateway

from validador_transaccion import ValidadorTransaccion
from calculador_comision import CalculadorComision
from comprobante import Comprobante
from auditoria import Auditoria


class TransaccionService:

    def __init__(self):
        self.repositorio = OracleRepositorio()
        self.sms = SmsGateway()

        self.validador = ValidadorTransaccion()
        self.calculador_comision = CalculadorComision()
        self.comprobante = Comprobante()
        self.auditoria = Auditoria()

    def transferir(
        self,
        origen,
        destino,
        monto,
        tipo
    ):

        self.validador.validar(monto)

        comision = self.calculador_comision.calcular(
            monto,
            tipo
        )

        origen.retirar(
            monto + comision
        )

        destino.depositar(
            monto
        )

        self.repositorio.guardar_transaccion(
            origen.get_numero(),
            destino.get_numero(),
            monto,
            comision
        )

        self.comprobante.imprimir(
            origen,
            destino,
            monto,
            comision
        )

        self.sms.enviar(
            origen.get_titular(),
            "Transferiste $"
            + str(monto)
            + " a la cuenta "
            + destino.get_numero()
        )

        self.auditoria.registrar(
            tipo,
            origen,
            destino,
            monto
        )