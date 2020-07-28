import sys
import pandas as pd
import os
import csv

root = 'tables'
_, _, files = next(os.walk(root))
files = [
	f for f in files 
	if not f.startswith('.') and f.endswith('tsv')
]

datas = {}
for file in files:
	try:
		path = os.path.join(root, file)
		df = pd.read_csv(path, sep='\t')
		datas[file] = df
	except Exception as e:
		print(file)
		print(e)
		exit(1)

for k, v in datas.items():
	row_cnt = len(v)
	name = k.strip('.tsv')
	datas[k]['Chapter'] = [name for _ in range(row_cnt)]


final_df = pd.concat([v for k, v in datas.items()], ignore_index=True)
final_df = final_df.apply(lambda x: x.str.strip() if x.dtype == "str" else x)

# Rearrange Columns
cols = list(df.columns.values)
cols.remove('Chapter')
cols.insert(0, 'Chapter')
final_df = final_df[cols]
final_df = final_df.sort_values('Chapter')
final_df.to_csv('all.tsv', sep='\t', index=False)