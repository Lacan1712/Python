#Faremos agora o estudo sobre tuplas

#Tuplas são reconhecidas por '( )' e são imutáveis

lanche = ("Suco","Pizza","Sanduíche","Açaí","Esfirra","Brigadeiro","Bolo","Torta")
decimais = (0,1,2,3,4,5,6,7,8,9)
#Tuplas também aceitam o formato lanche[1:7] lembrando sempre que a última posição é desconsiderada

print(lanche[1:7]) #Retorna os valores da tupla iniciando na posição 1 e terminando da posição 6

#Sorted(lanche) retorna uma LISTA com a TUPLA ordenada, ou seja, a tupla em si não é modificada

print(sorted(lanche))

#A concatenação de duas tuplas, no caso: soma = (lanche+decimais) retorna a concatenação dos valores

soma = (lanche + decimais)
print(soma)
