from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, id_conta: int, saldo: float, taxa_de_rendimento: float):
        super().__init__(id_conta, saldo)
        self._taxa_de_rendimento = taxa_de_rendimento
    
    def sacar(self, valor: float) -> None:
        if self._saldo < valor:
            raise ValueError('Saldo insuficiente')
        self._saldo -= valor
    
    def depositar(self, valor: float) -> None:
        self._saldo += valor
    
    def verificar_rendimento_ao_ano(self) -> float:
        return self._saldo * self._taxa_de_rendimento



