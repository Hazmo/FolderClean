import os
import shutil


directory = raw_input("Please enter the directory you want to clean: ")
dir_list = os.listdir(directory)
unmoved_files = []

for file in dir_list:
	file_directory = directory + "\\" + file
	if '.' in file:
		if '.' in file[-3:]:
			folder = file[-2:]
			if not os.path.exists(folder_directory):
				os.mkdir(folder_directory)
			
		else:
			folder = file[-3:]
			folder_directory = directory + "\\" + folder
			if not os.path.exists(folder_directory):
				os.mkdir(folder_directory)
			
		if not os.path.exists(folder + "\\" + file):
			print file
			shutil.move(file_directory, folder_directory)
		else:
			unmoved_files.append(file)

if unmoved_files:			
	print "The following files could not be moved:"
	for file in unmoved_files:
		print file