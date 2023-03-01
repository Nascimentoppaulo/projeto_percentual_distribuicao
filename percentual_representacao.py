# definir um dicionário com o faturamento por estado
faturamento = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

# calcular o total de faturamento somando os valores do dicionário
total_faturamento = sum(faturamento.values())

# iterar sobre o dicionário para calcular o percentual de faturamento de cada estado
for estado, valor in faturamento.items():
    percentual = (valor / total_faturamento) * 100  # calcular o percentual de faturamento
    print(f'{estado}: {percentual:.2f}%')  # exibir o percentual com duas casas decimais
