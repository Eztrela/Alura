usuarios_data_science = {15,23,43,56}
usuarios_machine_learning = {13,23,56,42}

assistiram = usuarios_data_science | usuarios_machine_learning
usuarios_data_science & usuarios_machine_learning
usuarios_data_science - usuarios_machine_learning
usuarios_data_science ^ usuarios_machine_learning
print(assistiram)

usuarios = {1,5,76,34,52,13,17}
print(len(usuarios))

usuarios.add(13)
print(len(usuarios))

usuarios.add(765)
print(len(usuarios))

usuarios = frozenset(usuarios)
print(usuarios)

print(type(usuarios))

#usuarios.add(134) daria erro pois usuarios agora é frozenset

meu_texto = "Bem vindo meu nome é Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto.split()
set(meu_texto.split())