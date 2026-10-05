from abc import ABC, abstractmethod


class TipoTransferencia(ABC):
    nombre: str

    @abstractmethod
    def calcular_comision(self, monto):
        """Calcula la comisión correspondiente a esta modalidad."""
        raise NotImplementedError
