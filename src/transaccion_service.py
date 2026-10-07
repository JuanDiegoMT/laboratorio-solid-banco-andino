class TransaccionService:

    def __init__(
        self,
        repositorio,
        notificadores,
        validador,
        calculador_comision,
        comprobante,
        auditoria
    ):
        self.repositorio = repositorio
        self.notificadores = notificadores
        self.validador = validador
        self.calculador_comision = calculador_comision
        self.comprobante = comprobante
        self.auditoria = auditoria

    def transferir(
        self,
        origen,
        destino,
        monto,
        tipo
    ):

        self.validador.validar(monto)

        comision = self.calculador_comision.calcular(
            monto,
            tipo
        )

        origen.retirar(
            monto + comision
        )

        destino.depositar(
            monto
        )

        self.repositorio.guardar_transaccion(
            origen.get_numero(),
            destino.get_numero(),
            monto,
            comision
        )

        self.comprobante.imprimir(
            origen,
            destino,
            monto,
            comision
        )

        mensaje = (
            "Transferiste $"
            + str(monto)
            + " a la cuenta "
            + destino.get_numero()
        )

        for notificador in self.notificadores:
            notificador.enviar(
                origen.get_titular(),
                mensaje
            )

        self.auditoria.registrar(
            tipo,
            origen,
            destino,
            monto
        )