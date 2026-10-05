class CalculadorComision:

    def calcular(self, monto, tipo):

        if tipo == "MISMO_BANCO":
            return 0

        if tipo == "OTRO_BANCO":
            return 7_500

        if tipo == "INTERNACIONAL":
            return monto * 0.03 + 25_000

        raise ValueError(
            "Tipo de transferencia desconocido"
        )