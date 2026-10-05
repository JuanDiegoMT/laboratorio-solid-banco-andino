class SmsGateway:
    def enviar(self, destinatario, mensaje):
        print("[SMS] Conectando al proveedor de mensajería...")
        print(f"[SMS] Para {destinatario}: {mensaje}")