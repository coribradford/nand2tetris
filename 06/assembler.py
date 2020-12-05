

import sys


inputFileName = sys.argv[1]
if "." in inputFileName:
    asm = ".asm"
    if asm in inputFileName:
        inputFileName = inputFileName.replace(".asm", "")
    else:
        raise ValueError("Please input the correct .asm file type.")

def parser():
    command_list = []

    asmFile = open(inputFileName + ".asm", "r")
    hackFile = open(inputFileName + ".hack", "w")

    for line in asmFile:
        cleanedLine = cleanup(line)
        if cleanedLine != "":
            hackFile.write(cleanedLine + "\n")
    
    asmFile.close()


def cleanup(fileLine):
    firstCharacter = fileLine[0]
    if firstCharacter == "\n" or firstCharacter == "/":
        return ""
    elif firstCharacter == " ":
        return cleanup(fileLine[1:])
    else:
        return firstCharacter + cleanup(fileLine[1:])

parser()