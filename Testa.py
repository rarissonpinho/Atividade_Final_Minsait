from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

# Teste para ContaCorrente
cc = ContaCorrente(1, 1000, 500)
print(f'Saldo inicial: {cc.get_saldo()}')
cc.sacar(200)
print(f'Saldo após saque: {cc.get_saldo()}')
cc.depositar(500)
print(f'Saldo após depósito: {cc.get_saldo()}')

# Teste para ContaPoupanca
cp = ContaPoupanca(2, 5000, 0.02)
print(f'Saldo inicial: {cp.get_saldo()}')
rendimento = cp.verificar_rendimento_ao_ano()
print(f'Rendimento ao ano: {rendimento}')
cp.depositar(rendimento)
print(f'Saldo após depósito do rendimento: {cp.get_saldo()}')




