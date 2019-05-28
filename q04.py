##
## Imprima los valores unicos e la columna _c4 de 
## de la tabla tbl1 en mayusculas
## 
import pandas as pd

df1 = pd.read_csv("tbl1.tsv", sep="\t")

uniques = df1['_c4'].unique()
res = []
for elemt in uniques:
    res.append(elemt.upper())
res = sorted(res)
res

print(res)