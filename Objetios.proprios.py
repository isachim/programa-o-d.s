class ContaCorrente: 

  def__init__(self, codigo):
      self.codigo = codigo
        self.saldo = 0

    def deposita(self, valor):
      self.saldo += valor

   def__str__(self):
  return "[>>codigo {} saldo {}<<]".format(self.codigo, self.saldo)


conta_do_gui.deposita(500)
print(conta_do_gui)

[>>Codigo 15 Saldo 500<<]


conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)

[>>Codigo 47685 Saldo 1000<<]


contas = [conta_do_gui, conta_da_dani]
print(contas)

[<__main__.ContaCorrente object at 0x7fabla6d40>, <__main__.ContaCorrente object at 07fabfla6db70>]


conta_do_gui.deposita(100)

print(contas[0])

[>>Codigo 15 Saldo 600<<]

print(conta_do_gui)

contas = [conta_do_gui, conta_da_dani, conta_do_gui]

  print(conta_do_gui)


guilherme = ('Guilherme', 37, 1981)
daniela = ('Daniela', 31, 1987)

conta_do_gui = (15, 1000)
# conta_do_gui.deposita() # variação OO
conta_do_gui[1]

1000


conta_do_gui[1] += 100

[>>Codigo 15 Saldo 600<<]

  print(contas[2])

[>>Codigo 15 Saldo 600<<]


AttributeError: 'tuple' object has no attribute 'append'
