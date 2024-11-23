from array import array

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

dataMem = [0] * 32

halt = False
programCounter = 0

flagsArray = [False,True,False,True,False,True,False,True]

registers = array('B', [0] * 8)

ioPorts = array('B', [0] * 8)

# Define Instructions
def nop(operands):
    pass
def hlt(operands):
    global halt
    halt = True
    print("Program stopped succesfully")
def add(operands):
    registerDest = operands[:3]
    registerA = operands[4:7]
    registerB = operands[9:13]
    registers[int(registerDest,2)] = (registers[int(registerA,2)] + registers[int(registerB,2)]) % 0x100
def sub(operands):
    registerDest = operands[:3]
    registerA = operands[4:7]
    registerB = operands[9:13]
    result = (registers[int(registerA,2)] + (registers[int(registerB,2)]^0xFF))
    registers[int(registerDest,2)] = (result + 1)  % 0x100
def bit(operands):
    registerDest = operands[:3]
    registerA = operands[4:7]
    registerB = operands[9:13]
    type = int(operands[7:9],2)
    
    if type == 0:
        registers[int(registerDest,2)] = (registers[int(registerA,2)] | registers[int(registerB,2)]) % 0x100
    elif type == 1:
        registers[int(registerDest,2)] = (registers[int(registerA,2)] & registers[int(registerB,2)]) % 0x100
    else:
        registers[int(registerDest,2)] = (registers[int(registerA,2)] ^ registers[int(registerB,2)]) % 0x100
    
def bnt(operands):
    registerDest = operands[:3]
    registerA = operands[4:7]
    registerB = operands[9:13]
    type = int(operands[7:9],2)
    if type == 0:
        registers[int(registerDest,2)] = (~(registers[int(registerA,2)] | registers[int(registerB,2)])) & 0xFF
    elif type == 1:
        registers[int(registerDest,2)] = (~(registers[int(registerA,2)] & registers[int(registerB,2)])) & 0xFF
    else:
        registers[int(registerDest,2)] = (~(registers[int(registerA,2)] ^ registers[int(registerB,2)])) & 0xFF
    
def inc(operands):
    registerDest = operands[:3]
    registerA = operands[4:7]
    result = registers[int(registerA,2)] + 1
    registers[int(registerDest,2)] = result % 0x100
    #print(result)
def dec(operands):
    registerDest = operands[:3]
    registerA = operands[4:7]
    registers[int(registerDest,2)] = (registers[int(registerA,2)] + 0xFF) % 0x100
def rsh(operands):
    registerDest = operands[:3]
    registerA = operands[4:7]
    registers[int(registerDest,2)] = registers[int(registerA,2)] >> 1
def ldi(operands):
    registerDest = operands[:3]
    immediate = operands[4:]
    registers[int(registerDest,2)] = int(immediate,2)
def mst(operands):
    global dataMem
    registerA = operands[4:7]
    dataMem[registers[7]] = registers[int(registerA,2)]
def mld(operands):
    global dataMem
    registerDest = operands[:3]
    registers[int(registerDest,2)] = dataMem[registers[7]] 
def jmp(operands):
    global programCounter
    jumpAddress = operands[6:]
    programCounter = int(jumpAddress,2)
def cjp(operands):
    global flagsArray
    global programCounter
    condition = int(operands[:3],2)
    jumpAddress = operands[6:]
    if flagsArray[condition] == True:
        programCounter = int(jumpAddress,2)
def pst(operands):
    portAddress = operands[9:13]
    registerA = operands[4:7]
    ioPorts[int(portAddress,2)] = registers[int(registerA,2)]
    print(ioPorts[7])
def pld(operands):
    registerDest = operands[:3]
    portAddress = operands[9:13]
    portInput = input(f"Enter input for port {int(portAddress,2)}: ")
    ioPorts[int(portAddress,2)] = int(portInput)
    registers[int(registerDest,2)] = ioPorts[int(portAddress,2)]

opcodeFunctions = [nop, hlt, add, sub, bit, bnt, inc, dec, rsh, ldi, mst, mld, jmp, cjp, pst, pld]

# Call a function based on opcode
def excecuteInstr(opcode,operands):
    if 0 <= opcode < len(opcodeFunctions):
        return opcodeFunctions[opcode](operands)
    else:
        return "Invalid function number"
    
def updateFlags(aluResult):
    global flagsArray
    flagsArray = [False,True,False,True,False,True,False,True]
    if aluResult >= 128:
        negFlag = True
        flagsArray[0] = negFlag
        flagsArray[1] = False
    if aluResult == 0:
        zeroFlag = True
        flagsArray[2] = zeroFlag
        flagsArray[3] = False
    '''
    if aluResult == 0:
        zeroFlag = True
        flagsArray = zeroFlag
    if aluResult == 0:
        zeroFlag = True
        flagsArray = zeroFlag
    '''
def run(machine_code_file):
    instructionMem = []
    instructionMem = read_file_to_16bit_array(machine_code_file)

    while not halt:
        global programCounter
        instrInt = instructionMem[programCounter]
        programCounter += 1

        instruction = f'{instrInt:016b}'
        opcodeStr = instruction[:4]
        opcode = int(opcodeStr, 2)
        operands = instruction[4:]
        
        registerDest = operands[:3]
        
        #print(opcode)
        registers[0] = 0
        excecuteInstr(opcode,operands)
        if(opcode < 9):
            updateFlags(registers[int(registerDest,2)])
            #print(list(flagsArray))
    print(list(dataMem))
    print(list(registers))
def resetEmulator():
    global halt
    halt = False

    global programCounter
    programCounter = 0

    global flagsArray
    flagsArray = [False,True,False,True,False,True,False,True]
    global ioPorts
    global registers
    registers = array('B', [0] * 8)
    ioPorts = array('B', [0] * 8)



