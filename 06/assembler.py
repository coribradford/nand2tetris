





import re, sys

def assembler():
    command_list = []

    root = sys.argv[1]
    asmFile = open(root + ".asm", "r")
    hackfile = open(root + ".hack", "w")

    for line in asmFile:
        hackfile.write("ah"+"\n")
    
    asmFile.close()
    hackfile.close()

assembler()
    # for command in asmFile:
    #     newline=re.sub(r'\/+.*\n|\n| *','',command)
    #     if newline!='':
    #         command_list.append(newline)

    # asmFile.close()


    # hackFile = open(f+'.hack','w')
    # hackFile.write("AHHH")
    # hackFile.close()