import sys

def handle(path):
	fd = open(path, 'r')
	data = fd.readlines()
	data = [i for i in data if len(i) > 5] # Filter out line that is too short
	for i, v in enumerate(data):
		data[i] = v.replace('\t', ' ').replace(' “', '\t').replace('” by ', '\t')
	data = ["ID\tTitle\tAuthorList\tDescription\n"] + data
	fs = open(path, 'w+')
	fs.writelines(data)
	fs.close()

if __name__ == '__main__':
	argv = sys.argv[1:]
	for arg in argv:
		path = arg
		handle(path)
		print(f'{path} handled -> {path}.')