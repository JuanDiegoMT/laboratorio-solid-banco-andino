from generable_extracto import GenerableExtracto
from calculable_intereses import CalculableIntereses
from pagable_cuota import PagableCuota


class CreditoVivienda(
    GenerableExtracto,
    CalculableIntereses,
    PagableCuota
):

    def __init__(self, valor_prestamo):
        self._saldo_pendiente = valor_prestamo

    def calcular_intereses(self):
        return self._saldo_pendiente * 0.011

    def pagar_cuota(self, monto):
        self._saldo_pendiente -= monto

    def generar_extracto(self):
        return (
            "Crédito vivienda - pendiente: $"
            + str(self._saldo_pendiente)
        )