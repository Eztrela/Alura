from functools import total_ordering

@total_ordering
class contaSalario():
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, outro):
        if type(outro) != contaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self, outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo <  outro._codigo
    
    def deposita(self, valor):
        self._saldo += valor
    
    def __str__(self) -> str:
        return f'[>>Codigo {self._codigo} Saldo {self._saldo}<<]'


class ContaMultiploSalario(contaSalario):
    pass
conta1 = contaSalario(37)
conta2 = contaSalario(37)

print(conta1 == conta2)

print(conta1 in [conta2])

print(isinstance(contaSalario(34), contaSalario))

conta_do_guilherme = contaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = contaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = contaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]

print(conta_do_guilherme <= conta_do_guilherme)

for conta in sorted(contas):
    print(conta)

for conta in sorted(contas,reverse=True):
    print(conta)