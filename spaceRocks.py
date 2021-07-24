print("Artemis Rover Rock Scanner Starting")

'''We are looking for the following rocks: Basalt: 
The Mare Rocks: Breccia: Shocked Rock, Highland Rock: 
Anorthosite, Regolith Soil/Surface Layer.
These are the four main types of rocks found on the moon'''

basalt = 0
breccia = 0
highland = 0
regolith = 0
rockList = []

'''We are creating a file called rocks and writing a list of rocks to tht file'''

strPath = "rocks.txt"
fileObject = open(strPath, "w")
fileObject.writelines(["Reading Rocks\n","basalt\n","breccia\n","highland\n","regolith\n","highland\n","breccia\n","highland\n","regolith\n","regolith\n","basalt\n","highland\n","basalt\n","breccia\n","breccia\n","regolith\n","breccia\n","highland\n","highland\n","breccia\n","basalt\n"])
fileObject.close()

'''We will read the fle and print the first line'''

strPath = "rocks.txt"
fileObject = open(strPath)
line = fileObject.readline()
print(line)

'''we can call the readlines() function to put all of the lines into our rockList variable. 
We'll also print all of the rocks that are in the rockList and close the fileObject.'''

rockList = fileObject.readlines()

for rock in rockList:
    print(rock)

fileObject.close()

'''We will now look at the list of rocks, 
work out which type of rock it is and add it to the list incrementally'''

def countMoonRocks(rockToID):
    global basalt
    global breccia
    global highland
    global regolith

    rockToID = rockToID.lower()

    if("basalt" in rockToID):
        print("Found a basalt\n")
        basalt += 1

    #TODO Add else if statements for breccia, highland and regolith

    elif("breccia" in rockToID):
        print("Found a breccia\n")
        breccia += 1
    elif("highland" in rockToID):
        print("Found a highland\n")
        highland += 1
    elif("regolith" in rockToID):
        print("Found a regolith\n")
        regolith += 1

    return

'''We will call the function.'''

for rock in rockList:
    countMoonRocks(rock)

'''Print the number of rocks'''

print("Number of Basalt: ", basalt) 

print("Number of Basalt: ", basalt)
print("Number of Breccia: ", breccia)
print("Number of Highland: ", highland)
print("Number of Regolith: ", regolith)

print("The max number of one type of rock found was:", max(basalt, breccia, highland,regolith))
print("The minimum number of one type of rock found was:", min(basalt, breccia, highland, regolith))