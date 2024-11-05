def read_assembly_file_to_list(file_path):
    # Initialize an empty list to store lines of the assembly file
    lines_list = []
    
    # Open the .as file in read mode
    try:
        with open(file_path, 'r') as file:
            # Read each line from the file
            for line in file:
                # Strip leading/trailing whitespace and add to the list
                stripped_line = line.strip()

                if not stripped_line.startswith('#') and stripped_line:
                    lines_list.append(stripped_line)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except IOError:
        print(f"Error: An I/O error occurred while reading the file '{file_path}'.")

    return lines_list

# Convert an integer to binary string using bin()
def binary_str(int_string) -> str:
    num = int(int_string)
    return bin(num)[2:]  # Remove the '0b' prefix

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index of the found element
    return -1  # Return -1 if the element is not found

# Usage
file_path = 'program.as'  # Replace with the path to your .as file
lines = read_assembly_file_to_list(file_path)

opcodeStrings = ['nop', 'hlt', 'add', 'sub', 'bit', 'bnt', 'inc', 'dec', 'rsh', 'ldi', 'mst', 'mld', 'jmp', 'cjp', 'pst', 'pld']

currentAddress = -1
jumpLabels = []
jumpAddesses = []



for line in lines:
    if line[:1] == '.':
        jumpLabels.append(line)
        jumpAddesses.append(currentAddress + 1)
    else:
        currentAddress += 1

#num = 0
for line in lines:
    if line[:1] != '.':
        binaryInstruction = ''
        tokens = line.split()
        opcodeStr = tokens[0]
        opcode = linear_search(opcodeStrings,opcodeStr)
        binaryInstruction += f'{opcode:04b}' 

        if opcode in (0, 1, 10, 12, 13, 14):
            pass
        else:
            regDestStr = tokens[1]
            regDestInt = int(regDestStr[1:])
            binaryInstruction += f'{regDestInt:03b}'
            binaryInstruction += '0'

        print(binaryInstruction)
        with open("machine_code.txt", "a") as file:
            file.write(binaryInstruction)
        #num += 1

print(jumpAddesses)
print(jumpLabels)



# Define Instructions
def NOP():
    pass
def HLT():
    pass
def ADD():
    pass
def SUB():
    pass
def BIT():
    pass
def BNT():
    pass
def INC():
    pass
def DEC():
    pass
def RSH():
    pass
def LDI():
    pass
def MST():
    pass
def MLD():
    pass
def JMP():
    pass
def CJP():
    pass
def PST():
    pass
def PLD():
    pass
# Create an array of Instructions
functions = [NOP, HLT, ADD, SUB, BIT, BNT, INC, DEC, RSH, LDI, MST, MLD, JMP, CJP, PST, PLD]

# Call a function based on opcode
def assembleInstruction(number):
    if 0 <= number < len(functions):
        return functions[number]()
    else:
        return "Invalid function number"
