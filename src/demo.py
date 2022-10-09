# Import das dependências
import plotly.express as px
import pandas as pd
import numpy as np
from matplotlib import pyplot
import scipy.stats

# Criação dos dataframes
data = {'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'y': [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68]}
dataFrame1 = pd.DataFrame(data)

data = {'x': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
        'y': [9.14, 8.14, 8.47, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74]}
dataFrame2 = pd.DataFrame(data)

data = {'x': [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 19],
        'y': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 5.56, 7.91, 6.89, 12.50]}
dataFrame3 = pd.DataFrame(data)

dataFrame4 = pd.read_excel('datasets/Dados Plano de Saúde USA.xlsx')


# Calcula o coeficiente de correlação a partir de dois vetores unidimensionais
def correlacao(x, y):
    return np.corrcoef(x, y)


# Calcula a regressão linear entre dois vetores unidimensionais
def regressao(x, y):
    return scipy.stats.linregress(x, y)


# Monta e exibe o gráfico de disperssão a partir de dois vetores unidimensionais
def grafico_dispersao(x, y):
    pyplot.scatter(x, y)
    pyplot.title("Gráfico de dispersão entre x e y")
    pyplot.show()


# Monta e exibe o gráfico de regressão linear a partir de um dataFrame da lib pandas
def grafico_regressao_linear(dataframe):
    grafico = px.scatter(dataframe, x="x", y="y", trendline="ols", title="Gráfico de regressão linear")
    grafico.show()


def analise_dataframe_1():
    print("Análise do dataset 1:\n")
    print("Gráfico de dispersão: ")
    grafico_dispersao(dataFrame1["x"], dataFrame1["y"])
    result = correlacao(dataFrame1["x"], dataFrame1["y"])
    print("Correlação:")
    print(result)
    print("\nRegressão:")
    result = regressao(dataFrame1["x"], dataFrame1["y"])
    print(result)
    print("\nGráfico regressão:")
    grafico_regressao_linear(dataFrame1)


def analise_dataframe_2():
    print("Análise do dataset 2:\n")
    print("Gráfico de dispersão: ")
    grafico_dispersao(dataFrame2["x"], dataFrame2["y"])
    result = correlacao(dataFrame2["x"], dataFrame2["y"])
    print("Correlação:")
    print(result)
    print("\nRegressão:")
    result = regressao(dataFrame2["x"], dataFrame2["y"])
    print(result)
    print("\nGráfico regressão:")
    grafico_regressao_linear(dataFrame2)


def analise_dataframe_3():
    print("Análise do dataset 3:\n")
    print("Gráfico de dispersão: ")
    grafico_dispersao(dataFrame3["x"], dataFrame3["y"])
    result = correlacao(dataFrame3["x"], dataFrame3["y"])
    print("Correlação:")
    print(result)
    print("\nRegressão:")
    result = regressao(dataFrame3["x"], dataFrame3["y"])
    print(result)
    print("\nGráfico regressão:")
    grafico_regressao_linear(dataFrame3)


def analise_dados_plano_de_saude():
    print(
        "Análise da planilha de dados de saúde (A função utilizada será a idade da pessoa em relação o  valor de cobrança):\n")
    print("Gráfico de dispersão: ")
    grafico_dispersao(dataFrame4["Valor Cobrança"], dataFrame4["Idade"])
    result = correlacao(dataFrame4["Valor Cobrança"], dataFrame4["Idade"])
    print("Correlação:")
    print(result)
    print("\nRegressão:")
    result = regressao(dataFrame4["Valor Cobrança"], dataFrame4["Idade"])
    print(result)
    print("\nGráfico regressão:")
    grafico = px.scatter(dataFrame4, x="Valor Cobrança", y="Idade", trendline="ols",
                         title="Gráfico de regressão linear")
    grafico.show()


def main():
    analise_dataframe_1()
    print("\n---------------------------\n")
    analise_dataframe_2()
    print("\n---------------------------\n")
    analise_dataframe_3()
    print("\n---------------------------\n")
    analise_dados_plano_de_saude()


main()
