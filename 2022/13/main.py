import functools
import re

def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a > b:
            return -1
        else:
            return 0

    if not isinstance(a, list):
        a = [a]
    if not isinstance(b, list):
        b = [b]

    for i in range(0, len(a)):
        if i >= len(b):
            return -1
        val = compare(a[i], b[i])
        if val != 0:
            return val

    if len(a) < len(b):
        return 1
    elif len(a) > len(b):
        return -1
    else:
        return 0

def parse_packet(line: str):
    packet = []
    parents = []
    parents.append(packet)
    current = packet
    i = 1
    while i < len(line):
        num = re.search("^(\d+)", line[i:])
        if num is not None:
            val = num.group(1)
            current.append(int(val))
            i += len(val)
        elif line[i] == "[":
            new = []
            current.append(new)
            parents.append(current)
            current = new
            i += 1
        elif line[i] == "]":
            current = parents.pop()
            i += 1
        else:
            i += 1
            
    return packet


def part1():
    with open("in.txt") as f:
        packets = []
        lines = []
        for line in f:
            if len(line.strip()) == 0:
                packets.append((parse_packet(lines[0]), parse_packet(lines[1])))
                lines = []
            else:
                lines.append(line)
        packets.append((parse_packet(lines[0]), parse_packet(lines[1])))
        lines = []

    return sum([i + 1 for i, p in enumerate(packets) if compare(p[0], p[1]) == 1])


def part2():
    with open("in.txt") as f:
        packets = []
        for line in f:
            if len(line.strip()) > 0:
                packets.append(parse_packet(line))

    packets.append([[2]])
    packets.append([[6]])

    packets = sorted(packets, key=functools.cmp_to_key(compare), reverse=True)

    return (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1)



def main():
    print(part1())
    print(part2())


main()
