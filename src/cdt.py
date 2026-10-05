from cuenta import Cuenta


class CDT(Cuenta):
    def __init__(self, numero, titular, monto, vencimiento):
        super().__init__(numero, titular, monto)
        self._vencimiento = vencimiento
