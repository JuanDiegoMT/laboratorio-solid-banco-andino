from generable_extracto import GenerableExtracto


class Cuenta(GenerableExtracto):

    def __init__(
        self,
        numero,
        titular,
        saldo_inicial
    ):
        self._numero = numero
        self._titular = titular
        self._saldo = saldo_inicial

    def get_numero(self):
        return self._numero

    def get_titular(self):
        return self._titular

    def get_saldo(self):
        return self._saldo

    def depositar(self, monto):
        if monto <= 0:
            raise ValueError("Monto inválido")

        self._saldo += monto

    def retirar(self, monto):
        if monto > self._saldo:
            raise RuntimeError("Saldo insuficiente")

        self._saldo -= monto

    def generar_extracto(self):
        return (
            "Cuenta "
            + self._numero
            + " - saldo: $"
            + str(self._saldo)
        )

class CuentaConRetiro(Cuenta):
    """Cuenta con saldo disponible para retiros inmediatos."""

    def retirar(self, monto):
        if monto > self._saldo:
            raise RuntimeError("Saldo insuficiente")

        self._saldo -= monto
