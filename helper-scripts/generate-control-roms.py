FETCH_STATES = {
    "T1": {
        "RD_SELECT": "PC",
        "R_ENABLE": 1,
        "MAR_LOAD": 1
    },
    "T2": {
        "RD_SELECT": "PC",
        "WR_SELECT": "PC",
        "R_LOAD": 1,
        "ALU_ENABLE": 1,
        "ALU_OP": "INR"
    },
    "T3": {
        "RAM_ENABLE": 1,
        "IR_LOAD": 1
    }
}

MNEMONICS = {
    "LDR": {
        "opcode": "111000",
        "states": {
            "T4": {
                "RD_SELECT": "PC",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T5": {
                "RD_SELECT": "PC",
                "WR_SELECT": "PC",
                "R_LOAD": 1,
                "ALU_ENABLE": 1,
                "ALU_OP": "INR2"
            },
            "T6": {
                "MAR_INTERNAL_LOAD": 1,
                "READ_TWO_BYTES": 1
            },
            "T7": {
                "WR_SELECT": "Rd",
                "R_LOAD": 1,
                "RAM_ENABLE": 1
            }
        }
    },
    "STR": {
        "opcode": "111001",
        "states": {
            "T4": {
                "RD_SELECT": "PC",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T5": {
                "RD_SELECT": "PC",
                "WR_SELECT": "PC",
                "R_LOAD": 1,
                "ALU_ENABLE": 1,
                "ALU_OP": "INR2"
            },
            "T6": {
                "MAR_INTERNAL_LOAD": 1,
                "READ_TWO_BYTES": 1
            },
            "T7": {
                "RD_SELECT": "Rs",
                "R_ENABLE": 1,
                "RAM_LOAD": 1
            }
        }
    },
    "MOV": {
        "opcode": "0100",
        "states": {
            "T4": {
                "RD_SELECT": "Rs",
                "WR_SELECT": "Rd",
                "INTERNAL_LOAD": 1,
            }
        }
    },
    "MVI": {
        "opcode": "110000",
        "states": {
            "T4": {
                "RD_SELECT": "PC",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T5": {
                "RD_SELECT": "PC",
                "WR_SELECT": "PC",
                "R_LOAD": 1,
                "ALU_ENABLE": 1,
                "ALU_OP": "INR"
            },
            "T6": {
                "WR_SELECT": "Rd",
                "R_LOAD": 1,
                "RAM_ENABLE": 1,
            },
        }
    },
    "ADD": {
        "opcode": "0101",
        "states": {
            "T4": {
                "RD_SELECT": "Rs",
                "WR_SELECT": "Rd",
                "R_LOAD": 1,
                "FLAGS_LOAD": 1,
                "R_ALU_TWO_OPERANDS": 1,
                "ALU_ENABLE": 1,
                "FLAGS_ENABLE": 1,
                "ALU_OP": "ADD",
            }
        }
    },
    "SUB": {
        "opcode": "0110",
        "states": {
            "T4": {
                "RD_SELECT": "Rs",
                "WR_SELECT": "Rd",
                "R_LOAD": 1,
                "FLAGS_LOAD": 1,
                "R_ALU_TWO_OPERANDS": 1,
                "ALU_ENABLE": 1,
                "FLAGS_ENABLE": 1,
                "ALU_OP": "SUB",
            }
        }
    },
    "INR": {
        "opcode": "000000",
        "states": {
            "T4": {
                "RD_SELECT": "R",
                "WR_SELECT": "R",
                "R_LOAD": 1,
                "FLAGS_LOAD": 1,
                "ALU_ENABLE": 1,
                "FLAGS_ENABLE": 1,
                "ALU_OP": "INR",
            }
        }
    },
    "DER": {
        "opcode": "000001",
        "states": {
            "T4": {
                "RD_SELECT": "R",
                "WR_SELECT": "R",
                "R_LOAD": 1,
                "FLAGS_LOAD": 1,
                "ALU_ENABLE": 1,
                "FLAGS_ENABLE": 1,
                "ALU_OP": "DER",
            }
        }
    },
    "ROR": {
        "opcode": "000010",
        "states": {
            "T4": {
                "RD_SELECT": "R",
                "WR_SELECT": "R",
                "R_LOAD": 1,
                "FLAGS_LOAD": 1,
                "ALU_ENABLE": 1,
                "FLAGS_ENABLE": 1,
                "ALU_OP": "ROR",
            }
        }
    },
    "ROL": {
        "opcode": "000011",
        "states": {
            "T4": {
                "RD_SELECT": "R",
                "WR_SELECT": "R",
                "R_LOAD": 1,
                "FLAGS_LOAD": 1,
                "ALU_ENABLE": 1,
                "FLAGS_ENABLE": 1,
                "ALU_OP": "ROL",
            }
        }
    },
    "ANR": {
        "opcode": "0111",
        "states": {
            "T4": {
                "RD_SELECT": "Rs",
                "WR_SELECT": "Rd",
                "R_LOAD": 1,
                "FLAGS_LOAD": 1,
                "R_ALU_TWO_OPERANDS": 1,
                "ALU_ENABLE": 1,
                "FLAGS_ENABLE": 1,
                "ALU_OP": "AND",
            }
        }
    },
    "ORR": {
        "opcode": "1000",
        "states": {
            "T4": {
                "RD_SELECT": "Rs",
                "WR_SELECT": "Rd",
                "R_LOAD": 1,
                "FLAGS_LOAD": 1,
                "R_ALU_TWO_OPERANDS": 1,
                "ALU_ENABLE": 1,
                "FLAGS_ENABLE": 1,
                "ALU_OP": "OR",
            }
        }
    },
    "XRR": {
        "opcode": "1001",
        "states": {
            "T4": {
                "RD_SELECT": "Rs",
                "WR_SELECT": "Rd",
                "R_LOAD": 1,
                "FLAGS_LOAD": 1,
                "R_ALU_TWO_OPERANDS": 1,
                "ALU_ENABLE": 1,
                "FLAGS_ENABLE": 1,
                "ALU_OP": "XOR",
            }
        }
    },
    "JMP": {
        "opcode": "11010001",
        "states": {
            "T4": {
                "RD_SELECT": "PC",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T5": {
                "WR_SELECT": "PC",
                "R_LOAD": 1,
                "RAM_ENABLE": 1,
                "READ_TWO_BYTES": 1
            }
        }
    },
    "JZ": {
        "opcode": "11010010",
        "states": {
            "T4": {
                "RD_SELECT": "SR",
                "R_ENABLE": 1
            },
            "T5": {
                "RD_SELECT": "PC",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T6": {
                "WR_SELECT": "PC",
                "R_LOAD": 1,
                "RAM_ENABLE": 1,
                "READ_TWO_BYTES": 1
            }
        }
    },
    "CALL": {
        "opcode": "11010011",
        "states": {
            "T4": {
                "RD_SELECT": "PC",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T5": {
                "RD_SELECT": "PC",
                "WR_SELECT": "PC",
                "R_LOAD": 1,
                "ALU_ENABLE": 1,
                "ALU_OP": "INR2"
            },
            "T6": {
                "WR_SELECT": "TMP",
                "R_LOAD": 1,
                "RAM_ENABLE": 1,
                "READ_TWO_BYTES": 1
            },
            "T7": {
                "RD_SELECT": "SP",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T8": {
                "RD_SELECT": "PC",
                "R_ENABLE": 1,
                "RAM_LOAD": 1,
            },
            "T9": {
                "RD_SELECT": "TMP",
                "WR_SELECT": "PC",
                "INTERNAL_LOAD": 1,
            },
            "T10": {
                "RD_SELECT": "SP",
                "WR_SELECT": "SP",
                "R_LOAD": 1,
                "ALU_ENABLE": 1,
                "ALU_OP": "DER"
            },
        }
    },
    "RET": {
        "opcode": "11110000",
        "states": {
            "T4": {
                "RD_SELECT": "SP",
                "WR_SELECT": "SP",
                "R_LOAD": 1,
                "ALU_ENABLE": 1,
                "ALU_OP": "INR"
            },
            "T5": {
                "RD_SELECT": "SP",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T6": {
                "WR_SELECT": "PC",
                "R_LOAD": 1,
                "RAM_ENABLE": 1,
                "READ_TWO_BYTES": 1
            },
        }
    },
    "PUSH": {
        "opcode": "000100",
        "states": {
            "T4": {
                "RD_SELECT": "SP",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T6": {
                "RD_SELECT": "R",
                "R_ENABLE": 1,
                "RAM_LOAD": 1,
            },
            "T6": {
                "RD_SELECT": "SP",
                "WR_SELECT": "SP",
                "R_LOAD": 1,
                "ALU_ENABLE": 1,
                "ALU_OP": "DER"
            },
        }
    },
    "POP": {
        "opcode": "000101",
        "states": {
            "T4": {
                "RD_SELECT": "SP",
                "WR_SELECT": "SP",
                "R_LOAD": 1,
                "ALU_ENABLE": 1,
                "ALU_OP": "INR"
            },
            "T5": {
                "RD_SELECT": "SP",
                "R_ENABLE": 1,
                "MAR_LOAD": 1,
            },
            "T6": {
                "RD_SELECT": "R",
                "R_LOAD": 1,
                "RAM_ENABLE": 1,
            },
        }
    },
    "OUTX": {
        "opcode": "000110",
        "states": {
            "T4": {
                "RD_SELECT": "R",
                "R_ENABLE": 1,
                "PORT_SELECT": "X",
                "OUT_LOAD": 1
            },
        }
    },
    "OUTY": {
        "opcode": "000111",
        "states": {
            "T4": {
                "RD_SELECT": "R",
                "R_ENABLE": 1,
                "PORT_SELECT": "Y",
                "OUT_LOAD": 1
            },
        }
    },
    "OUTZ": {
        "opcode": "001000",
        "states": {
            "T4": {
                "RD_SELECT": "R",
                "R_ENABLE": 1,
                "PORT_SELECT": "Z",
                "OUT_LOAD": 1
            },
        }
    },
    # "NOP": "11111110", Removed because it only perform the general fetch microinstructions
    "HLT": {
        "opcode": "11111111",
        "states": {
            "T4": {
                "HLT": 1,
            },
        }
    },
}

CONTROL_SIGNALS_ENCODING = {
    "IR_LOAD": 0,
    "RAM_LOAD": 1,
    "RAM_ENABLE": 2,
    "MAR_LOAD": 3,
    "MAR_INTERNAL_LOAD": 4,
    "READ_TWO_BYTES": 5,
    "PORT_SELECT_1": 6,
    "PORT_SELECT_0": 7,
    "OUT_LOAD": 8,
    "ALU_ENABLE": 9,
    "FLAGS_ENABLE": 10,
    "ALU_OP_3": 11,
    "ALU_OP_2": 12,
    "ALU_OP_1": 13,
    "ALU_OP_0": 14,
    "RD_SELECT_3": 15,
    "RD_SELECT_2": 16,
    "RD_SELECT_1": 17,
    "RD_SELECT_0": 18,
    "WR_SELECT_3": 19,
    "WR_SELECT_2": 20,
    "WR_SELECT_1": 21,
    "WR_SELECT_0": 22,
    "R_ENABLE": 23,
    "R_LOAD": 24,
    "FLAGS_LOAD": 25,
    "INTERNAL_LOAD": 26,
    "R_ALU_TWO_OPERANDS": 27,
    "HLT": 28
}

MULTIPLE_BITS_CONTROL_SIGNALS = ["PORT_SELECT", "ALU_OP", "RD_SELECT", "WR_SELECT"]

ENCODING = {
    "PORT_SELECT": {"X": "00", "Y": "01", "Z": "10"},
    "ALU_OP": {
        "ADD":  "0000",
        "SUB":  "0001",
        "INR":  "0010",
        "DER":  "0011",
        "ROR":  "0100",
        "ROL":  "0101",
        "AND":  "0110",
        "OR":   "0111",
        "XOR":  "1000",
        "INR2": "1001"
    },
    "REGISTERS": {
        "A":   "0000",
        "B":   "0001",
        "C":   "0010",
        "D":   "0011",
        "SR":  "0100",
        "TMP": "0110",
        "SP":  "1000",
        "PC":  "1010"
    }
}

control_rom = []
address_rom = {}

def generate_control_word_from_t_state(t_state, destination_register_encoding="", source_register_encoding=""):
    control_word = list("0" * len(CONTROL_SIGNALS_ENCODING))

    for control_signal in t_state.keys():
        if control_signal in MULTIPLE_BITS_CONTROL_SIGNALS:
            if control_signal in ["RD_SELECT", "WR_SELECT"]:
                if t_state[control_signal] in ["R", "Rd"]:
                    encoding_value = destination_register_encoding
                elif t_state[control_signal] == "Rs":
                    encoding_value = source_register_encoding
                else:
                    encoding_value = ENCODING["REGISTERS"][t_state[control_signal]]
            else:
                encoding_value = ENCODING[control_signal][t_state[control_signal]]

            for index, digit in enumerate(encoding_value):
                control_word[CONTROL_SIGNALS_ENCODING[control_signal + "_" + str(len(encoding_value) - 1 - index)]] = digit
        else:
            control_word[CONTROL_SIGNALS_ENCODING[control_signal]] = str(t_state[control_signal])

    return "".join(control_word)

def decimal_to_binary(decimal, bits=2):
    return bin(decimal)[2:].zfill(bits)

def save_rom_to_file(rom, file_path):
    with open(file_path, "w") as output_file:
        output_file.write("\n".join(rom))

for fetch_state in FETCH_STATES.keys():
    control_rom.append(generate_control_word_from_t_state(FETCH_STATES[fetch_state]))

for mnemonic in MNEMONICS.keys():
    if len(MNEMONICS[mnemonic]["opcode"]) == 6:
        for register_index in range(4):
            register_encoding = decimal_to_binary(register_index)
            opcode = MNEMONICS[mnemonic]["opcode"] + register_encoding
            address_rom[int(opcode, 2)] = decimal_to_binary(len(control_rom), 8)

            for t_state in MNEMONICS[mnemonic]["states"].keys():
                control_rom.append(generate_control_word_from_t_state(MNEMONICS[mnemonic]["states"][t_state], register_encoding))
    elif len(MNEMONICS[mnemonic]["opcode"]) == 4:
        for destination_register_index in range(4):
            destination_register_encoding = decimal_to_binary(destination_register_index)

            for source_register_index in range(4):
                source_register_encoding = decimal_to_binary(source_register_index)
                opcode = MNEMONICS[mnemonic]["opcode"] + destination_register_encoding + source_register_encoding
                address_rom[int(opcode, 2)] = decimal_to_binary(len(control_rom), 8)

                for t_state in MNEMONICS[mnemonic]["states"].keys():
                    control_rom.append(generate_control_word_from_t_state(MNEMONICS[mnemonic]["states"][t_state], destination_register_encoding, source_register_encoding))
    else:
        address_rom[int(MNEMONICS[mnemonic]["opcode"], 2)] = decimal_to_binary(len(control_rom), 8)

        for t_state in MNEMONICS[mnemonic]["states"].keys():
            control_rom.append(generate_control_word_from_t_state(MNEMONICS[mnemonic]["states"][t_state]))

# Fill in the empty records of the address memory with zeros to reserve the address
for index in range(256):
    if index not in address_rom.keys():
        address_rom[index] = decimal_to_binary(0, 8)

save_rom_to_file(control_rom, "control_rom.bin")
save_rom_to_file(dict(sorted(address_rom.items())).values(), "address_rom.bin")