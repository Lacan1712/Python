#Importando biblioteca matplot para construção dos gráfico
import matplotlib.pyplot as plt

#Definindo a função de retorno para o plot
def f(x):
    return 8*x + 8*x - 1

#Criação das variáveis
y = [] #Lista com valores de f(x)
x = [] #Lista com valores de x
resposta = " "

#Looping com condição de parada para inserção de valores de x
while(resposta != "Sair"):
    valor = input("Digite os valores de x para [8x + 8x - 1]: ")
    y.append(f(int(valor))) #Adicionando valor à lista y com uso de type cast
    x.append(int(valor))    #Adicionand valor à lista x com uso de type cast
    resposta = str(input("Digite C para continuar ou S para sair: "))
    #Tratando condição de parada
    if(resposta == "S"):
        plt.plot(x, y, label = "Gráfico") #Exibe o gráfico com a legenda "Gráfico"
        plt.legend() #Função de exibição das legendas
        plt.show()   #Função que mostra o gráfico em modo janela
        resposta = "Sair"






