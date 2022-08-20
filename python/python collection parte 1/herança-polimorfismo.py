from abc import ABCMeta, abstractclassmethod, abstractmethod

class conta(metaclass =  ABCMeta):
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita(self, valor):
        self._saldo += valor
    
    def __str__(self) -> str:
        return f'[>>Codigo {self._codigo} Saldo {self._saldo}<<]'

    @abstractmethod
    def passa_o_mes(self):
        pass

class ContaCorrente(conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupança(conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(conta):
    def passa_o_mes():
        pass

conta15 = ContaInvestimento(15)
conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta17 = ContaPoupança(17)
conta17.deposita(1000)



contas = [conta16, conta17]

for conta in contas:
    conta.passa_o_mes()
    print(conta)