#Alguns exemplos de manipulação de listas

#Vamos criar uma espécie de buffer de dados com o nome e idades de pessoas

pessoas = list()
dados = list()

for c in range(0,4):
    dados.append(str(input("Nome:")))
    dados.append(int(input("Idade:")))
    pessoas.append(dados[:])
    dados.clear();
