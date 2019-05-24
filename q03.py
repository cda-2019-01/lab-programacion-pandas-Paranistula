##
## Imprima el maximo de la _c2 por cada letra de la _c1 
## de la tabla tbl0
## 
import pandas as pd
import numpy as np
df = pd.read_csv("tbl0.tsv", sep="\t")
df2 = df.copy()

df2 = df2.groupby('_c1').max()['_c2']

print(df2)