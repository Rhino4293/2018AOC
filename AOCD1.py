import itertools

#cwd = os.getcwd()
def getData(filename):
    with open(filename,"r") as files:
        return (files.readlines())

def getPart1(data):
    return(sum(data))

def getPart2(data):
    doubleNotFound =True
    frequency = set()
    Csum = 0
    while doubleNotFound:
        for feq in itertools.cycle(data):
            Csum += feq           
            if Csum in frequency:
                return Csum
            frequency.add(Csum)

            

inputData = map(int, getData("AOCD1input.txt"))
#print("Part 1: ", getPart1(inputData))
print("PArt 2: ",  getPart2(inputData))