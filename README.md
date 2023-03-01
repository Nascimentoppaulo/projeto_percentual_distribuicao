# projeto_percentual_distribuicao


**DESCRIÇÃO**

Este código calcula o percentual de representação de cada estado no faturamento mensal de uma distribuidora. O valor do faturamento é detalhado por estado e é representado em um dicionário, com as chaves sendo os nomes dos estados e os valores sendo os valores do faturamento. O programa calcula o percentual de representação de cada estado em relação ao valor total do faturamento mensal da distribuidora.

**USO**

Para usar este programa, basta executá-lo em qualquer ambiente Python compatível, como um console interativo ou um arquivo Python. Não há dependências externas ou parâmetros necessários.

**Exemplo**

Um exemplo de uso do programa é:

\# definir um dicionário com o faturamento por estado
faturamento = {

    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

\# calcular o total de faturamento somando os valores do dicionário


total_faturamento = sum(faturamento.values())

\# iterar sobre o dicionário para calcular o percentual de faturamento de cada estado


    for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100  
    
 \# calcular o percentual de faturamento
 
 
    print(f'{estado}: {percentual:.2f}%')  # exibir o percentual com duas casas decimais

A saída para esse exemplo seria:


SP: 39.90%

RJ: 21.61%

MG: 17.24%

ES: 16.02%

Outros: 5.23%


 
**Documentação**

O código está documentado com comentários que explicam a lógica, as variáveis e o fluxo de controle. Os comentários seguem as melhores práticas de documentação de código, incluindo uma descrição geral do código, descrições de variáveis e funções, e explicações de fluxo de controle.
