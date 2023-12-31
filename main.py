import pandas as pd
import random

arquivo = '/home/eliseulinux/Documentos/python/MegaSena/loteria.xlsx'

dados = pd.read_excel(arquivo)

frequencias = {}

for coluna in dados.columns[1:]:
    frequencias[coluna] = dados[coluna].value_counts(normalize=True)

numeros_sorteados = []

for coluna in dados.columns[1:]:
    bola_preditiva = random.choices(frequencias[coluna].index, weights=frequencias[coluna].values)[0]
    numeros_sorteados.append(bola_preditiva)

print("Números Sorteados:", numeros_sorteados)