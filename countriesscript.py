#Script to generate a list of countries that are of similar size
import arcpy

#Set workspace and import source file
arcpy.env.workspace = r'data/World.gdb/'
worldfile = r'data/World.gdb/Borders'

#Create unique name for output file in workspace
name = arcpy.CreateUniqueName('Borders', arcpy.env.workspace)

#Sort countries by area size
arcpy.management.Sort('Borders', name, [['AREA', 'Descending']] )
cursor = arcpy.da.SearchCursor(name, ['NAME', 'AREA'])

#Put values in a list
values = []
for row in cursor:
    values.append(float(row[1]))
print values

#Put values with country names in a dictionary
dic = {}
for row in cursor:
    print 'work'
    print row[0], row[1]
    dic[row[0]] = row[1]

winners = []

#Loop to get a value and its next value
for item in values:
    next_item = values[values.index(item) + 1]
    if (item / next_item) <= 1.001:
        winners.append(item)
        winners.append(next_item)
    if item <= 100:
        print 'End'
        break

print winners

