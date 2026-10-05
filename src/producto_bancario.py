from abc import ABC, abstractmethod


class ProductoBancario(ABC):

    @abstractmethod
    def depositar(self, monto):
        pass

    @abstractmethod
    def retirar(self, monto):
        pass

    @abstractmethod
    def calcular_intereses(self):
        pass

    @abstractmethod
    def pagar_cuota(self, monto):
        pass

    @abstractmethod
    def generar_extracto(self):
        pass