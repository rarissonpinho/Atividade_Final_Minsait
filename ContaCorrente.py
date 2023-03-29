from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, id_conta: int, saldo: float, limite: float):
        super().__init__(id_conta, saldo)
        self._limite = limite
    
    def sacar(self, valor: float) -> None:
        if self._saldo + self._limite < valor:
            raise ValueError('Saldo insuficiente')
        self._saldo -= valor
    
    def depositar(self, valor: float) -> None:
        self._saldo += valor

