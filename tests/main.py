from io import StringIO
import pandas as pd
import datacompy
from datacompy import facade

# from datacompy import facade

data1 = """acct_id,dollar_amt,name             ,float_fld ,date_fld, extra_col1
10000001234,123.45    ,George Maharis1     ,14530.1555,2017-01-01
10000001235,0.45      ,Michael Bluth      ,1         ,2017-01-01
10000001236,1345      ,George Bluth       ,          ,2017-01-01
10000001237,123456    ,Bob Loblaw         ,345.12    ,2017-01-01
10000001238,123456    ,Bob Loblaw         ,345.12    ,2017-01-01
"""

data2 = """acct_id,dollar_amt,name             ,float_fld ,date_fld
10000001234    ,George Maharis123     ,14530.1555,2017-01-01
10000001235,Michael Bluth      ,1         ,2017-01-01
0000001236,George Bluth       ,          ,2017-01-01
10000001237,Bob Loblaw         ,345.12    ,2017-01-01
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))
reports,metrics,status = facade.try_compare(df1, df2, key='acct_id')
print(status)
print(reports)