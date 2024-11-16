def read_assembly_file_to_list(file_path):
    # Initialize an empty list to store lines of the assembly file
    lines_list = []
    
    # Open the .as file in read mode
    try:
        with open(file_path, 'r') as file:
            # Read each line from the file
            for line in file:
                # Strip leading/trailing whitespace and add to the list
                stripped_line = line.lstrip().rstrip()

                if not stripped_line.startswith('#') and stripped_line:
                    lines_list.append(stripped_line)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while reading the file '{file_path}'.")

    return lines_list

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index of the found element
    print("Not found")
    return -1  # Return -1 if the element is not found
#def findJumpAddress():

# Usage
def assemble(file_path, output_file):
    with open(output_file, "w") as file:
                file.write('')
    lines = read_assembly_file_to_list(file_path)

    opcodeStrings = ['nop', 'hlt', 'add', 'sub', 'bit', 'bnt', 'inc', 'dec', 'rsh', 'ldi', 'mst', 'mld', 'jmp', 'cjp', 'pst', 'pld']
    flagLabels = ['msb','!msb', 'zero', '!zero','sss','sss','sss','sss']

    currentAddress = -1
    jumpLabels = []
    jumpAddresses = []

    for line in lines:
        if line[:1] == '.':
            jumpLabels.append(line)
            jumpAddresses.append(currentAddress + 1)
        else:
            currentAddress += 1

    #missing instructions: MST MLD BIT BNT
    #PLD not tested yet
    #loading negative immediates not tested yet
    for line in lines:
        if line[:1] != '.':
            binaryInstruction = ''
            tokens = line.split()
            #print(list(tokens))
            opcodeStr = tokens[0]
            opcode = linear_search(opcodeStrings,opcodeStr)
            binaryInstruction += f'{opcode:04b}' 

            if opcode in (0, 1, 10, 12, 13, 14):
                if opcode < 2:
                    binaryInstruction += '000000000000'
                if opcode == 12:
                    jumpLabel = tokens[1]
                    jumpLabelIndex = linear_search(jumpLabels, jumpLabel)
                    jumpAddress = jumpAddresses[jumpLabelIndex]
                    binaryInstruction += '0000'
                    binaryInstruction += f'{jumpAddress:08b}'
                if opcode == 13:
                    flagLabel = tokens[1]
                    flagLabelIndex = linear_search(flagLabels, flagLabel)
                    binaryInstruction += f'{flagLabelIndex:03b}'
                    binaryInstruction += '0'

                    jumpLabel = tokens[2]
                    jumpLabelIndex = linear_search(jumpLabels, jumpLabel)
                    jumpAddress = jumpAddresses[jumpLabelIndex]
                    binaryInstruction += f'{jumpAddress:08b}'
                if opcode == 14:
                    binaryInstruction += '0000'
                    regAStr = tokens[1]
                    regAInt = int(regAStr[1:])
                    binaryInstruction += f'{regAInt:03b}'
                    portAddressStr = tokens[2]
                    portAddress = int(portAddressStr[1:])
                    binaryInstruction += f'{portAddress:05b}'
            else:
                regDestStr = tokens[1]
                regDestInt = int(regDestStr[1:])
                binaryInstruction += f'{regDestInt:03b}'
                binaryInstruction += '0'
                if opcode > 1 and opcode < 9:
                    regAStr = tokens[2]
                    regAInt = int(regAStr[1:])
                    binaryInstruction += f'{regAInt:03b}'
                    if opcode == 4 or opcode == 5:
                        pass
                    elif opcode == 2 or opcode == 3:
                        binaryInstruction += '00'
                        regBStr = tokens[3]
                        regBInt = int(regBStr[1:])
                        binaryInstruction += f'{regBInt:03b}'
                    else:
                        binaryInstruction += '00000'

                if opcode == 9:
                    immediateStr = tokens[2]
                    immediateInt = int(immediateStr)
                    binaryInstruction += f'{immediateInt:08b}'
                if opcode == 15:
                    portAddressStr = tokens[2]
                    portAddress = int(portAddressStr[1:])
                    binaryInstruction += f'{portAddress:08b}'
        
            print(binaryInstruction)
            with open(output_file, "a") as file:
                file.write(binaryInstruction)
    print('Succesfully Assembled ' + f'{currentAddress + 1}' + ' Instructions')
#print(jumpAddresses)
#print(jumpLabels)
