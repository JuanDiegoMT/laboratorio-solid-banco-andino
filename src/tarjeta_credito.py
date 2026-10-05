from generable_extracto import GenerableExtracto
from calculable_intereses import CalculableIntereses
from pagable_cuota import PagableCuota


class TarjetaCredito(
    GenerableExtracto,
    CalculableIntereses,
    PagableCuota
):

    def __init__(self, cupo):
        self._deuda = 0
        self._cupo = cupo

    def retirar(self, monto):
        if self._deuda + monto > self._cupo:
            raise RuntimeError("Cupo insuficiente")

        self._deuda += monto

    def calcular_intereses(self):
        return self._deuda * 0.028

    def pagar_cuota(self, monto):
        self._deuda -= monto

    def generar_extracto(self):
        return f"Tarjeta - deuda: ${self._deuda}"