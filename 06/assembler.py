

import sys
inputFileName = sys.argv[1]

def parser():
    command_list = []

    asmFile = open(inputFileName + ".asm", "r")
    hackfile = open(inputFileName + ".hack", "w")

    for line in asmFile:
        cleanedLine = cleanup(line)
        if cleanedLine != "":
            hackfile.write(cleanedLine + "\n")
    
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

parser()