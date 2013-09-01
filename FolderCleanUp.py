import os
import shutil

dir_list = os.listdir('C:\Users\Maureen\Downloads')
unmoved_files = []

for file in dir_list:
	if '.' in file:
		if '.' in file[-3:]:
			folder = file[-2:]
			if not os.path.exists(folder):
				os.mkdir(folder)
			
		else:
			folder = file[-3:]
			if not os.path.exists(folder):
				os.mkdir(folder)
			
		if not os.path.exists(folder + "\\" + file):
			shutil.move(file, folder)
		else:
			unmoved_files.append(file)

if unmoved_files:			
	print "The following files could not be moved:"
	for file in unmoved_files:
		print file