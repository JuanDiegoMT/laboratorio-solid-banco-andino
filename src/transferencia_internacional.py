from tipo_transferencia import TipoTransferencia


class TransferenciaInternacional(TipoTransferencia):
    nombre = "INTERNACIONAL"

    def calcular_comision(self, monto):
        return monto * 0.03 + 25_000
