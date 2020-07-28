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

print(datas)