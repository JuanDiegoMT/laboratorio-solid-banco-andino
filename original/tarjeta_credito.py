from producto_bancario import ProductoBancario


class TarjetaCredito(ProductoBancario):
    def __init__(self, cupo):
        self._deuda = 0
        self._cupo = cupo

    def depositar(self, monto):
        pass

    def retirar(self, monto):
        # Avance en efectivo
        if self._deuda + monto > self._cupo:
            raise RuntimeError("Cupo insuficiente")

        self._deuda += monto

    def calcular_intereses(self):
        return self._deuda * 0.028

    def pagar_cuota(self, monto):
        self._deuda -= monto

    def generar_extracto(self):
        return f"Tarjeta - deuda: ${self._deuda}"