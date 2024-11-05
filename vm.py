from array import array

instructionMem = []

def read_file_to_16bit_array(file_path, chunk_size=16):
    # Initialize an empty list to store the 16-bit integers
    instructionArr = []
    
    # Open the file in read mode
    with open(file_path, 'r') as file:
        # Read the entire content of the file
        #content = file.read().strip()  # Remove any extra whitespace
        content = file.read().replace('\n', '').strip()
        
        # Split content into chunks of specified size
        for i in range(0, len(content), chunk_size):
            chunk = content[i:i + chunk_size]
            
            # Check if the chunk has exactly 16 bits
            if len(chunk) == chunk_size:
                # Convert the 16-bit binary chunk to an integer and add to the array
                instructionArr.append(int(chunk, 2))
    
    return instructionArr

file_path = 'machine_code.txt'  # Replace with the path to your text file
instructionMem = read_file_to_16bit_array(file_path)

dataMem = []

halt = False
programCounter = 0

flagsArray = [False,True,False,True,False,True,False,True]

registers = array('B', [0] * 8)

registers[1] = 3
registers[2] = 5

ioPorts = array('B', [0] * 8)

# Define Instructions
def NOP():
    pass
def HLT():
    global halt
    halt = True
    print("Program stopped succesfully")
def ADD():
    registers[int(registerDest,2)] = (registers[int(registerA,2)] + registers[int(registerB,2)]) % 0x100
def SUB():
    registers[int(registerDest,2)] = (registers[int(registerA,2)] + (registers[int(registerB,2)]^0xFF)) % 0x100
def BIT():
    pass
def BNT():
    pass
def INC():
    registers[int(registerDest,2)] = registers[int(registerA,2)] + 1
def DEC():
    registers[int(registerDest,2)] = (registers[int(registerA,2)] + 0xFF) % 0x100
def RSH():
    registers[int(registerDest,2)] = registers[int(registerA,2)] >> 1
def LDI():
    registers[int(registerDest,2)] = int(immediate,2)
def MST():
    pass
def MLD():
    pass
def JMP():
    global programCounter
    programCounter = int(jumpAddress,2)
def CJP():
    global flagsArray
    global programCounter
    if flagsArray[condition] == True:
        programCounter = int(jumpAddress,2)
def PST():
    ioPorts[int(portAddress,2)] = registers[int(registerA,2)]
    print(ioPorts[0])
def PLD():
    registers[int(registerDest,2)] = ioPorts[int(portAddress,2)]
# Create an array of Instructions
functions = [NOP, HLT, ADD, SUB, BIT, BNT, INC, DEC, RSH, LDI, MST, MLD, JMP, CJP, PST, PLD]

# Call a function based on opcode
def excecuteInstr(number):
    if 0 <= number < len(functions):
        return functions[number]()
    else:
        return "Invalid function number"
    
def updateFlags(aluResult):
    global flagsArray
    if aluResult >= 128:
        negFlag = True
        flagsArray[0] = negFlag
    if aluResult == 0:
        zeroFlag = True
        flagsArray[2] = zeroFlag
    '''
    if aluResult == 0:
        zeroFlag = True
        flagsArray = zeroFlag
    if aluResult == 0:
        zeroFlag = True
        flagsArray = zeroFlag
    '''

while not halt:
    #global registerDest
    instrInt = instructionMem[programCounter]
    programCounter += 1

    instruction = f'{instrInt:016b}'
    opcodeStr = instruction[:4]
    opcode = int(opcodeStr, 2)
    operands = instruction[4:]

    registerDest = operands[:3]
    registerA = operands[4:7]
    registerB = operands[9:13]
    immediate = operands[4:]
    jumpAddress = operands[6:]
    condition = int(registerDest,2)
    portAddress = registerB

    #print(opcode)
    excecuteInstr(opcode)
    if(opcode < 9):
        updateFlags(registers[int(registerDest,2)])
