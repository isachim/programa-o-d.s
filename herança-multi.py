class funcionario:
  def registra_horas(self, horas):
      print('Horas registradas...')

  def mostrar_tarefas(self):
      print('Fez muia coisa...'0


Class Caelum(funcionario):
   def mostrar_tarefas(self):
       print('Fez muita coisa, Caelumer')

   def busca_cursos_do_mes(self, mes=None):
       print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mẽs')

Class Alura(Funcionario):
   def mostrar_tarefas(self):
       print('Fez muita coisa, Alurete!')

   def busca_perguntas_sem_respostas(self):
       print('Mostrando perguntas não espondidas no fórum')

Class Hipster:
   def __str__(self):
       return f'Hipster,  {self.nome}'

Class Junior(Alura0:
   pass

Class Pleno(Alura, Caelum):
   pass

Class Senior(Alura, Caelum):
   pass

jose = Junior()
jose.busca_perguntas_sem_respostas()
jose.busca_curos_do_mes()

luan = Pleno()
luan.busca_perguntas_sem_resposta()
luan.busca_cursos_do_mes()

luan.mostrar_tarefas()

#MRO
# pleno > Alura > Funcionario > Caelum > Funcionario

Luan = Senior('Luan')
print(luan)

