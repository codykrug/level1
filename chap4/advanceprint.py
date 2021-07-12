import json
import os
f = open('assign.py','w')
f.write(
'''def f(x):
    return r"['7:30'],"*x

def allot(num):
    print r"allotments = ("
    print f(num)
    print r")"
    return None

allot(8)''')
f.close()
os.system("python assign.py > assignments.py")

execfile("assignments.py")

g = open("format.py", 'w')
g.write(
'''def multiple(time):
    for i in range(time):
        print "worksheet.set_row(" + str(i) + ",30)"

multiple(8)''')
g.close()
os.system("python format.py > formats.py")


import xlsxwriter

# Create a workbook and add a worksheet.
workbook = xlsxwriter.Workbook('fakeallotments.xlsx')
cell_format = workbook.add_format()
cell_format.set_border()
worksheet = workbook.add_worksheet()
worksheet.set_landscape()
#worksheet.set_header('&LCiao&CBello&RCielo')
worksheet.print_area('A1:I10') #make printable area
worksheet.fit_to_pages(1, 1) #ensure fit to page zoom
#necessary for merge format
merge_format = workbook.add_format({'align': 'center'})
worksheet.merge_range('A1:I1', 'Tour Allotments', merge_format)

worksheet.set_column(0, 0, 10)  # Width of columns B:D set to 30.
worksheet.set_column(1, 1, 30)  # Width of columns B:D set to 30.
worksheet.set_column(2, 6, 10)  # Width of columns B:D set to 30.
worksheet.set_column(7, 7, 30)  # Width of columns B:D set to 30.
worksheet.set_column(8, 8, 10)  # Width of columns B:D set to 30.

execfile("formats.py")

worksheet.write('A2', 'Confirm?')
worksheet.write('B2', 'Time') 
worksheet.write('C2', 'Name') 
worksheet.write('D2', 'Room #') 
worksheet.write('E2', 'Code') 
worksheet.write('F2', 'H/W') 
worksheet.write('G2', 'C/I') 
worksheet.write('H2', 'C/O') 
worksheet.write('I2', 'Comments') 
worksheet.write('J2', 'GEN ID') 

# Start from the first cell. Rows and columns are zero indexed.
row = 3
col = 1

# Iterate over the data and write it out row by row.
for item, in (allotments):
    worksheet.write(row, col ,     item)
    #worksheet.write(row, col + 1, cost)
    row += 1



# Write a total using a formula.
worksheet.write(row, 0, 'Total')
#worksheet.write(row, 1, '=SUM(B1:B4)')

workbook.close()

