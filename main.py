from assembler import assemble
from schematic import create_schematic
from emulator import run

def assemble_and_run(program_file_path):
    assemble(program_file_path, 'machine_code.txt')
    run('machine_code.txt')

def assemble_and_make_schem(program_file_path, schem_path, schem_file_name):
    assemble(program_file_path, 'machine_code.txt')
    create_schematic('machine_code.txt', schem_path, schem_file_name)

assemble_and_make_schem('programs/division.as',"C:/Users/paulm/AppData/Roaming/.minecraft/config/worldedit/schematics","division")
