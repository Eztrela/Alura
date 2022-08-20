from datetime import datetime, timedelta
from datas_br import datasBr
from acesso_cep import buscaEndereco
import requests

#r = requests.get('https://viacep.com.br/ws/01001000/json/')
#print(r.text)

cep = 58428153
objeto_cep = buscaEndereco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep()
print(bairro, cidade, uf)

'''
print(objeto_cep)

hoje = datasBr()
print(hoje.tempo_cadastro())

cadastro = datasBr()
print(cadastro)

#hoje =  datetime.today()
#hoje_formatado = hoje.strftime('%d/%m/%Y %H:%M')
#print(hoje)
#print(hoje_formatado)


from telefonesBr import telefonesBr
import re


from validate_docbr import CNPJ
#from cpf import cpf


#cpf = 15616987913

#objeto_cpf = Cpf(cpf)
#print(objeto_cpf)

#cpf_um = cpf("15316264754")
#print(cpf_um)

exemplo_cnpj = "35379838000112"
cnpj = CNPJ()
print(cnpj.validate(exemplo_cnpj))


padrao = '[0-9]{2}[0-9]{4,5}[0-9]{4}'
texto = ''
resposta = re.search(padrao,texto)
print(resposta.group())


telefone = ' 552126481234'
objeto_telefone = telefonesBr(telefone)

print(objeto_telefone)
'''