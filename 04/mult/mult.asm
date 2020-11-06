// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

    @R2
    M=0     // zero out end value

    @R1
    D=M     // grab value from register 1
    @n
    M=D     //set n variable to register 1 value for comparison
    @i
    M=1     //set i for count
    @sum
    M=0     //initialize sum

    @R0     // check the first register
    D = M 
    @STOP   //if zero jump to STOP
    D;JEQ

    @R1     // check the second register
    D = M 
    @STOP   //if zero jump to STOP
    D;JEQ

(LOOP)
    @i
    D=M
    @n
    D=D-M
    @STOP
    D;JGT   //if i>n goto STOP

    @sum
    D=M     //grab value from sum
    @R0 
    D = D+M //add to R0 value
    @sum
    M=D     //store sum

    @i
    M=M+1
    @LOOP
    0;JMP   //increment i and jump to LOOP

(STOP)
    @sum
    D=M
    @R2
    M=D     //puts sum value in R2

(END)
    @LOOP
    0;JMP   //end