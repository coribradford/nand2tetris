

import sys


inputFileName = sys.argv[1]
if "." in inputFileName:
    asm = ".asm"
    if asm in inputFileName:
        inputFileName = inputFileName.replace(".asm", "")
    else:
        raise ValueError("Please input the correct .asm file type.")


symbols={'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576,
         'R0':0,'R1':1,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,
         'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15}


linenumber = 0
variablenumber = 16


def parser():
    asmFile = open(inputFileName + ".asm", "r")
    tempFile = open(inputFileName + ".tmp", "w")

    for line in asmFile:
        cleanedLine = cleanup(line)
        if cleanedLine != "":
            tempFile.write(cleanedLine + "\n")
    
    asmFile.close()
    tempFile.close()


def cleanup(fileLine):
    firstCharacter = fileLine[0]
    if firstCharacter == "\n" or firstCharacter == "/":
        return ""
    elif firstCharacter == " ":
        return cleanup(fileLine[1:])
    else:
        return firstCharacter + cleanup(fileLine[1:])


def firstPass(line):
    global linenumber
    if line[0] == "(":
        label = line[1:-1]
        symbols[label] = linenumber 
    else:
        linenumber += 1
        return line


def secondPass(line):
    if line[0] == "@":
        return a_instruction(line)
    else:
        return c_instruction(line)


def a_instruction(line):
    global variablenumber
    if line[1].isalpha():
        label = line[1:-1]
        value = symbols.get(label, -1)
        if value == -1:
            value = a_instruction_prep(label)
    else:
        value = int(line[1:])
    newvalue = bin(value)[2:].zfill(16)
    return newvalue


def a_instruction_prep(label):
    global variablenumber
    symbols[label] = variablenumber
    variablenumber += 1
    return symbols[label]

def c_instruction(line):
    line = c_instruction_prep(line)
    print(line)
    destSplit = line.split("=")
    #perform grab from table for dest; build table
    jumpSplit = destSplit.split(";")
    #perform grab from table for comp and jump
    #return stitched new line

def c_instruction_prep(line):
    if "=" not in line:
        line = " ="+line
    if ";" not in line:
        line = line + "; "
    return line


def performPasses():
    tempFile = open(inputFileName + ".tmp", "r")
    temp2File = open(inputFileName + "1.tmp", "w")
    for line in tempFile:
        firstpassLine = firstPass(line)
        secondpassLine = secondPass(firstpassLine)
        temp2File.write(secondpassLine)
    tempFile.close()
    temp2File.close()



parser()
performPasses()
