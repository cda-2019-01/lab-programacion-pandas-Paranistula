##
## Construya una tabla que contenga _c0 y una lista
## separada por ',' de los valores de la columna _c5a
## y _c5b (unidos por ':') de la tabla tbl2.tsv
## 

import pandas as pd
import numpy as np
df = pd.read_csv("tbl0.tsv", sep="\t")