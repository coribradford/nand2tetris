// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

(TOP)
    @SCREEN
    D=A
    @screenaddress
    M=D             //grab first screen address and store in a temp register for easier incrementing

(KEYS)
    @KBD
    D=M
    @BLACK
    D;JGT           //if d is greater than zero some key is pressed, proceed to black
    @WHITE
    D;JEQ           //if d is zero no keys are pressed, proceed to white

(BLACK)
    @instruction    //hold fill value in temp register
    M=-1            //determines fill val based on earlier jump condition
    @FILL
    0;JMP           //unconditionally jump to fill

(WHITE)
    @instruction    //again, holds fill value in temp register
    M=0             //determines fill val based on earlier jump condition
    @FILL
    0;JMP           //unconditionally jump to fill again

(FILL)
    @instruction    //check temp register which is holding color instructions
    D=M             //grab instruction and hold in d
    @screenaddress  //grab screen address
    A=M             //go there
    M=D             //fill pixel based on instruction
    @screenaddress  //go back to temp register holding screen address
    D=M+1           //increment by 1 pixel but in data register
    @KBD            //go to keyboard
    D=A-D           //store value for check for end of loop; 
                    //keyboard addresses start at end of screen addresses
    @screenaddress  //back to register holding screen address
    M=M+1           //increment stored screen address by 1 pixel
    A=M             //goto that address
    @FILL           //restart loop if incremented pixel value stored in data register doesnt
    D;JGT           //exceed screen addresses

    @TOP
    0;JMP           //always restart loop


