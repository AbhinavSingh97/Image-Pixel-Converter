#This is the puzzle
from sys import *
from groups import *

def puzzle():
	try:
		f = open(argv[1], "r")

	except:
		print "File could not be opened or no argument was given"
		exit() 

	try:
		hid = open("hidden.ppm", "w")
		hid.write("P3\n")
		temp_list = []
		count = 0
		
		for line in f:
			l = line.split()
			count += 1
			
			for i in l:
				try:
					if count < 4:
						if count == 2:
							width = int(l[0])
							height = int(l[1])

					elif float(i) * 10 > 255:
						r = 255
						g = 255
						b = 255
						temp_list.append(str(255))
					else:
						r = float(i) * 10
						ri = int(r)
						temp_list.append(str(ri))
				except:
					pass
		hid.write(str(width) + ' ')
		hid.write(str(height) + '\n')
		hid.write("255\n")
		fin_list = groups_of_3(temp_list)
		
		for i in fin_list:
			hid.write(i[0] + " "+ i[0] + " " + i[0] + '\n')
				

		
		f.close()
		hid.close()
	
	except:
		print "Something went wrong with the processing of the image"
		exit()
if __name__ == "__main__":
	puzzle()