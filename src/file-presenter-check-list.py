import sys
import csv

path = "all.tsv"
chapter_names = "chapter-names.csv"
with open(path, 'r') as f:
	reader = csv.DictReader(f, delimiter='\t')
	rows = [r for r in reader]

with open(chapter_names, 'r') as f:
	reader = csv.DictReader(f, delimiter=',')
	chapters = {r["ID"]: r["Title"] for r in reader}

readme = []
current_chapter = -1
for r in rows:
	# chapter = r['Chapter']
	# if chapter != current_chapter:
	# 	current_chapter = chapter
	# 	chapter_name = chapters[current_chapter]
	# 	readme.append(f'# Chapter {current_chapter}: {chapter_name}')
	# 	readme.append('')
	ID = r['ID']
	Title = r['Title'].strip()
	AuthorList = r['AuthorList'].strip()
	Description = r['Description'].strip()
	readme.append(f'- [ ] **{Title}** *{AuthorList}* {Description}')
	# readme.append(AuthorList)
	# readme.append(Description)
	# readme.append('')

readme = '\n'.join(readme)
print(readme)