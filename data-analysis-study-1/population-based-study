import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = "https://raw.githubusercontent.com/azzalim/Datavis-com-Python/refs/heads/main/DadosClientes.csv"
df = pd.read_csv(url)

############ FAIXA ETARIA #############

# Criar faixas etárias
bins = [17, 27, 37, 47, 57, np.inf]
labels = ['18–26', '27–36', '37–46', '47–56', '56+']

# Criar nova coluna com a faixa correspondente
df['faixa_etaria'] = pd.cut(df['idade'], bins=bins, labels=labels)

# Contar número de pessoas em cada faixa e calcular a porcentagem do total em cada faixa
faixa_etaria = df['faixa_etaria'].value_counts().sort_index()
faixas_percentual = df['faixa_etaria'].value_counts(normalize=True).sort_index() * 100

# Mostrar contagem em tabela
print("Quantidade de pessoas por faixa etária:")
print(faixa_etaria)

# Plotar gráfico diretamente com pandas
graf_faixaetaria = faixa_etaria.plot(
    kind='barh',
    title='Distribuição por Faixa Etária (%)',
    xlabel='Faixa Etária',
    ylabel='Clientes',
    grid=False,
    color='steelblue',
    edgecolor='black'
)

# Adicionando rótulo de porcentagem em cada faixa
for i, (v, p) in enumerate(zip(faixa_etaria, faixas_percentual)):
    graf_faixaetaria.text(v + 1, i, f'{p:.1f}%', va='center')

plt.show()

############ ATIVOS x CANCELADOS #############

df['status_cliente'] = np.where(df['cancelou'] == 1, 'Cancelados', 'Ativos')
cancelamentos = df['status_cliente'].value_counts().sort_index()
labels = cancelamentos.index

plt.pie(cancelamentos, labels=labels,
        autopct='%1.1f%%', startangle=90,
        wedgeprops={'linewidth': 0.5, 'edgecolor': 'white'},
        textprops={'fontsize': 10})
plt.title('Status dos clientes:')

plt.show()

############ PLANOS #############

# Agrupamento por plano
planos = df['tipo_plano'].value_counts().sort_index()

# Calcular porcentagens relativas ao total de cancelados com atraso
porcent_plano = (planos / planos.sum()) * 100

# Tabela
tabela_planos = pd.DataFrame({
    'meses_atraso': planos.index,
    'contagem': planos.values,
    'porcentagem (%)': porcent_plano.round(2).values
})
print("Distribuição de clientes por plano:\n", tabela_planos)

# Plotar gráfico de barras com porcentagens no topo
plt.figure(figsize=(8, 5))
bars = plt.bar(planos.index.astype(str), porcent_plano.values)

# Ajustar e posicionar rótulos de porcentagem no topo de cada barra
for bar, pct in zip(bars, porcent_plano.values):
    altura = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        altura + 0.1,                     
        f'{pct:.1f}%',
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.title('Distribuição de clientes por plano')
plt.xlabel('Planos')
plt.ylabel('Porcentagem de clientes por plano (%)')
plt.ylim(0, porcent_plano.max() + 8)

plt.show()

############ FAIXA SALARIAL #############

# Criar faixas salariais
bins = [1412.00, 2824.00, 4236.00, 5684.00, 7096.00, np.inf]
labels = ['até 1', '1 a 2', '2 a 3', '3 a 4', '4+']

# Criar nova coluna com a faixa correspondente
df['faixa_salarial'] = pd.cut(df['renda_mensal'], bins=bins, labels=labels)

# Contar número de pessoas em cada faixa e calcular a porcentagem do total em cada faixa
faixa_salarial = df['faixa_salarial'].value_counts().sort_index()
faixas_salperc = df['faixa_salarial'].value_counts(normalize=True).sort_index() * 100

# Mostrar contagem em tabela
print("Faixa salarial:")
print(faixa_salarial)

# Plotar gráfico diretamente com pandas
graf_faixasalarial = faixa_salarial.plot(
    kind='barh',
    title='Distribuição por Faixa Salarial (%)',
    xlabel='Faixa Salarial',
    ylabel='Clientes',
    grid=False,
    color='steelblue',
    edgecolor='black'
)

# Adicionando rótulo de porcentagem em cada faixa
for i, (v, p) in enumerate(zip(faixa_salarial, faixas_salperc)):
    graf_faixasalarial.text(v + 1, i, f'{p:.1f}%', va='center')

plt.show()

############ GÊNERO #############
 
genero = df['genero'].value_counts().sort_index()
labels = genero.index

plt.pie(genero, labels=labels,
        autopct='%1.1f%%', startangle=90,
        wedgeprops={'linewidth': 0.5, 'edgecolor': 'white'},
        textprops={'fontsize': 10})
plt.title('Status dos clientes:')

plt.show()

############ FIDELIDADE #############

# Criar faixas de tempo com empresa
bins = [1, 13, 26, 39, 52, np.inf]
labels = ['1-12', '13-25', '26–38', '39–51', '52+']

# Criar nova coluna com a faixa correspondente
df['fidelidade'] = pd.cut(df['tempo_com_empresa'], bins=bins, labels=labels)

# Contar número de pessoas em cada faixa e calcular a porcentagem do total em cada faixa
fidelidade = df['fidelidade'].value_counts().sort_index()
faixas_fidelidade = df['fidelidade'].value_counts(normalize=True).sort_index() * 100

# Mostrar contagem em tabela
print("Quantidade de pessoas por faixa de tempo com empresa")
print(fidelidade)

# Plotar gráfico diretamente com pandas
graf_fidelidade = fidelidade.plot(
    kind='barh',
    title='Distribuição por Faixa de Tempo com Empresa (%)',
    xlabel='Clientes',
    ylabel='Faixa de tempo com empresa',
    grid=False,
    color='steelblue',
    edgecolor='black'
)

# Adicionando rótulo de porcentagem em cada faixa
for i, (v, p) in enumerate(zip(fidelidade, faixas_fidelidade)):
    graf_fidelidade.text(v + 1, i, f'{p:.1f}%', va='center')
    
plt.show()
