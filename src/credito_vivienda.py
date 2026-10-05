from producto_bancario import ProductoBancario


class CreditoVivienda(ProductoBancario):
    def __init__(self, valor_prestamo):
        self._saldo_pendiente = valor_prestamo

    def depositar(self, monto):
        pass

    def retirar(self, monto):
        pass

    def calcular_intereses(self):
        return self._saldo_pendiente * 0.011

    def pagar_cuota(self, monto):
        self._saldo_pendiente -= monto

    def generar_extracto(self):
        return (
            f"Crédito vivienda - pendiente: "
            f"${self._saldo_pendiente}"
        )