idades.append(15)
idades
[39,30,27,18,15]

for idade in idades: 
  print(idade)

idades.remove(30)
idades
[39,27,18,15]

idades.append(27)
idades.remove(27)
idades
[39,18,15,27]

if 15 in idades:
  idades.remove(15)

for elemento in idades: 
  print("Recebi o elemento", elemento)

Recebi o elemento 20 
Recebi o elemento 39
Recebi o elemento 18
Recebi o elemento [27, 19]

idades_no_ano_que_vem = []
for idade in idades:
  idades_no_ano_que_vem.append(idade+1)


[(idade) for idade in idades if idade > 21]

def proximo ano(idade):
  return idade+1

[proximo_ano(idade) for idade in idades if idade > 21]

def faz_processamento_de_visualizacao(lista):
  print(len(lista))
    lista.append(13)

idades = [16, 21, 29, 56, 43]
faz_processamento_de_visualizacao(idades)

idades =====v
     [16, 21, 29, 56, 43]

def faz_processamento_de_visualizacao(lista = None):
  if lista == None:
     lista = list()
    print(len(lista))
    print(lista)
    lista.append(13)
      
