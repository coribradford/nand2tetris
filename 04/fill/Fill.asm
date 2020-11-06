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
    @0
    M=D     //grab screen address and store in ram0 for easier incrementing

(KEYS)
    @KBD
    D=M
    @BLACK
    D;JGT   //if d is greater than zero some key is pressed, proceed to black
    @WHITE
    D;JEQ   //if d is zero no keys are pressed, proceed to white

(BLACK)
    @1      //hold fill value in register 1
    M=-1    //determines fill val based on earlier jump condition
    @FILL
    0;JMP   //unconditionally jump to fill

(WHITE)
    @1      //again, holds fill value in register 1
    M=0     //determines fill val based on earlier jump condition
    @FILL
    0;JMP   //unconditionally jump to fill again

(FILL)
    @1      //check register 1 which is holding color instructions
    D=M     //grab instruction and hold in d
    @0      //grab screen address
    A=M     //go there
    M=D     //fill pixel based on instruction
    @0      //go back to register 0 holding screen address
    D=M+1   //increment by 1 pixel but in data register
    @KBD    //go to keyboard
    D=A-D   //store value for check for end of loop; 
            //keyboard addresses start at end of screen addresses
    @0      //back to register holding screen address
    M=M+1   //increment stored screen address by 1 pixel
    A=M     //goto that address
    @FILL   //restart loop if incremented pixel value stored in data register doesnt
    D;JGT   //exceed screen addresses

    @TOP
    0;JMP  //always restart loop


