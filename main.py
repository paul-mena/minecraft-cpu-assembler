import argparse
from assembler import assemble
from schematic import create_schematic
from emulator import run

parser = argparse.ArgumentParser(description="Assembler CLI")

parser.add_argument("program", help="Program name")
parser.add_argument(
    "-r", "--run",
    action="store_true",
    help="Assemble and run the program"
)
parser.add_argument(
    "-s", "--schematic",
    metavar="PATH",
    help="Generate a schematic at the specified path"
)

args = parser.parse_args()

def assemble_program(program):
    assemble(f"programs/{program}.as", "programs/machine_code.txt")

if args.schematic:
    assemble_program(args.program)
    create_schematic("programs/machine_code.txt", args.schematic, args.program)

elif args.run:
    assemble_program(args.program)
    run("programs/machine_code.txt")

else:
    assemble_program(args.program)