from datetime import date

from cuenta import CuentaConRetiro


class CuentaInfantil(CuentaConRetiro):
    """Cuenta con retiros acumulados limitados por día calendario."""

    TOPE_RETIROS_DIARIO = 200_000

    def __init__(self, numero, titular, saldo_inicial):
        super().__init__(numero, titular, saldo_inicial)
        self._fecha_retiros = date.today()
        self._retiros_hoy = 0

    def retirar(self, monto):
        if monto <= 0:
            raise ValueError("Monto inválido")

        hoy = date.today()
        if hoy != self._fecha_retiros:
            self._fecha_retiros = hoy
            self._retiros_hoy = 0

        if self._retiros_hoy + monto > self.TOPE_RETIROS_DIARIO:
            raise RuntimeError("Supera el tope de retiros diario")

        super().retirar(monto)
        self._retiros_hoy += monto
