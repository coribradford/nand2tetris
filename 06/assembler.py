





import re, sys

def assembler(file):
    command_list = []

    f = sys.argv[1]
    asmFile = open(f+".asm", "r")

    for command in asmFile:
        newline=re.sub(r'\/+.*\n|\n| *','',command)
        if newline!='':
            command_list.append(newline)

    asmFile.close()


    hackFile = open(f+'.hack','w')
    hackFile.write("AHHH")
    hackFile.close()