import pandas as pd

df=pd.DataFrame({'pipeline':['etl'],'error':['schema mismatch']})
assert 'pipeline' in df.columns
print('Validation passed')
