import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Carregar os dados do GitHub
url = "https://raw.githubusercontent.com/azzalim/Datavis-com-Python/refs/heads/main/data-analysis-study-1/DadosClientes.csv"
df = pd.read_csv(url)

############ ATRASO NO PAGAMENTO #############

# Filtrar apenas os clientes que cancelaram
cancelados = df[df['cancelou'] == 1]

# Criar uma nova coluna indicando se há ou não atraso
cancelados['tem_atraso'] = np.where(cancelados['atrasos_pagamento'] > 0, 'Com atraso', 'Sem atraso')

# Contar quantos cancelados têm ou não atraso
atraso_counts = cancelados['tem_atraso'].value_counts().sort_index()
porcent_atraso = (atraso_counts / atraso_counts.sum()) * 100

tabela1 = pd.DataFrame({
    'tem_atraso': atraso_counts.index,
    'atraso_counts': atraso_counts.values,
    'porcentagem (%)': porcent_atraso.round(2).values
})
print("Resumo dos cancelados:\n", tabela1)

# Plotar gráfico
plt.figure(figsize=(5, 5))
plt.pie(atraso_counts,
        labels=atraso_counts.index,
        autopct='%1.2f%%',
        startangle=90,
        wedgeprops={'linewidth': 1.0, 'edgecolor': 'white'},
        textprops={'fontsize': 10})
plt.title('Cancelamento com base no atraso dos pagamentos')

plt.show()

############ MESES DE ATRASO #############

# Filtrar apenas clientes que cancelaram e que têm atraso (> 0 meses)
cancelados_com_atraso = df[(df['cancelou'] == 1) & (df['atrasos_pagamento'] > 0)].copy()

# Contar ocorrências por número de meses em atraso e ordenar por meses
cont_atraso = cancelados_com_atraso['atrasos_pagamento'].value_counts().sort_index()

# Calcular porcentagens relativas ao total de cancelados com atraso
porcent_atraso = (cont_atraso / cont_atraso.sum()) * 100

# Tabela
tabela2 = pd.DataFrame({
    'meses_atraso': cont_atraso.index,
    'contagem': cont_atraso.values,
    'porcentagem (%)': porcent_atraso.round(2).values
})
print("Meses em atraso dos cancelados:\n", tabela2)

# Plotar gráfico de barras com porcentagens no topo
plt.figure(figsize=(8, 5))
bars = plt.bar(cont_atraso.index.astype(str), porcent_atraso.values)

# Ajustar e posicionar rótulos de porcentagem no topo de cada barra
for bar, pct in zip(bars, porcent_atraso.values):
    altura = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        altura + 0.1,                     
        f'{pct:.1f}%',
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.title('Distribuição dos cancelados por meses de atraso')
plt.xlabel('Meses de atraso')
plt.ylabel('Porcentagem dos cancelados com atraso (%)')
plt.ylim(0, porcent_atraso.max() + 8)

plt.show()

############ QUANTIDADE DE RECLAMAÇÕES #############

# Filtrar apenas clientes que cancelaram e que têm registro de reclamação (> 0 reclamações)
cancelados_com_reclamacao = df[(df['cancelou'] == 1) & (df['numero_reclamacoes'] > 0)].copy()

# Contar ocorrências por número de reclamações e ordenar
cont_reclamacao = cancelados_com_reclamacao['numero_reclamacoes'].value_counts().sort_index()

# Calcular porcentagens relativas ao total de cancelados com reclamação
porcent_reclamacao = (cont_reclamacao / cont_reclamacao.sum()) * 100

# Tabela
tabela3 = pd.DataFrame({
    'numero_reclamacoes': cont_reclamacao.index,
    'contagem': cont_reclamacao.values,
    'porcentagem (%)': porcent_reclamacao.round(2).values
})
print("Cancelados com reclamação:\n", tabela3)

# Plotar gráfico de barras com porcentagens no topo
plt.figure(figsize=(8, 5))
bars = plt.bar(porcent_reclamacao.index.astype(str), porcent_reclamacao.values)

# Ajustar e posicionar rótulos de porcentagem no topo de cada barra
for bar, pct in zip(bars, porcent_reclamacao.values):
    altura = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        altura + 0.1,                     
        f'{pct:.1f}%',
        ha='center',
        va='bottom',
        fontsize=10
    )

plt.title('Distribuição dos cancelados por número de reclamações')
plt.xlabel('Quantidade de reclamações')
plt.ylabel('Porcentagem dos cancelados com reclamação (%)')
plt.ylim(0, porcent_reclamacao.max() + 8)

plt.show()

############ MOTIVO DE CANCELAMENTO #############

# Filtrar apenas clientes que cancelaram e que registraram o motivo do cancelamento (coluna preenchida)
motivo_cancelamento = df[(df['cancelou'] == 1) & (df['motivo_cancelamento'].notna())].copy()

# Agrupar ocorrências por tipo de motivo de cancelamento e ordenar
cont_motivo = motivo_cancelamento['motivo_cancelamento'].value_counts().sort_index()

# Calcular porcentagens relativas ao tipo de cada motivo de cancelamento
porcent_motivo = (cont_motivo / cont_motivo.sum()) * 100

# Tabela
tabela4 = pd.DataFrame({
    'motivo_cancelamento': cont_motivo.index,
    'contagem': cont_motivo.values,
    'porcentagem (%)': porcent_motivo.round(2).values
})
print("Motivos de cancelamento:\n", tabela4)

# Plotar gráfico
plt.figure(figsize=(5, 5))
plt.pie(cont_motivo,
        labels=None,
        autopct='%1.2f%%',
        startangle=90,
        wedgeprops={'linewidth': 1.0, 'edgecolor': 'white'},
        textprops={'fontsize': 10})
plt.title('Motivo do cancelamento:')

# Legenda do gráfico de pizza agrupada no lado centro-esquerdo.
plt.legend(cont_motivo.index,
           title="Motivos",
           loc="center left",
           bbox_to_anchor=(1, 0.5))

plt.show()

############ MOTIVO DE CANCELAMENTO - clientes com SUPORTE TÉCNICO #############

# Filtrar apenas clientes que cancelaram e que possuíam o benefício de suporte técnico
canc_suptec = df[(df['cancelou'] == 1) & (df['suporte_tecnico'] == 'Sim')].copy()

# Agrupar ocorrências por motivo de cancelamento e ordenar
cont_suptec = canc_suptec['motivo_cancelamento'].value_counts().sort_index()

# Calcular porcentagens relativas ao motivo de cancelamento dos clientes com suporte técnico
porcent_cancsuptec = (cont_suptec / cont_suptec.sum()) * 100

# Tabela
tabela4 = pd.DataFrame({
    'motivo_cancelamento': cont_suptec.index,
    'contagem': cont_suptec.values,
    'porcentagem (%)': porcent_cancsuptec.round(2).values
})
print("Motivo de cancelamento de clientes com suporte técnico:\n", tabela4)

# Plotar gráfico
plt.figure(figsize=(5, 5))
plt.pie(cont_suptec,
        labels=None,
        autopct='%1.2f%%',
        startangle=90,
        wedgeprops={'linewidth': 1.0, 'edgecolor': 'white'},
        textprops={'fontsize': 10})
plt.title('Motivo de cancelamento de clientes com suporte técnico:')

# Legenda do gráfico de pizza agrupada no lado centro-esquerdo.
plt.legend(cont_suptec.index,
           title="Motivos",
           loc="center left",
           bbox_to_anchor=(1, 0.5))

plt.show()

############ USO DE INTERNET ACIMA DA MÉDIA #############

# Agrupar ocorrências de cancelamento dos clientes que tinham alto uso de internet
cont_alto_uso = cancelados['usa_internet'].value_counts().sort_index()

# Calcular porcentagens relativas ao uso de internet dos clientes que cancelaram seus planos e tinham consudo de internet acima da média
porcent_consumo = (cont_alto_uso / cont_alto_uso.sum()) * 100

# Tabela
tabela5 = pd.DataFrame({
    'usa_internet': cont_alto_uso.index,
    'contagem': cont_alto_uso.values,
    'porcentagem (%)': porcent_consumo.round(2).values
})
print("Consumo de internet cliente cancelado era acima da média?\n", tabela5)

# Plotar gráfico
plt.figure(figsize=(5, 5))
plt.pie(cont_alto_uso,
        labels=cont_alto_uso.index,
        autopct='%1.2f%%',
        startangle=90,
        wedgeprops={'linewidth': 1.0, 'edgecolor': 'white'},
        textprops={'fontsize': 10})
plt.title('Consumo de internet do cliente cancelado era acima da média?')

# Legenda do gráfico de pizza agrupada no lado centro-esquerdo.
plt.legend(cont_alto_uso.index,
           title="Motivos",
           loc="center left",
           bbox_to_anchor=(1, 0.5))

plt.show()

############ POR PLANO #############

# Contar ocorrências por número de meses em atraso e ordenar por meses
cont_plano = cancelados['tipo_plano'].value_counts().sort_index()

# Calcular porcentagens relativas ao total de cancelados com atraso
porcent_plano = (cont_plano / cont_plano.sum()) * 100

# Tabela
tabela6 = pd.DataFrame({
    'tipo_plano': cont_plano.index,
    'contagem': cont_plano.values,
    'porcentagem (%)': porcent_plano.round(2).values
})
print("Planos:\n", tabela6)

# Plotar gráfico de barras com porcentagens no topo
plt.figure(figsize=(8, 5))
bars = plt.bar(cont_plano.index.astype(str), porcent_plano.values)

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

plt.title('Distribuição dos cancelados por plano')
plt.xlabel('Planos')
plt.ylabel('Cancelados')
plt.ylim(0, porcent_plano.max() + 8)

plt.show()

############ POR TEMPO DE EMPRESA #############

# Criar faixas de tempo com empresa
bins = [1, 13, 26, 39, 52, np.inf]
labels = ['1-12', '13-25', '26–38', '39–51', '52+']

# Criar nova coluna com a faixa correspondente
cancelados['fidelidade'] = pd.cut(df['tempo_com_empresa'], bins=bins, labels=labels)

# Contar ocorrências por número de meses em atraso e ordenar por meses
faixa_fidelidade = cancelados['fidelidade'].value_counts().sort_index()

# Calcular porcentagens relativas ao total de cancelados com atraso
porcent_fidelidade = (faixa_fidelidade / faixa_fidelidade.sum()) * 100

# Tabela
tabela7 = pd.DataFrame({
    'faixa_fidelidade': faixa_fidelidade.index,
    'contagem': faixa_fidelidade.values,
    'porcentagem (%)': porcent_fidelidade.round(2).values
})
print("Tempo com empresa:\n", tabela7)

# Plotar gráfico de barras com porcentagens no topo
plt.figure(figsize=(8, 5))
bars = plt.bar(faixa_fidelidade.index.astype(str), porcent_fidelidade.values)

# Ajustar e posicionar rótulos de porcentagem no topo de cada barra
for bar, pct in zip(bars, porcent_fidelidade.values):
    altura = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        altura + 0.1,                     
        f'{pct:.1f}%',
        ha='center',
        va='bottom',
        fontsize=10)

plt.title('Distribuição dos cancelados por tempo com empresa')
plt.xlabel('Faixas de tempo com empresa')
plt.ylabel('Porcentagem')
plt.ylim(0, faixa_fidelidade.max() + 8)

plt.show()
