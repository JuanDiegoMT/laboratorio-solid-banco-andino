class CobroCuotaManejo:
    CUOTA = 12_900

    def cobrar_mensual(self, cuentas):
        for cuenta in cuentas:
            cuenta.retirar(self.CUOTA)

            print(
                f"Cuota de manejo cobrada a "
                f"{cuenta.get_numero()}"
            )