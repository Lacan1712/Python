


#Definindo a classe 'Calculadora'
class Calculadora:
    # Definindo o método construtor
    def __init__(self, operacao):
        self._operacao = operacao

#Definindo o método getter e setter
    @property
    def operacao(self):
        return self._operacao

    @operacao.setter
    def operacao(self, nova_operacao):
        self._operacao = nova_operacao

#Criação dos métodos correspondentes às operações matemáticas: Multiplicação, Soma, Divisão, Subtração e Resto
    def multiplica(self, x, y):
        resultado = x*y
        print("Resultado: " + str(resultado))

    def soma(self, x, y):
        resultado = x+y
        print("Resultado: ", resultado)

    def Divisao(self, x, y):
        resultado = x/y
        print("Resultado: " + str(resultado))

    def Subtracao(self, x, y):
        resultado = x-y
        print("Resultado: " + str(resultado))

    def Resto(self, x, y):
        resultado = x % y
        print("Resultado: " + str(resultado))

    pass
#Fim da classe Calculadora

#################################################################################################################

#Definindo 'calculadora01' como um objeto
calculadora01 = Calculadora("nenhuma")

#Construção do menu de interação
cont = 0
while(cont != 1):
    print( "\n[1] Multiplicação \n[2] Soma \n[3] Divisão \n[4] Subtração \n[5] Resto\n[6] Sair\n") #Apresentação das ações possíveis
    opr = input("Selecione a ação desejada:") #Escutando o valor de entrada em uma variável

    #Definindo uma estrutura switche case

    match opr:
        case "1":
            calculadora01.operacao = "Multiplicação"   #Seta o atributo de operação de 'none' para a atual
            x = int(input("Valor x: "))                #Escutando a entrada do valor de x
            y = int(input("Valor y: "))                #Escutando a entrada do valor de x
            calculadora01.multiplica(x,y)              #Método definido na classe calculadora
                                                       #A lógica segue para os demais casos

        case"2":
            calculadora01.operacao = "Soma"
            x = int(input("Valor x: "))
            y = int(input("Valor y: "))
            calculadora01.soma(x,y)

        case "3":
            calculadora01.operacao = "Divisão"
            x = int(input("Valor x: "))
            y = int(input("Valor y: "))
            calculadora01.Divisao(x, y)

        case "4":
            calculadora01.operacao = "Subtração"
            x = int(input("Valor x: "))
            y = int(input("Valor y: "))
            calculadora01.Subtracao(x, y)

        case "5":
            calculadora01.operacao = "Resto"
            x = int(input("Valor x: "))
            y = int(input("Valor y: "))
            calculadora01.Resto(x, y)

        case "6":
            print("Saindo...")
            cont = 1
        case _:
            print("Digite uma das operações possíveis")
        #Fim da estrutura switche case

#Fim do menu de interação



