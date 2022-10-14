import arcpy
import math
class factors():
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def buffer(self):
        #define as a linear funciton of weight for the size of the buffer?
        return 0    
    def intersect(self):
        return 0
    def selfdefine(self):
        return 0
    
#class operations(factors):
    #Define each possible GIS operation/tool in this class derived from factors
    #instantiate an object for each operation done?
    #maybe better to just define inside of factors!
#    def __init__(self, factor, weight):
#        self.factor = factor
#        self.weight = weight

databasefile = input("Insert database file name\n")

print("Begin to input weights for the following factors:")
print("To disregard a factor, input a weight of 0")
print("To inversely correlate a factor, input a negative weight") #does this need to be done?
#More can be added any time!
print("Enter \"exit\" as factor name to exit data entry")
listfactors = []
while True:
    name = input("Enter Factor's name:\n>>>")
    print()
    if name == "exit":
        break
    weight = float(input("Enter Factor's weight:\n>>>"))
    print()
    listfactors.append(factors(name, weight))
for x in listfactors:
    while True:
        print("Enter the number for the geoprocessing tool for ", x.name, "data set")
        print("1) Buffer")
        print("2) Intersect")
        print("3) Self Defined Tool #1")
        print("Enter 0 To Exit")
        tool = int(input("\n>>>"))
        if tool == 0:
            break
        elif tool == 1:
            x.buffer()
        elif tool == 2:
            x.intersect()
        elif tool == 3:
            x.selfdefined()
        else:
            print("Invalid Tool, try again please")