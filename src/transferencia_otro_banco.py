from tipo_transferencia import TipoTransferencia


class TransferenciaOtroBanco(TipoTransferencia):
    nombre = "OTRO_BANCO"

    def calcular_comision(self, monto):
        return 7_500
