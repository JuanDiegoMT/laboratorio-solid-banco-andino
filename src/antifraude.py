class Antifraude:

    def registrar(
        self,
        tipo,
        origen,
        destino,
        monto
    ):
        print(
            "[ANTIFRAUDE] "
            + tipo
            + " "
            + origen.get_numero()
            + " -> "
            + destino.get_numero()
            + " $"
            + str(monto)
        )