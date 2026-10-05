from datetime import datetime


class Auditoria:

    def registrar(
        self,
        tipo,
        origen,
        destino,
        monto
    ):
        print(
            "[AUDITORIA] "
            + str(datetime.now())
            + " "
            + tipo
            + " "
            + origen.get_numero()
            + " -> "
            + destino.get_numero()
            + " $"
            + str(monto)
        )