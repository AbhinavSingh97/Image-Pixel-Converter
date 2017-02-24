from sys import *
from groups import *
from math import *

def fade():
	try:
		f = open(argv[1], "r")
	except:
		print "File could not be opened or no file was given"
		exit()
			
	fin_list= []
	hid = open("faded.ppm", "w")
	hid.write("P3\n")
	try:
		radius = int(argv[4])
		col = int(argv[3])
		row = int(argv[2])
	except:
		print "There was an invalid argument input into commandline or there was a missing argument."
		print "Remember the arguements are row, column, and radius. These are expected to be integers"
		exit()

	count = 0
	temp_list = []
	
	for line in f:
		l = line.split()
		count += 1
		for i in range(len(l)):
				if count < 4:
					if count == 2:
						width = int(l[0])
						height = int(l[1])
				else:
					temp_list.append(l[i])
	fin_list = groups_of_3(temp_list)
	
	hid.write(str(width) + " ")
	hid.write(str(height) + "\n")
	hid.write("255\n")


	scale_values = []
	for i in range(0, height):
		for j in range(0, width):
			dist = sqrt((col - j)**2 + (row - i)**2)
			scale = (radius - dist)/radius
			if scale < 0.2:
				scale = .2
			scale_values.append(scale)
	
	final = []
	for i in range(len(fin_list)):
		r = float(fin_list[i][0]) * scale_values[i]
		g = float(fin_list[i][1]) * scale_values[i]
		b = float(fin_list[i][2]) * scale_values[i]
		final.append([int(r), int(g), int(b)])

	for colors in final:
		hid.write(str(colors[0]) + " " + str(colors[1]) + " "+ str(colors[2]) + "\n")
	
	f.close()
	hid.close()

if __name__ == '__main__':
	fade()


