import argparse
import os

HEXA_OUTPUT_FILE_EXTENSION = ".hex"
BINARY_OUTPUT_FILE_EXTENSION = ".bin"

MNEMONICS_ENCODING = {
    "LDR": "111000",
    "STR": "111001",
    "MOV": "0100",
    "MVI": "110000",
    "ADD": "0101",
    "SUB": "0110",
    "INR": "000000",
    "DER": "000001",
    "ROR": "000010",
    "ROL": "000011",
    "ANR": "0111",
    "ORR": "1000",
    "XRR": "1001",
    "JMP": "11010001",
    "JZ": "11010010",
    "CALL": "11010011",
    "RET": "11110000",
    "PUSH": "000100",
    "POP": "000101",
    "OUTX": "000110",
    "OUTY": "000111",
    "OUTZ": "001000",
    "NOP": "11111110",
    "HLT": "11111111",
}

REGISTERS_ENCODING = {"A": "00", "B": "01", "C": "10", "D": "11"}

class Assembler():
    def __init__(self, assembly_file_path):
        self.assembly_instructions = self.__read_assembly_file(assembly_file_path)
        self.output_file_path = self.__get_file_path_without_extension(assembly_file_path)
        self.memory_records = self.__translate_assembly_instructions()

    def __get_file_path_without_extension(self, assembly_file_path):
        file_name_with_extension = os.path.basename(assembly_file_path)
        file_name_without_extension, file_extension = os.path.splitext(file_name_with_extension)
        directory_path = os.path.dirname(assembly_file_path)

        return os.path.join(directory_path, file_name_without_extension)

    def __read_assembly_file(self, assembly_file_path):
        with open(assembly_file_path, "r") as assembly_file:
            assembly_file_lines = assembly_file.readlines()
            assembly_instructions = []

            for line in assembly_file_lines:
                # Remove comments and empty lines from the start and end of the line
                line = line.split("#")[0].rstrip().strip()
                if line:
                    assembly_instructions.append(line)

            return assembly_instructions

    def __translate_assembly_instructions(self):
        labels_address = {}
        memory_records = []

        # Extract Labels
        for assembly_instruction in self.assembly_instructions:
            if ":" in assembly_instruction:
                label = assembly_instruction[:-1]
                self.__check_label(assembly_instruction, labels_address.keys(), label)
                labels_address[label.upper()] = 0

        for assembly_instruction in self.assembly_instructions:
            instruction_type, instruction_components = self.__get_instruction_type(assembly_instruction)

            if instruction_type == "LABEL":
                labels_address[instruction_components[0].upper()] = self.__decimal_to_hexa(len(memory_records))
            else:
                self.__check_mnemonic(assembly_instruction, instruction_components[0])

                if instruction_type == "SR":
                    self.__check_register(assembly_instruction, instruction_components[1])
                    memory_records.append(MNEMONICS_ENCODING[instruction_components[0]] + REGISTERS_ENCODING[instruction_components[1]])
                elif instruction_type == "DR":
                    self.__check_register(assembly_instruction, instruction_components[1])
                    self.__check_register(assembly_instruction, instruction_components[2])
                    memory_records.append(MNEMONICS_ENCODING[instruction_components[0]] + REGISTERS_ENCODING[instruction_components[1]] + REGISTERS_ENCODING[instruction_components[2]])
                elif instruction_type == "I":
                    self.__check_register(assembly_instruction, instruction_components[1])
                    memory_records.append(MNEMONICS_ENCODING[instruction_components[0]] + REGISTERS_ENCODING[instruction_components[1]])
                    self.__check_hexa_bytes(assembly_instruction, instruction_components[2])
                    memory_records.append(self.__hexa_to_binary(instruction_components[2]))
                elif instruction_type == "J":
                    memory_records.append(MNEMONICS_ENCODING[instruction_components[0]])
                    if instruction_components[1] in labels_address.keys():
                        memory_records.append(instruction_components[1])
                        memory_records.append(instruction_components[1])
                    else:
                        self.__check_hexa_bytes(assembly_instruction, instruction_components[1], 2)
                        memory_records.append(self.__hexa_to_binary(instruction_components[1][:2]))
                        memory_records.append(self.__hexa_to_binary(instruction_components[1][2:]))
                elif instruction_type == "D":
                    self.__check_register(assembly_instruction, instruction_components[1])
                    memory_records.append(MNEMONICS_ENCODING[instruction_components[0]] + REGISTERS_ENCODING[instruction_components[1]])
                    self.__check_hexa_bytes(assembly_instruction, instruction_components[2], 2)
                    memory_records.append(self.__hexa_to_binary(instruction_components[2][:2]))
                    memory_records.append(self.__hexa_to_binary(instruction_components[2][2:]))
                elif instruction_type == "O":
                    memory_records.append(MNEMONICS_ENCODING[instruction_components[0]])

        return self.__replace_label_with_address(memory_records, labels_address)

    def __get_instruction_type(self, instruction):
        instruction_type = ""
        instruction_components = instruction.split()

        if len(instruction_components) == 1:
            if ":" in instruction_components[0]:
                instruction_type = "LABEL"
                instruction_components[0] = instruction_components[0][:-1]
            else:
                instruction_type= "O"
        elif len(instruction_components) == 2:
            if "H" in instruction_components[1] or instruction_components[1] not in REGISTERS_ENCODING:
                instruction_type = "J"

                if "H" in instruction_components[1]:
                    instruction_components[1] = instruction_components[1][:-1].zfill(4)
            else:
                instruction_type = "SR"
        else:
            instruction_components[1] = instruction_components[1][:-1]

            if "H" in instruction_components[2] or instruction_components[2] not in REGISTERS_ENCODING:
                if "H" in instruction_components[2]:
                    instruction_components[2] = instruction_components[2][:-1]

                if len(instruction_components[2]) <= 2:
                    instruction_type = "I"
                    instruction_components[2] = instruction_components[2].zfill(2)
                else:
                    instruction_type = "D"
                    instruction_components[2] = instruction_components[2].zfill(4)
            else:
                instruction_type = "DR"

        return instruction_type, instruction_components
    
    def __replace_label_with_address(self, memory_records, labels_address):
        for memory_address, memory_record in enumerate(memory_records):
            if memory_record in labels_address.keys():
                memory_records[memory_address] = self.__hexa_to_binary(labels_address[memory_record][:2])
                memory_records[memory_address + 1] = self.__hexa_to_binary(labels_address[memory_record][2:])

        return memory_records

    def __check_mnemonic(self, assembly_instruction, mnemonic):
        if mnemonic.upper() not in MNEMONICS_ENCODING.keys():
            raise AssemblySyntaxError(f"at \"{assembly_instruction}\" {mnemonic} mnemonic not defined in the ISA")

    def __check_register(self, assembly_instruction, register):
        if register.upper() not in REGISTERS_ENCODING.keys():
            raise AssemblySyntaxError(f"at \"{assembly_instruction}\" {register} register not available; Programmer-Accessible Registers are [A, B, C, D]")

    def __check_label(self, assembly_instruction, labels, label):
        if label.upper() in labels:
            raise AssemblySyntaxError(f"at \"{assembly_instruction}\" {label} label defined multiple times")

    def __check_hexa_bytes(self, assembly_instruction, hexa, max_bytes_num=1):
        for digit in hexa:
            if digit.upper() not in "0123456789ABCDEF":
                raise AssemblySyntaxError(f"at \"{assembly_instruction}\" {hexa} invalid hexadecimal value")

        if len(hexa) > 2 * max_bytes_num:
            raise AssemblySyntaxError(f"at \"{assembly_instruction}\" {hexa} maximum size exceeded, maximum {max_bytes_num} bytes")

    def generate_binary_machine_code(self):
        self.__generate_machine_code_file(self.memory_records, BINARY_OUTPUT_FILE_EXTENSION)

    def generate_hexa_machine_code(self):
        memory_hexa_records = [self.__binary_to_hexa(memory_binary_record) for memory_binary_record in self.memory_records]
        self.__generate_machine_code_file(memory_hexa_records, HEXA_OUTPUT_FILE_EXTENSION)

    def __binary_to_hexa(self, binary):
        return hex(int(binary, 2))[2:].zfill(2).upper()
    
    def __hexa_to_binary(self, hexa):
        return bin(int(hexa, 16))[2:].zfill(8)
    
    def __decimal_to_hexa(self, decimal):
        return hex(decimal)[2:].zfill(4).upper()

    def __generate_machine_code_file(self, machine_code_lines, extension):
        with open(self.output_file_path + extension, "w") as output_file:
            output_file.write("\n".join(machine_code_lines))

class AssemblySyntaxError(Exception):
    pass

parser = argparse.ArgumentParser(
    prog="Microprocessor Assembler",
    description="Translate the assembly code into machine code, either in hexadecimal or binary format.",
)

parser.add_argument("assembly_file")
parser.add_argument("-oH", "--hexa" , action="store_true", default=False, help="Output the machine code in hexadecimal format")
parser.add_argument("-oB", "--binary", action="store_true", default=False, help="Output the machine code in binary format")

args = parser.parse_args()

assembler = Assembler(args.assembly_file)

if args.binary or (not args.binary and not args.hexa):
    assembler.generate_binary_machine_code()

if args.hexa:
    assembler.generate_hexa_machine_code()