from datetime import date

from cuenta import Cuenta


class CDT(Cuenta):
    def __init__(self, numero, titular, monto, vencimiento):
        super().__init__(numero, titular, monto)
        self._vencimiento = vencimiento

    def retirar(self, monto):
        if date.today() < self._vencimiento:
            raise RuntimeError(
                "Un CDT no permite retiros antes del vencimiento"
            )

        super().retirar(monto)