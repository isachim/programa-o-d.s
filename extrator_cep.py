endereco = "Rua das Flores 72, apartamento 1002, Laranjeiras, Rio de Janeiro, Rj, 23440-120"


import re # Regular Expression "" RegEx

#5 digitos + hifen(opcional) + 3 digitos

padrao = re.compile("[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]")
busca = padrao.search(endereco) # Match
if busca:
  cep = busca.group()
  print(cep)
  
                    
