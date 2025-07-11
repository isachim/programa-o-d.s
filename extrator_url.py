import re

class ExtratorURL:
   def __init__(self,url):
       self.url = self.sanitiza_url(url)
       self.valida_url()

def sanitiza_url(self, url):
    return url.strip()

def valida_url(self):
    if self.url =="":
       raise ValueError("A URL está vazia")

   padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
   match = padrao_url.match(url)
if not match:
   raise ValueError("a url não é valida.")

def get_url_base(self):
    indice_interrogacao = self.url.find('?')
    url_base = self.url[:indice_interrogacao]

def get_url_parametros(self):
    indice_interrogacao = self.url.find('?')
    url_parametros = self.url[:indice_interrogacao]

def get_valor_parametro(self, nome_parametro):
    parametro_busca = 'quantidade'
    indice_parametro = url_parametro.find(parametro_busca)
    indice_valor = indice_parametro + len(parametro_busca) + 1
    indice_e_comercial = url_parametros.find('&' indice_valor)
    if indice_e_comercial == -1:
       valor = url_parametros[indice_valor:]
    else:
       valor = url_parametros[indice_valor:indice_e_comercial]

def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url



url = "bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
# print("O tamanho da URL: ", len(extrator_url))
# print(extrator_url)

print(extrator_url == etrator_url_2)

# valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)


