

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
    command_list = []

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
    # tempFile = open(inputFileName + ".tmp", "r")
    # temp2File = open(inputFileName + "1.tmp", "w")
    global linenumber
    # for line in tempFile:
    if line[0] == "(":
        label = line[1:-1]
        symbols[label] = linenumber
    else:
        linenumber += 1
        return line
    # tempFile.close()
    # temp2File.close()


# def secondPass():
#     variablenumber = 16
#     tempFile = open(inputFileName + "1.tmp", "r")
#     tempFile2 = open(inputFileName + "2.tmp", "w")
#     for line in tempFile:
#         if line[0] == "@":
#             if line[1].isalpha():
#                 label = line[1:-1]
#                 value = symbols.get(label, -1)
#                 if value == -1:
#                     value = symbols[label] = variablenumber
#                     variablenumber += 1
#             else:
#                 value = int(line[1:])
#             returnvalue = bin(value)[2:].zfill(16)
#         tempFile2.write(line)
#         tempFile.close()
#         tempFile2.close()

def performPasses():
    tempFile = open(inputFileName + ".tmp", "r")
    temp2File = open(inputFileName + "1.tmp", "w")
    for line in tempFile:
        firstPass(line)
        temp2File.write(line)



parser()
performPasses()
# firstPass()
# secondPass()