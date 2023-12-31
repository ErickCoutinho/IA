from src.utils import load_wine_dataset
import numpy as np
import pandas as pd

wine = load_wine_dataset()

pd.set_option('display.max_columns', None)

# print as caractéristicas estatísticas do dataset wine
print(wine.describe())

## Aplique a função de nomarlização logarítmica na coluna Proline
wine['Proline_log'] = np.log(wine['Proline'])

# Print a variância da coluna proline
print('\n')
print('Coluna Proline sem logaritmo')
print(np.var(wine['Proline']))

# print a variância da coluna proline normalizada
print('\n')
print('coluna proline com logaritmo')
print(np.var(wine['Proline_log']))
