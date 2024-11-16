import mcschematic

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
                instructionArr.append(chunk)
    
    return instructionArr
def create_schematic(machine_code_file):
    schem = mcschematic.MCSchematic()
    instructions = read_file_to_16bit_array(machine_code_file)
    block = 'minecraft:barrel{Items:[{Slot:0,id:redstone,Count:1}]}'
    instructionNum = 0
    secondBytesDistance = 17
    firstBytesDistance = 32

    for instruction in instructions:
        byte1 = instruction[:8]
        byte2 = instruction[8:]
        currentBit = 0
        for bit in byte1:
            if bit == '1':
                schem.setBlock(  (0, currentBit, (firstBytesDistance + instructionNum)), block  )
                currentbit -= 1
        for bit in byte2:
            if bit == '1':
                schem.setBlock(  (0, currentBit, (firstBytesDistance - instructionNum)), block  )
                currentbit -= 1
        instructionNum += 1
    
    schem.save(  "schematics", "fibsequence", mcschematic.Version.JE_1_18_2)
        


