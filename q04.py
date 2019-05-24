##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd
import numpy as np
df = pd.read_csv("tbl1.tsv", sep="\t")

df2 = df.copy()

df2['_c4'] = df2['_c4'].str.upper()

df2 = df2['_c4'].unique().sorted('_c4')

print(df2)