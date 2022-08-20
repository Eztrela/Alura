

url = 'bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real'

#Sanitizacao da URL
url = url.strip(' ')

#validacao da URL
if url == '':
    raise ValueError("A URL esta vazia")

#Separa base e os parametros
indidce_interrogacao= url.find('?')
url_base = url[:indidce_interrogacao]
url_parametros = url[indidce_interrogacao+1:]
print(url_parametros)


#Busca o valor de um parametro
parametro_busca = 'quantidade'
indice_parametro = url_parametros.find(parametro_busca)
indice_valor = indice_parametro + len(parametro_busca) + 1
indice_e_comercial = url_parametros.find('&',indice_valor)
if indice_e_comercial == -1:
    valor = url_parametros[indice_valor:]
else:
    valor = url_parametros[indice_valor:indice_e_comercial]
print(valor)
