#url = "https://bytebank.com/cambio?moeda0rigem=real"
url = ""

# Sanitização da url
url = url.replace("","")

# Validação da url
if url =="":
    raise ValueError("A url etá vazia")

# Separa base e parametros
indice_interrogação= url.find('?')
url_base = url[0:19]
print(url_base)
url_parametros = url[20:36]
print(url_parametros)

# Busca o valor de um paramero
parametro_busca = 'mquantidade'
indice_parametro = url_paramentros.find(parametro_busca)
indice_valor = indice_parametro + indice_tamanho + 1
indice_e_comercial = url_parametros.find('&')
if indice_e_comercial ==-1:
    valor = url_parametro[indice_valor:]
else:
   valor= url_parametro[indice_valor:indice_e_comercial]

print(valor)
