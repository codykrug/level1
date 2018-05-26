''' reading files take effort
consoder the following file containing

the first line
the second line
the third line
'''

#requires two steps

'''
This takes the file and processes it through python
it takes each line and turns into an element in a list
'''

#make a empty list
lines = []

#use for loop to read line by line

for line in open('Inputfile.dat', 'r'): lines.append(line)


OutputFile = open('OutFile.out', 'w')
for n in range(0, len(lines)):
  outputFile.write(lines[n])

outputFile.close()



#you may not want to read each line into an elements.

InputFile = open("InputNumbers.dat", "r").read()
lines = InputFile.split("\n")

x = []
y = []
z = []

N = len(lines)

for n in range(0, N-1):
  row = lines[n].split()
  x.append(int(row[0]))
  y.append(int(row[1]))
  y.append(int(row[2]))


