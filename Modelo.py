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

class Playlist (list):
     def__init__(self,nome, programas):
        self.nome = nome
        self.programas = programas
def __getitem__(self, nome, programas):
    self.nome = nome
    self.programas = programas
@property
def listagem(self):
    return self._programas

@property
def tamanho(self):
    return self._programas

def tamanho(self):
    return len (self.programas)

vingadores = filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pãnico, 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like ()
atlanta.dar_like()
alanta.dar_like()
atlanta.dar_like()

filmes_e_series + [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = playlist('fim de semana', filmes_e_series)

print(f'Tamanho do plalist: {len(playlist_fim_de_semana)}')

for programa in playlist_fim_de_semana:
    prrint(programa)

print(vingadores in playlis_fim_de_semana)

len(playlist_fim_de_semana)

print(f'Tá ou não tá? {demolidor in playlist_fim_de_semana}')

     
