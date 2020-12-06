

import sys, os


inputFileName = sys.argv[1]
if "." in inputFileName:
    asm = ".asm"
    if asm in inputFileName:
        inputFileName = inputFileName.replace(".asm", "")
    else:
        raise ValueError("Please input the correct .asm file type.")


symbolTable={'SP':0,'LCL':1,'ARG':2,'THIS':3,'THAT':4,'SCREEN':16384,'KBD':24576,
    'R0':0,'R1':1,'R1':1,'R2':2,'R3':3,'R4':4,'R5':5,'R6':6,'R7':7,
    'R8':8,'R9':9,'R10':10,'R11':11,'R12':12,'R13':13,'R14':14,'R15':15}

destTable={'':'000','M':'001','D':'010','MD':'011',
    'A':'100','AM':'101','AD':'110','AMD':'111'}
    
jumpTable={'':'000','JGT':'001','JEQ':'010','JGE':'011',
    'JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
    
compTable={'0':'0101010','1':'0111111','-1':'0111010','D':'0001100',
    'A':'0110000','M':'1110000','!D':'0001101','!A':'0110001',
    '!M':'1110001','-D':'0001111','-A':'0110011','-M':'1110011',
    'D+1':'0011111','A+1':'0110111','M+1':'1110111','D-1':'0001110',
    'A-1':'0110010','M-1':'1110010','D+A':'0000010','D+M':'1000010',
    'D-A':'0010011','D-M':'1010011','A-D':'0000111','M-D':'1000111',
    'D&A':'00000000','D&M':'1000000','D|A':'0010101','D|M':'1010101'}


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
        symbolTable[label] = linenumber 
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
    destSplit = line.split("=")
    dest = destTable.get(destSplit[0])
    jumpSplit = destSplit[1].split(";")
    comp = compTable.get(jumpSplit[0])
    jump = jumpTable.get(jumpSplit[1])
    c_inst = "111" + str(comp) + str(dest)+ str(jump)
    return c_inst


def c_instruction_prep(line):
    line = line[:-1]
    if "=" not in line:
        line = " ="+line
    if ";" not in line:
        line = line + "; "
    return line


def performPasses():
    tempFile = open(inputFileName + ".tmp", "r")
    hackFile = open(inputFileName + ".hack", "w")
    for line in tempFile:
        firstpassLine = firstPass(line)
        secondpassLine = secondPass(firstpassLine)
        hackFile.write(secondpassLine + "\n")
    tempFile.close()
    os.remove(inputFileName + ".tmp")
    hackFile.close()


parser()
performPasses()

