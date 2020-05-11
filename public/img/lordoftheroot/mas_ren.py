import os


#counter = 1
for file_name in os.listdir("."):
	if file_name == __file__:
		continue
	os.rename(file_name,file_name[10:])
#	counter += 1
