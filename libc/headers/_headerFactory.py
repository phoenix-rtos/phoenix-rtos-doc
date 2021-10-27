import string

doMainReadme = True
doSubReadmes = True

file = open("headerFactory_list.txt","r")
l = file.readlines()
file.close()

alphalist = []
for h in l:
	hstrip = h.strip()
	alphalist.append(hstrip[2:])

alphalist.sort()


if doMainReadme is True:
	file = open("README.md", "w")
	lastchar = 0
	file.write("# Header files\n")
	for e in alphalist:
		if "/" in e:
			subs = e[:e.index("/")]
			aft = e[e.index("/"):]
			if lastchar != subs:
				lastchar = subs
				file.write('\n#### ' + lastchar + '/\n')
		else:
			if lastchar != e[0]:
				lastchar = e[0]
				file.write('\n## **' + lastchar + '**\n')

		file.write('[`' + e + '`](' + e[:-2] + '.md "'+ e +' functions list"), ')
	#file.write('\n</details>\n')
	file.close()

if doSubReadmes is True:
	for e in alphalist:
		filename = str(e[:-2]) + ".md"
		file = open(filename,"w")
		file.write("# " + e + "\n")
		file.write("This is generic page for header file `" + e + "`\n")
		file.write("# See also\n")

		
		if "/" in e:	# REMEMBER to change "See also" part in both scenarios (with '/' and without it!)
			file.write("1. [Header files](../README.md)\n")
			file.write("2. [Standard library](../../README.md)\n")
			file.write("3. [Table of Contents](../../../README.md)\n")
		else:			# REMEMBER to change "See also" part in both scenarios (with '/' and without it!)
			file.write("1. [Header files](README.md)\n")
			file.write("2. [Standard library](../README.md)\n")
			file.write("3. [Table of Contents](../../README.md)\n")
		file.close()
