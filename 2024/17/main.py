import re
import sys


def format_out(arr):
    return ",".join([str(a) for a in arr])


class Computer:
    
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = b
        self.program = program

    def execute(self):
        ip = 0
        count = 0
        output = []
        while ip < len(self.program) and count < 9999:
            count += 1
            match self.program[ip]:
                case 0:  # adv
                    self.a = self.a >> self.combo(ip)
                    ip += 2
                case 1:  # bxl
                    self.b ^= self.literal(ip)
                    ip += 2
                case 2:  # bst
                    self.b = self.combo(ip) % 8
                    ip += 2
                case 3:  # jnz
                    if self.a != 0:
                        ip = self.literal(ip)
                    else:
                        ip += 2
                case 4:  # bxc
                    self.b ^= self.c
                    ip += 2 
                case 5:  # out
                    out = self.combo(ip) % 8
                    # print(out)
                    output.append(out)
                    ip += 2
                case 6:  # bdv
                    self.b = self.a >>  self.combo(ip)
                    ip += 2
                case 7:  # cdv
                    self.c = self.a >> self.combo(ip)
                    ip += 2

        return output

    def quine(self):
        a = 0
        for shift in range(len(self.program), -1, -1):
            j = shift - len(self.program) 
            print(f"pos: {shift}")
            for i in range(0, 8**3):
                test = a + i * pow(8, shift)
                self.a = test
                out = self.execute()
                print(oct(test), i, j, out, self.program)
                if len(out) + j >= 0 and out[j] == self.program[j]:
                    a = test
                    break

        return a


    def literal(self, ip):
        return self.program[ip + 1]

    def combo(self, ip):
        op = self.program[ip + 1]
        match op:
            case 0 | 1 | 2 | 3:
                return op
            case 4:
                return self.a
            case 5:
                return self.b
            case 6:
                return self.c
            case 7:
                raise Exception("Reserved operand 7")

def parse(file="input.txt"):
    with open(file, "r") as f:
        data = f.read()
        match = re.search(r"Register A: (\d+)", data)
        a = int(match[1])
        match = re.search(r"Register B: (\d+)", data)
        b = int(match[1])
        match = re.search(r"Register C: (\d+)", data)
        c = int(match[1])

        match = re.search(r"Program: (.*)", data)
        program = [int(m) for m in match[1].split(",")]

    return Computer(a, b, c, program)

computer = parse()
print(format_out(computer.execute()))
print(computer.quine())
