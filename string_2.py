nome = "Aiko"
idade = 23
profissao = "Estudante de TI"
linguagem = "python"

print (f"Eu sou a {nome}, tenho {idade}, sou uma {profissao} e trabalho na linguagem: {linguagem}")

print ("Nome: %s Idade %d"% (nome,idade))

print ("Nome: {} Idade: {}".format(nome,idade))

print ("Nome: {0} Idade: {1}".format(nome,idade))
print ("Nome: {nome} Idade: {idade}".format(nome=nome,idade=idade))


