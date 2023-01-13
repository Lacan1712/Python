#Tipo lista é um tipo bastante importante
#Vejamos agora a sintaxe do tipo lista

list = []#Lista vazia
list = [1,2,3],["a","b","c"]#A lista com seus elementos

#Diferentemente das tuplas listas são completamentes mutáveis

#Métodos da classe(tipo) list
b = [2,7,4,6,8,9,3,5,1]
a = ["a","b","c"]

a.append("d")         #Adiciona um valor no final da lista

b.sort()              #Ordena um conjunto de valor de forma crescente

b.sort(reverse = True)#Ordena o conjunto de valores de forma decrescente

len(b)                #Retorna a quantidade de elementos de um tipo

a.insert(3,"d")       #Cria uma posição e insere o valor, nunca substituindo

a.pop()               #Sem parâmetros remove a última posição da lista
a.pop(3)              #Remove a posição 3 da lista

b.remove(8)           #Diferente do pop() o remove() faz a removação por busca de valor

del b[3]              #Deleta um item da lista pela sua posição

