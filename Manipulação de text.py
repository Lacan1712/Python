#Existem alguns métodos para o tratamento de uma str
#Vejamos a sua sintaxe

#Lower
palavra = "ATRÁs DO POTE TEM BOLO"
palavra.lower()
print(palavra.lower())
#Será printado na tela todoas as lestras em minúsculas

#Upper
palavra1 = "atrás do pote tem bolo"
palavra1.upper()
print(palavra.upper())
#Será printado na tela toas as letras em maiusculas

#Split
palavra2 = "atrás da geladeira tem bolo"
palavra2.split()
print(palavra2.split())
#Cria uma lista de str com cada palavra

#[0:0]
palavra[4:10]
#Retorna as letras que iniciam na 4ª posição e termina na 10ª-1 posição

#[0:0:0]
palavra[2:3:10]
#Retorna as letras que iniciam na 2º posição saltando de 3 em 3 posição até 10º-1

#count("str")
palavra.count("o")
#Vai retonar o número de vezes que "o" aparece na frase

#replace("str","str")
palavra.replace("ATRÀS","NA FRENTE")
#replace() irá trocar a palavra "ATRÁS" pela palavra "NA FRENTE"

#find("str")
palavra1.find('pote')
#Retorna a posição em que a palavra "pote" incia-se, no caso: 8







