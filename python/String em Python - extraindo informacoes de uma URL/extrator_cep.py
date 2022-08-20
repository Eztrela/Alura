endereco = 'Rua edmundo Pereira de Assis 205, apartamento 307, Universitario, Campina Grande, PB, 58428-153'

import re

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')
busca = padrao.search(endereco)

if busca:
    cep = busca.group()
    print(cep)