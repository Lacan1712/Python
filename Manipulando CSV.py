#importando a biblioteca pandas
import pandas as pd


#Setando a variável arquivo como objeto csv pandas
arquivo = pd.read_csv('Stores.csv', delimiter=",")                                    #Realizando a leitura do arquivo store.csv
arquivo.columns = ["Identificação","Local","Total Itens","Clientes","Vendas da Loja"] #Renomeando as colunas
arquivo = arquivo.describe()                                                          #Função com saída de descrições estatísticas
arquivo = arquivo.loc[["min","max","mean","std"],"Total Itens":"Vendas da Loja"]      #Filttrando as linhas e colunas

print(arquivo)
