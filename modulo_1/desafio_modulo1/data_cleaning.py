# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 12:52:31 2020

@author: bueni

@source:Fonte: Secretarias de Saúde das Unidades Federativas, dados tratados por Álvaro Justen e colaboradores/Brasil.IO.
"""

import pandas as pd
import numpy as np

df = pd.read_csv('csv\\caso.csv')

# TO-DO LIST
# verificar a possibilidade de mexer com as datas
# separar data por mes e dia
# arrumar a formatacao dos numeros
# separar entre 3 dfs: completo, UF-only e city-only
#   em city-only, tirar cidades indefinidas

# separar data por mes e dia
df.insert(1, 'day', df.date.apply(lambda date: int(date[-2:])))
df.insert(2, 'month', df.date.apply(lambda date: int(date[5:7])))

# verificar a possibilidade de mexer com as datas
df.date = pd.to_datetime(df.date, format = "%Y-%m-%d")

# separar entre 3 dfs: completo, UF-only e city-only
uf_df = df[df['place_type'] == 'state']
city_df = df[np.logical_and(df['place_type'] == 'city', df['city'] != 'Importados/Indefinidos')]

#exportar csvs
df.to_csv('csv//casos_clean.csv')
uf_df.to_csv('csv//casos_clean_UF.csv')
city_df.to_csv('csv//casos_clean_city.csv')