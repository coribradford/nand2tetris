


"""parser"""
#need to start reading a file with a given name 
    #eg constructor for a parser object (class?) that accepts a string specififying a file name
    #need to know how to read text files
#need to move to the next line each time - are we finished? boolean has more command
#get the next command - void advance
#need to read one line at a time
    #need to skip whitespace including comments
#get the fields of the current command
    #a command, c command, labels
    #easy access to the fields(where things will go)
    #string dest(), string comp(), string jump(), string label() - methods in a class?
#translate from mnemonic to binary syntax following the formula - hash table with commands?

"""Handling symbols"""
#construct empty hash table (symbol table)
#add predefined symbol
#first pass - scan the entire program
# for each instruction in the form of (XXX)
    #add the pair, (XXX, address) to the symbol table, where address is the number of the instruction following the label
#second pass - 
#set n to 16, because registers for variables begin at 16
#scan the entire program again for variables (@symbol)
    #if the instruction is @symbol, look up the symbol in the table
        # if it exists, use the value to complete the translation into decimal
        #if not, add @n to the table, complete the translataion, and 
        # n++
#if its a C-instruction, complete its translation
#write the translated instruction to the output file



    #if line starts with @, its an a instruction
    #if the character after the @ is a number, its already in decimal, otherwise it needs to be run through the symbol table
    #try catch block^
        #goto a instruction function
    #elif it starts with open parenthesis its a label, ie (LOOP)
        #goto label function
    #else, its a c instruction
        #goto c instruction function


    #def a instruction function, take input in number (location):
        #output beginning with 0 for a instructiuon
        #calculate 15 bit number in binary
        #return 16 bit location starting with 0

    #def loop instruction:
        #symbols? come back to

    #def c instructions, input instruction:
        #break them into separate strings at the equals and the semicolon (if they exist)
        #if no equals, do something (000)
        #if no semicolon, do something else (000)
        #begin with 111
        #111aCCCCCCDDDJJJ


#whitespace - regular instructions - regex - string operations

###need a readme!!!

