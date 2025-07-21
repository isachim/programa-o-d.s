for nome,_,_ in usuarios: # ja desempacotando, ignorando o resto
  print(nome)

Guilherme
Daniela
Paulo

idades

[15, 87, 32, 65, 56, 32, 49, 37]

sorted(idades)

[15, 32, 32, 37, 49, 56, 65, 87]

15 < 32

True

reversed(idades)

<list_reverseiterator at 0x7f4846782e8>

list(reversed(idades))

[37, 49, 32, 56, 65, 32, 87, 15]

sorted(idades, reverse=True)

[87, 65, 56, 49, 37, 32, 32, 15]

list(reversed(sorted(idades)))

[87, 65, 56, 49, 37, 32, 32, 15]

idades

[15, 87, 32, 65, 56, 32, 49, 37]

def__lt__(self, outro):
  return self._saldo < outro._saldo


def extrai_saldo(conta):
  return conta_saldo

for conta in sorted(contas, key=extrai_saldo):

[>>Codigo 17 Saldo 500<<]
[>>Codigo 133 Saldo 210<<]
[>>Codigo 3 Saldo 1000<<]

for conta in sorted(contas, key=attrgetter("_saldo", "_codigo")):
  print(conta)

[>>Codigo 3 Saldo 500<<]
[>>Codigo 133 Saldo 500<<]


 class ContaSalario:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def __eq__(self, outro):
    if type(outro) != ContaSalario:
      return False

    return self._codigo == outro._codigo and self._saldo == outro._saldo

  def __lt__(self, outro):
    return self._saldo < outro._saldo

        def deposita(self, valor):
          self._saldo += valor

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)
