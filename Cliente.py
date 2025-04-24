Class Cliente:
    def _init_(self, nome):
        self.nome= nome

@property
def nome(self):
    print( *chamando @property nome()*)
    return self.nome.title()

@nome.setter
def nome(self,nome):
    print(*chamando setter nome()*)
    self._nome= nome 
