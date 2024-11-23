ldi r5 10
ldi r6 11
ldi r7 0
jmp .clear_registers
.clear_registers_end
pst r2 p7
.wait_for_input
    pld r1 p0
    sub r0 r1 r5
    cjp zero .wait_for_input
sub r0 r1 r6
cjp zero .store_num
ldi r6 12
sub r0 r1 r6
ldi r6 11
cjp zero .done
jmp .input_next_digit
#Functions
#Multiplies value in r2 by 10 and stores it in r4
.mult_ten
    add r4 r2 r2
    add r2 r2 r2
    add r2 r2 r2
    add r2 r2 r2
    add r4 r4 r2
    jmp .mult_ten_end
.input_next_digit
    #Store Newest/Rightmost digit in r3
    add r3 r1 r0
    #Multiply previous num by 10 and store in r4
    jmp .mult_ten
    .mult_ten_end
    #Add values in r3 and r4 to append new digit, new num stored in r2
    add r2 r3 r4
    pst r2 p7
    nop
    jmp .wait_for_input
.clear_registers
    ldi r1 0
    ldi r2 0
    ldi r3 0
    ldi r4 0
    jmp .clear_registers_end
.store_num
    mst r2
    inc r7 r7
    jmp .clear_registers
.done
    hlt
