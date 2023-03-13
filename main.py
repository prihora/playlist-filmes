playlist = []

print("Olá! Essa é a minha Playlist de Filmes!")
novo_filme = input("Digite 'sim' se você deseja inserir um filme, caso contrário, digite 'não': ")

if novo_filme == "nao" or novo_filme == "não" or novo_filme == "Nao" or novo_filme == "Não":
  print("Tudo bem! Infelizmente não terei a sua indicação.")

while novo_filme == "sim" or novo_filme == "Sim":
  colega = input("Qual o seu primeiro e último nome: ")
  titulo =  input("{}, digite o título do seu filme favorito: ".format(colega))
  genero = input("Qual o gênero de '{}'? ".format(titulo))
  diretor = input("Quem dirigiu '{}'? ".format(titulo))
  ano = int(input("Qual o ano em que '{}' foi lançado? ".format(titulo)))
    
  filme = {
    "título": titulo,
    "gênero": genero,
    "diretor(a)": diretor,
    "ano": ano,
    "colega": colega
  }
  
  playlist.append(filme)

  novo_filme = input("\n Filme inserido. Agora, se você ou outra pessoa deseja inserir mais um filme, é só digitar 'sim', caso contrário, digite 'não'! ")
  if novo_filme == "nao" or novo_filme == "não" or novo_filme == "Nao" or novo_filme == "Não":
    break

print("\n::: Lista de filmes para assistir na Netflix durante as férias :::")
print("=========================================================")

for filme in playlist:
  print(">>> Filme indicado por {}".format(filme['colega']))
  print("- Título: {}".format(filme['título']))
  print("- Gênero: {}".format(filme['gênero']))
  print("- Diretor(a): {}".format(filme['diretor(a)']))
  print("- Ano de lançamento: {}".format(filme['ano']))
  print("=========================================================")
