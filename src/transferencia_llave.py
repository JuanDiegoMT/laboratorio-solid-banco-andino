from tipo_transferencia import TipoTransferencia


class TransferenciaLlave(TipoTransferencia):
    """Transferencia inmediata identificada por celular o cédula."""

    nombre = "LLAVE"

    def calcular_comision(self, monto):
        return 0
