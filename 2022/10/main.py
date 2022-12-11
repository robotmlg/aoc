
def parse_input():
    instructions = []
    with open("in.txt") as f:
        for line in f:
            instructions.append(line.strip().split(" "))
    return instructions


INSTRUCTIONS = {
    "noop": 1,
    "addx": 2,
}


def main():
    instructions = parse_input()

    cycle = 1
    x = 1
    signal_strength = [0]  # set cycle 0 to 0 strength
    pixels = [" "] * 240
    for instr in instructions:
        instr_cycles = INSTRUCTIONS[instr[0]]
        curr_cycles = 0

        while curr_cycles < instr_cycles:
            signal_strength.append(cycle * x)
            if (cycle - 1) % 40 in range(x-1, x+2):
                pixels[cycle-1] = "#"
            cycle += 1
            curr_cycles += 1
            if curr_cycles == instr_cycles:
                match instr[0]:
                    case "addx":
                        x += int(instr[1])
                    case "noop":
                        pass
                    case _:
                        raise Exception

    print(
        signal_strength[20] +
        signal_strength[60] +
        signal_strength[100] +
        signal_strength[140] +
        signal_strength[180] +
        signal_strength[220] 
    )
    for i in range(0, 6):
        print(
            "".join(pixels[i*40:(i+1)*40])
        )


main()
