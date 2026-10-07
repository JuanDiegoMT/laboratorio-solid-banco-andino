class PostgresRepositorio:

    def guardar_transaccion(
        self,
        origen,
        destino,
        monto,
        comision
    ):
        print(
            "[POSTGRES] Conectando a "
            "postgresql://prod-db/BANCO..."
        )

        print(
            "[POSTGRES] INSERT INTO transacciones VALUES "
            f"('{origen}', '{destino}', {monto}, {comision})"
        )