from cuenta import CuentaConRetiro


class CuentaAhorros(CuentaConRetiro):
    def __init__(self, numero, titular, saldo_inicial):
        super().__init__(numero, titular, saldo_inicial)
