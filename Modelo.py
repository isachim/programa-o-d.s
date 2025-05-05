class Filme:
  def __init__(self, nome, ano, duracao):
      self.__nome = nome
      self.ano = ano
      self.duracao = duracao
      self.__likes = 0
@property
def likes(self):
    return self.__likes

  def dar_like(self):
      self.__likes += 1

@property
def nome(self):
    return self.__nome

@nome.setter
def nome(self, novo_nome):
    self.__nome = novo_nome.title()

  class Serie:
   def __init__(self,nome,ano, temporadas):
       self.nome = nome
       self.ano = ano
       self.temporadas = temporadas
       self.likes = 0

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
print(f'Nome: {vingadores.nome} - Ano: {vingadores.ano} '
      f'- Duração: {vingadores.duracao} - Likes {vingadores.likes}')
vingadores.dar_like()
atlanta = Serie('atlanta', 2018, 2)

print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} '
      f'- Temporadas: {atlanta.temporadas} -Likes {atlanta.likes}')
atlanta.darlike()

     
