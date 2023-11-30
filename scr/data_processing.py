import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df_marketcap = pd.read_csv("../Data/Raw/mc.csv", parse_dates = ['DateTime'], sep=";")
df_marketcap['Market cap'] = df_marketcap['Market cap'].str.replace(',', '.').astype(float)
df_volume = pd.read_csv("../Data/Raw/volume24h.csv", parse_dates = ['DateTime'], sep=";")
df_volume.set_index('DateTime', inplace=True)
df_volume['Volume (24h)'] = df_volume['Volume (24h)'].str.replace(',', '.').astype(float)

df_dom = pd.read_csv("../Data/Raw/btc_dominance.csv", parse_dates = ['DateTime'], sep=";")
df_dom.set_index('DateTime', inplace=True)
df_dom['BTC'] = df_dom['BTC'].str.replace(',', '.').astype(float)
df_dom['ETH'] = df_dom['ETH'].str.replace(',', '.').astype(float)
df_dom['USDT'] = df_dom['USDT'].str.replace(',', '.').astype(float)
df_dom['BNB'] = df_dom['BNB'].str.replace(',', '.').astype(float)
df_dom['XRP'] = df_dom['XRP'].str.replace(',', '.').astype(float)
df_dom['Otros'] = df_dom['Otros'].str.replace(',', '.').astype(float)

df_dom["Total"] = df_dom.sum(axis=1)

df_dompercentage = df_dom[['BTC', 'ETH', 'USDT', 'BNB', 'XRP', 'Otros']].div(df_dom['Total'], axis=0) * 100

df_mcbtc = pd.read_csv("../Data/Raw/mcbtc.csv", parse_dates = ['DateTime'], sep=";")
df_mcbtc.set_index('DateTime', inplace=True)
df_mcbtc['Market cap BTC'] = df_mcbtc['Market cap'].str.replace(',', '.').astype(float)
df_mcbtc = df_mcbtc.drop(columns="Market cap")

df_mceth = pd.read_csv("../Data/Raw/mceth.csv", parse_dates = ['DateTime'], sep=";")
df_mceth.set_index('DateTime', inplace=True)
df_mceth['Market cap ETH'] = df_mceth['Market cap'].str.replace(',', '.').astype(float)
df_mceth = df_mceth.drop(columns="Market cap")

df_mcusdt = pd.read_csv("../Data/Raw/mcusdt.csv", parse_dates = ['DateTime'], sep=";")
df_mcusdt.set_index('DateTime', inplace=True)
df_mcusdt['Market cap USDT'] = df_mcusdt['Market cap'].str.replace(',', '.').astype(float)
df_mcusdt = df_mcusdt.drop(columns="Market cap")

df_mcbnb = pd.read_csv("../Data/Raw/mcbnb.csv", parse_dates = ['DateTime'], sep=";")
df_mcbnb.set_index('DateTime', inplace=True)
df_mcbnb['Market cap BNB'] = df_mcbnb['Market cap'].str.replace(',', '.').astype(float)
df_mcbnb = df_mcbnb.drop(columns="Market cap")

df_mcxrp = pd.read_csv("../Data/Raw/mcxrp.csv", parse_dates = ['DateTime'], sep=";")
df_mcxrp.set_index('DateTime', inplace=True)
df_mcxrp['Market cap XRP'] = df_mcxrp['Market cap'].str.replace(',', '.').astype(float)
df_mcxrp = df_mcxrp.drop(columns="Market cap")

df_mcusdc = pd.read_csv("../Data/Raw/mcusdc.csv", parse_dates = ['DateTime'], sep=";")
df_mcusdc.set_index('DateTime', inplace=True)
df_mcusdc['Market cap USDC'] = df_mcusdc['Market cap'].str.replace(',', '.').astype(float)
df_mcusdc = df_mcusdc.drop(columns="Market cap")

df_mcsol = pd.read_csv("../Data/Raw/mcsol.csv", parse_dates = ['DateTime'], sep=";")
df_mcsol.set_index('DateTime', inplace=True)
df_mcsol['Market cap SOL'] = df_mcsol['Market cap'].str.replace(',', '.').astype(float)
df_mcsol = df_mcsol.drop(columns="Market cap")

df_mcada = pd.read_csv("../Data/Raw/mcada.csv", parse_dates = ['DateTime'], sep=";")
df_mcada.set_index('DateTime', inplace=True)
df_mcada['Market cap ADA'] = df_mcada['Market cap'].str.replace(',', '.').astype(float)
df_mcada = df_mcada.drop(columns="Market cap")

df_mcdoge = pd.read_csv("../Data/Raw/mcdoge.csv", parse_dates = ['DateTime'], sep=";")
df_mcdoge.set_index('DateTime', inplace=True)
df_mcdoge['Market cap DOGE'] = df_mcdoge['Market cap'].str.replace(',', '.').astype(float)
df_mcdoge = df_mcdoge.drop(columns="Market cap")

df_mctrx = pd.read_csv("../Data/Raw/mctrx.csv", parse_dates = ['DateTime'], sep=";")
df_mctrx.set_index('DateTime', inplace=True)
df_mctrx['Market cap TRX'] = df_mctrx['Market cap'].str.replace(',', '.').astype(float)
df_mctrx = df_mctrx.drop(columns="Market cap")

"""Unimos columnas en un Df y concatenamos"""
dfs = [df_marketcap,df_volume,df_mcbtc, df_mceth, df_mcusdt, df_mcbnb, df_mcxrp, df_mcusdc, df_mcsol, df_mcada, df_mcdoge, df_mctrx]
result_df = pd.concat(dfs, axis=1)

"""Añadimos variables"""
result_df['MA200'] = result_df['Market cap'].rolling(window = 200).mean()
result_df['MA200/BTC'] = result_df['Market cap BTC'].rolling(window = 200).mean()
result_df['MA200/ETH'] = result_df['Market cap ETH'].rolling(window = 200).mean()
result_df['MA200/USDT'] = result_df['Market cap USDT'].rolling(window = 200).mean()
result_df['NVT'] = result_df['Market cap'] / result_df['Volume (24h)']
result_df['NVT-smooth'] = result_df['NVT'].rolling(window = 14).mean()
"""Descartamos irrelevantes"""
result_df = result_df.drop(columns="NVT")
"""Guardamos en csv"""
result_df.to_csv("Dfmcap.csv", index=False)

"""Siguiente apartado de procesamiento de datos"""
df_marketcap = pd.read_csv("../Data/Raw/dataset/Dfmcap.csv",parse_dates = ['DateTime'])
df_domper100 = pd.read_csv("../Data/Raw/dataset/df_domper100.csv",parse_dates = ['DateTime'])
df_agrupado = df_marketcap.resample('D', on='DateTime').mean()
df_domper100 = df_domper100.resample('D', on='DateTime').mean()
df_marketcap = df_marketcap.set_index("DateTime")

"""Aplicamos métodos de interpolación"""
df_agrupado = df_agrupado.interpolate(method='time')
"""Sustituimos Nan"""
df_agrupado = df_agrupado.fillna(0)

"""De nuevo"""
df_domper100 = df_domper100.interpolate(method='time')

"""A través de la siguiente funcion se añaden columnas representando el dominio de cada criptomoneda"""
monedas = ['BTC', 'ETH', 'USDT', 'BNB', 'XRP', 'USDC', 'SOL', 'ADA', 'DOGE', 'TRX']

for moneda in monedas:
    col_market_cap = f'Market cap {moneda}'
    col_porcentaje = f'Porcentaje {moneda}'
    df_agrupado[col_porcentaje] = (df_agrupado[col_market_cap] / df_agrupado['Market cap'])


"""Dataframe Definitivo"""
df_def = df_agrupado
"""Quitamos irrelevantes"""
df_def = df_def.drop(columns=["MM","NVT-smooth"])
"""Añadimos columna representando dominio de criptomonedas fuera del top 10"""
df_def['Porcentaje Otros'] = 1 - df_def.iloc[:,-10:].sum(axis=1)
"""Proceso para obtener la capitalización del total de aquellas criptomonedas fuera del top 10"""
cap_top10 = df_def[["Market cap BTC","Market cap ETH","Market cap USDT","Market cap BNB","Market cap XRP","Market cap USDC","Market cap SOL","Market cap ADA","Market cap DOGE","Market cap TRX"]].sum(axis=1)
df_def['Market cap Others'] = df_def['Market cap'] - cap_top10
"""Se coloca donde corresponde"""
df_def.insert(12, 'Market cap Others', df_def.pop('Market cap Others'))


def entrenar_modelo(data):
    