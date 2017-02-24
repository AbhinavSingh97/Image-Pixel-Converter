#This is blur
from sys import *
from groups import *

def blur():
	try:
		f = open(argv[1], "r")
	except:
		print "Error: File could not be opened"
		exit()

	try:
		neighbor_reach = int(argv[2])
	except:
		neighbor_reach = 4

	temp_list = []
	count = 0
		
	for line in f:
		l = line.split()
		count += 1
			
		for i in range(len(l)):
				if count < 4:
					if count == 2:
						width = int(l[0])
						height = int(l[1])
					else:
						pass
					
				else:
					temp_list.append(l[i])
		
	hid = open("blurred.ppm", "w")
	hid.write("P3\n")
	hid.write(str(width) + " ")
	hid.write(str(height) + '\n')
	hid.write("255\n")

					
	list_of_three = groups_of_3(temp_list)
	pts_and_colors = {}
	a = 0

	for i in range(height):
		for j in range(width):
			pts_and_colors[(j, i)] = list_of_three[a]
			a += 1
		

	for y in range(0, height):
		for x in range(0, width):
			points = []
			pts = []
			r = 0
			g = 0
			b = 0
			index = 0
			for x_pt in range(x - neighbor_reach, x + neighbor_reach):
				for y_pt in range(y - neighbor_reach, y + neighbor_reach):
					if x_pt > width - 1  or x_pt < 0:
						pass
					elif y_pt > height - 1  or y_pt < 0:
						pass
					else:
						index += 1
						points.append((x_pt, y_pt))
			

			for i in points:
				pts.append(pts_and_colors[i])

			for j in pts:
				r += float(j[0])
				g += float(j[1])
				b += float(j[2])

			r_avg = int(float(r)/index)
			g_avg = int(float(g)/index)
			b_avg = int(float(b)/index)
	
			hid.write(str(r_avg) + " "+ str(g_avg) + " " + str(b_avg) + '\n')
				
				

		
	f.close()
	hid.close()
if __name__ == "__main__":
	blur()