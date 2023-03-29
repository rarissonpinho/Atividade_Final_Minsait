from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, id_conta: int, saldo: float):
        self._id_conta = id_conta
        self._saldo = saldo
        
    @abstractmethod
    def sacar(self, valor: float) -> None:
        pass
    
    @abstractmethod
    def depositar(self, valor: float) -> None:
        pass

    def get_saldo(self):
        return self._saldo

    def set_saldo(self, value):
        if value <= 0:
            raise ValueError('Saldo insuficiente')
        else:
            self._saldo = value
