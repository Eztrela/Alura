from tkinter.filedialog import SaveFileDialog


class contaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor
    
    def __str__(self) -> str:
        return f'[>>Codigo {self.codigo} Saldo {self.saldo}<<]'
    
conta_do_pablo = contaCorrente(15)
print(conta_do_pablo)
conta_do_pablo.deposita(500)
print(conta_do_pablo)
conta_da_dani = contaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

contas = [conta_do_pablo, conta_da_dani, conta_do_pablo]
for conta in contas:
    print(conta)
