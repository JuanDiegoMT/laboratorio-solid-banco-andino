from tipo_transferencia import TipoTransferencia


class TransferenciaMismoBanco(TipoTransferencia):
    nombre = "MISMO_BANCO"

    def calcular_comision(self, monto):
        return 0
