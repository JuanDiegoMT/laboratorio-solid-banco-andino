from datetime import date
from dateutil.relativedelta import relativedelta

from cuenta_ahorros import CuentaAhorros
from cdt import CDT
from transaccion_service import TransaccionService
from cobro_cuota_manejo import CobroCuotaManejo
from tarjeta_credito import TarjetaCredito
from credito_vivienda import CreditoVivienda
from generador_extractos import GeneradorExtractos
from oracle_repositorio import OracleRepositorio
from sms_gateway import SmsGateway
from validador_transaccion import ValidadorTransaccion
from calculador_comision import CalculadorComision
from comprobante import Comprobante
from auditoria import Auditoria

def main():

    ana = CuentaAhorros(
        "001-1",
        "Ana",
        2_000_000
    )

    luis = CuentaAhorros(
        "001-2",
        "Luis",
        500_000
    )

    cdt_ana = CDT(
        "CDT-9",
        "Ana",
        10_000_000,
        date.today() + relativedelta(months=6)
    )

    servicio = TransaccionService(
        OracleRepositorio(),
        SmsGateway(),
        ValidadorTransaccion(),
        CalculadorComision(),
        Comprobante(),
        Auditoria()
    )

    servicio.transferir(
        ana,
        luis,
        150_000,
        "OTRO_BANCO"
    )

    CobroCuotaManejo().cobrar_mensual(
        [ana, luis]
    )

    productos = [
        ana,
        TarjetaCredito(3_000_000),
        CreditoVivienda(120_000_000)
    ]

    GeneradorExtractos().generar(productos)
    
if __name__ == "__main__":
    main()