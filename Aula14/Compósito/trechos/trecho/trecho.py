from abc import ABC, abstractmethod


class Trecho(ABC):

    @abstractmethod
    def imprime(self):
        pass
