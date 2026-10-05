class OracleRepositorio:
    def guardar_transaccion(self, origen, destino, monto, comision):
        print(
            "[ORACLE] Conectando a "
            "jdbc:oracle:thin:@prod-db:1521/BANCO..."
        )

        print(
            "[ORACLE] INSERT INTO transacciones VALUES "
            f"('{origen}', '{destino}', {monto}, {comision})"
        )