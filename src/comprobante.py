class Comprobante:

    def imprimir(
        self,
        origen,
        destino,
        monto,
        comision
    ):
        print(
            "===== BANCO ANDINO - COMPROBANTE ====="
        )
        print(
            "Origen: " + origen.get_numero()
        )
        print(
            "Destino: " + destino.get_numero()
        )
        print(
            "Monto: $" + str(monto)
        )
        print(
            "Comisión: $" + str(comision)
        )
        print(
            "======================================"
        )