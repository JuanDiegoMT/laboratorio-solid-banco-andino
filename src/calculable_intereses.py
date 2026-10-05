from abc import ABC, abstractmethod


class CalculableIntereses(ABC):

    @abstractmethod
    def calcular_intereses(self):
        pass