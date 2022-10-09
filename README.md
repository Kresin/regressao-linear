## Alunos:
* Gabriel Kresin
* Iago G. Tambosi
* Jonas F. Schuh

## Tarefa 2: Análise de Correlação e Regressão Linear

Este trabalho visa entender a natureza da relação linear entre os dados.

Faremos a análise de correlação, que é utilizada para medir a intensidade de associação de duas variáveis (Relação Linear), e, também a análise de regressão, que é utilizada para prever valores de uma variável dados os valores de outra. A correlação foca primeiramente na associação das variáveis, enquanto a regressão é designada para ajudar a fazer previsões.

Considere os três Grupos de Dados (datasets) do arquivo [dataset.txt](dataset.txt)

A melhor maneira para visualizar a relação entre os dados é gerando um Diagrama de Dispersão (utilize o comando scatter – veja também as bibliotecas plotly (para gráficos interativos), numpy, matplotlib e math do Python). O Diagrama de Dispersão representa o quanto uma variável é afetada por outra.

A correlação mede a direção e intensidade da relação linear. O coeficiente da correlação r entre as variáveis x e y são calculadas com a seguinte equação:

A reta da regressão é definida por:

Onde,

1. Implemente duas funções chamadas correlacao e regressao. Cada uma deve ter dois vetores Nx1 como entrada, onde N é a dimensão do vetor (no caso de x N=11). A primeira função deve calcular o coeficiente de correlação r, e a segunda função deve calcular a regressão, isto é, β0 e β1.
2. Faça um script no Python chamado demo onde para cada dataset, faça os seguintes comandos:
   1. Faça um Gráfico de Dispersão (veja função scatter). 
   2. Calcule o coeficiente de correlação. 
   3. Trace a linha da regressão no Gráfico de Dispersão (veja a função plot)
   4. Mostre os coeficientes de correlação e regressão no Gráfico de Dispersão (utilize a função title)
3. Qual dos datasets não é apropriado para regressão linear?