class PushGateway:

    def enviar(self, destinatario, mensaje):
        print(
            f"[PUSH] Para {destinatario}: {mensaje}"
        )