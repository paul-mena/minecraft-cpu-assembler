This is an assembler and emulator I made for an 8-bit computer I made in Minecraft. It uses a custom instruction set (see [ISA.md](ISA.md)) since a Minecraft computer ain't running x86. I've done my best to add good documentation but this is mainly just an old project I made public for anyone curious.

If you want to attempt to use this proceed to the instructions below. 

# Usage
You can run programs on the Minecraft computer or the emulator. Perform the initial setup and proceed below.
## Initial Setup
**1. Make sure you have Python installed**

Install it [here](https://www.python.org/downloads/)

**2. Clone the repo and cd into it**
```bash
git clone https://github.com/paul-mena/minecraft-cpu-assembler
cd minecraft-cpu-assembler
```
**3. Setup a Python virtual environment**

Try `python3` if `python` doesn't work
```bash
python -m venv venv
source venv/bin/activate
```
**4. Install mcschematic**
```bash
pip install mcschematic
```
## Running programs in Minecraft
To see how to setup the Minecraft world and run programs, see [MINECRAFT.md](./MINECRAFT.md).
## Running programs in the emulator

**Running a program from `programs/`**
```bash
python main.py fibsequence -r
```
At the end of each run, the emulator will print a memory dump of all 32 bytes of memory and then the registers.

Take a look at the examples in `programs/` and [ISA.md](ISA.md) for info on how to make your own programs.
