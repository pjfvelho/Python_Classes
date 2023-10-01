#parte 1 

# Criando uma lista
frutas = ["maçã", "banana", "laranja"]

# Acessando elementos
primeira_fruta = frutas[0]
print(primeira_fruta)

# Adicionando um elemento
frutas.append("uva")

# Iterando em uma lista
for fruta in frutas:
    print(fruta)


#parte 2

# Criando um dicionário
pessoa = {
    "nome": "João",
    "idade": 30,
    "cidade": "São Paulo"
}

# Acessando valores
print("Nome:", pessoa["nome"])

# Adicionando um novo par chave-valor
pessoa["profissão"] = "Engenheiro"

# Iterando em um dicionário
for chave, valor in pessoa.items():
    print(chave + ":", valor)

#parte 3

# Criando conjuntos
conjunto1 = {1, 2, 3}
conjunto2 = {3, 4, 5}

# União de conjuntos
uniao = conjunto1.union(conjunto2)

# Interseção de conjuntos
intersecao = conjunto1.intersection(conjunto2)

# Verificando se um conjunto é subconjunto de outro
e_subconjunto = conjunto1.issubset(conjunto2)
