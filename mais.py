url = "https://bytebank.com/cambio?moeda0rigem=real"
print(url)

indice_interrogação= url.find('?')
url_base = url[0:19]
print(url_base)

url_parametros = url[20:36]
print(url_parametros)

parametro_busca = 'moeda)rigem'
indice_parametro = url_paramentros.find(parametro_busca)

print(indice_parametro)

indice_valor = indice_parametro + indice_tamanho + 1
valor = url_parametro[indice_valor:]

print(valor)
