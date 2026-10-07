from transferencia_internacional import TransferenciaInternacional
from transferencia_llave import TransferenciaLlave
from transferencia_mismo_banco import TransferenciaMismoBanco
from transferencia_otro_banco import TransferenciaOtroBanco


class CalculadorComision:
    """Delega el cálculo de comisión a la estrategia de transferencia."""

    def __init__(self, tipos=None):
        self.tipos = tipos or {
            estrategia.nombre: estrategia
            for estrategia in (
                TransferenciaMismoBanco(),
                TransferenciaOtroBanco(),
                TransferenciaInternacional(),
                TransferenciaLlave(),
            )
        }

    def calcular(self, monto, tipo):
        try:
            estrategia = self.tipos[tipo]
        except KeyError:
            raise ValueError("Tipo de transferencia desconocido") from None
        return estrategia.calcular_comision(monto)
