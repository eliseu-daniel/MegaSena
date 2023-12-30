import pandas as pd
import random

arquivo = 'User/Documentos/python/MegaSena/loteria.xlsx'

frequencias = {}

for coluna in dados.columns[1:]:
    frequencias[coluna] = dados[coluna].value_counts(normalize=True)

sequencia_preditiva = []

for coluna in dados.columns[1:]:
    bola_preditiva = random.choices(frequencias[coluna].index, weights=frequencias[coluna].values)[0]
    sequencia_preditiva.append(bola_preditiva)

print("Sequencias Preditiva:", sequencia_preditiva)