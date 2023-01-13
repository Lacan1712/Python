#Tratamento de erros
#Erros acontecem por vários motivos e a qualquer momento, python
#apresenta uma certa analise sobre qualquer erro que aconteça, inclusive
#detalhando o tipo de erro que acontece chamado exceção.

#Essa é a estrutura para tratamento de exceções

#try: Tente algo, se der problema

#except: Use essa exceção

#else: se tudo ocorrer bem faça...

#finally: Acontece independente se der erro, sempre vai acontecer
#exemplo

try:
    a = int(input("Numerador:"))
    b = int(input("Denominador:"))
    r = a/b
except Exception as erro:
    print(f'O problema encontrado é: {erro.__class__}')
else:
    print(f'Resultado da divisão: {r}')
finally:
    print("Obrigado pelo uso")
