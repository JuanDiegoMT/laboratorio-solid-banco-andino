from cuenta import Cuenta


class CuentaAhorros(Cuenta):
    def __init__(self, numero, titular, saldo_inicial):
        super().__init__(numero, titular, saldo_inicial)