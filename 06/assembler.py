



import re, sys
inputFile = sys.argv[1]
def assembler():
    command_list = []

    
    asmFile = open(inputFile + ".asm", "r")
    hackfile = open(inputFile + ".hack", "w")

    for line in asmFile:
        hackfile.write(cleanup(line))
    
    asmFile.close()
    hackfile.close()






def cleanup(fileLine):
    firstCharacter = fileLine[0]
    if firstCharacter == "\n" or firstCharacter == "/":
        return ""
    elif firstCharacter == " ":
        return cleanup(fileLine[1:])
    else:
        return firstCharacter + cleanup(fileLine[1:])

assembler()