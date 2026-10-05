from abc import ABC, abstractmethod


class GenerableExtracto(ABC):

    @abstractmethod
    def generar_extracto(self):
        pass