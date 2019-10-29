import time

def printLine(iteration,line):
    print("")
    print(str(iteration)+")"+line)

def createNewLine(line):
    newLine = ""
    key = int(line[0])
    count = 0

    for i in range(len(line)):
        curNumber = int(line[i])
        if curNumber == key:
            count += 1
        else:
            newLine = newLine+str(count)+str(key)
            key = curNumber
            count = 1

    newLine = newLine+str(count)+str(key)
    return newLine

def specificLine(line,lineNum):
    for i in range(lineNum):
        line = createNewLine(line)
    printLine(i+1,line)

def cleanRun(line,iterations):
    for k in range(iterations+1):
        printLine(k,line)
        line = createNewLine(line)

def menu():
    print(chr(27) + "[2J")
    choice = str(input("Temporary torment(T) Eternal torment(E): "))
    
    if choice in ['t',"T"]:
        while 1:
            line = str(input("Starting input: "))
            if line == "b":
                menu()
            lineNum = int(input("Line Number: "))
            start = time.time()
            specificLine(line,lineNum)
            end = time.time()
            print(end-start)
    else:
        while 1:
            line = str(input("Starting input: "))
            if line == "b":
                menu()
            iterations = int(input("Iterations?: "))
            cleanRun(line,iterations)

menu()
