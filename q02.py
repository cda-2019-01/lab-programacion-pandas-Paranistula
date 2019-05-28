##
## Imprima el promedio de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
## ejecutar = python3 q01.py
import pandas as pd

df0 = pd.read_csv("tbl0.tsv", sep="\t")

df0 = df0.groupby('_c1').mean()['_c2']

print(df0)