from io import StringIO
import pandas as pd
import datacompy

data1 = """acct_id,dollar_amt,name             ,float_fld ,date_fld, extra_col1
10000001234,123.45    ,George Maharis1     ,14530.1555,2017-01-01
10000001235,0.45      ,Michael Bluth      ,1         ,2017-01-01
10000001236,1345      ,George Bluth       ,          ,2017-01-01
10000001237,123456    ,Bob Loblaw         ,345.12    ,2017-01-01
10000001238,123456    ,Bob Loblaw         ,345.12    ,2017-01-01
"""

data2 = """acct_id,dollar_amt,name             ,float_fld ,date_fld
10000001234,123.45    ,George Maharis123     ,14530.1555,2017-01-01
10000001235,0.45      ,Michael Bluth      ,1         ,2017-01-01
10000001236,1345      ,George Bluth       ,          ,2017-01-01
10000001237,123456    ,Bob Loblaw         ,345.12    ,2017-01-01
"""

df1 = pd.read_csv(StringIO(data1))
df2 = pd.read_csv(StringIO(data2))

compare = datacompy.Compare(
    df1,
    df2,
    join_columns='acct_id',
    abs_tol=0,
    rel_tol=0,
    df1_name='Source',
    df2_name='Target',
    )
compare.matches(ignore_extra_columns=False)
reports,metrics = compare.report(html_file='report.html')
print(reports)
print("\nMetrics:")
print(metrics)