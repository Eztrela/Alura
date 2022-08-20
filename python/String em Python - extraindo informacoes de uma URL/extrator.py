import re

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
    
    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ''
    
    def valida_url(self):
        if not self.url:
            raise ValueError('A URL esta vazia')
        
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError('A URL nao é valida')
    
    def get_url_base(self):
        indidce_interrogacao= self.url.find('?')
        url_base = self.url[:indidce_interrogacao]
        return url_base
    
    def get_url_parametro(self):
        indidce_interrogacao= self.url.find('?')
        url_parametros = self.url[indidce_interrogacao+1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametro().find('&',indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
        return valor
    
    def converte_moedas(self, dolar, quantidade, origem):
        if (origem == 'real'):
            return float(quantidade)/dolar
        else:
            return float(quantidade) * dolar
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url

    def __eq__(self,other):
        return self.url == other.url
    

url = 'bytebank.com/cambio?moedaDestino=real&quantidade=100&moedaOrigem=dolar'
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
print(extrator_url == extrator_url_2)
print("O tamanho da URL: ", len(extrator_url))
print(extrator_url)
VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
quantidade = extrator_url.get_valor_parametro("quantidade")
print(extrator_url.converte_moedas(VALOR_DOLAR, quantidade,moeda_origem))