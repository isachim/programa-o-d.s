class Conta:

  def __init__(self, codigo):
    self._codigo = codigo
    self._saldo = 0

  def deposita(self, valor):
    self._saldo += valor

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

class ContaCorrente(Conta):

  def passa_o_mes(self):
    self._saldo -= 2

class ContaPoupanca(Conta):

  def passa_o_mes(self):
    self._saldo *= 1.01
    self._saldo -= 3

for conta in contas:
  conta.passa_o_mes() # duck typing


import array as arr

arr.array('d', [1, 3.5])

array('d', [1.0. 3.5])

[>>Codigo 88 Saldo 0<<]



from abc import ABCMeta, abstractmethod

class Conta(metaclass=ABCMeta):

  def __init__(self, codigo):
    self.codigo = codigo
    self.saldo = 0

  def deposita(self, valor):
      self._saldo += valor

    @abstractmethod
    def passa_o_mes(self):
      pass

  def __str__(self):
    return "[>>Codigo {} Saldo {}<<]".format(self.codigo, self.saldo)



class ContaSalario: 

  def__init__(self, codigo):
      self._codigo = codigo
        self._saldo = 0

    def.deposita(self, valor):
      self._saldo += valor

    def__str__(self):
      return "[>>Codigo {} Saldo {}<<]".format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
print(conta1)

[>>Codigo 37 Saldo 0<<]

def__eq__(self, outro):
  return self.codigo == outro._codigo and self._saldo == outro._saldo


idades = [15, 87, 32, 65, 56, 32, 49, 37]

for i in range(len(idades)):
  print(i, idades[i])

15
87
32
65
56
32
49
37

enumerate(idades)

<enumerate at 0x7f4846889fc0>

type(range(len(idades)))

range

list(range(len(idades))) # forcei a geração dos valores

[0,1,2,3,4,5,6,7]

for indice, idade in enumerate(idades): # unpacking da nossa tupla
  print(indice, "x", idade)

0 x 15
1 x 87
2 x 32
3 x 65
4 x 56
5 x 32
6 x 49
7 x 37

for nome,_,_ in usuarios: # ja desempacotando, ignorando o resto
  print(nome)

Guilherme
Daniela
Paulo
