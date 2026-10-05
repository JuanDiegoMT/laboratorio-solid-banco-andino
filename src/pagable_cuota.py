from abc import ABC, abstractmethod


class PagableCuota(ABC):

    @abstractmethod
    def pagar_cuota(self, monto):
        pass