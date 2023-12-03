
def parse_input():
    rows = []
    with open("in.txt", "r") as f:
        for l in f:
            rows.append(list(l.strip()))
    return rows


def parse_number(arr, idx):
    if not arr[idx].isdigit():
        return 0
    num_str = arr[idx]

    # try backward
    if idx-1 >=0 and arr[idx-1].isdigit():
        curr = idx-1
        while curr >=0 and arr[curr].isdigit():
            num_str += arr[curr]
            curr -= 1
        num_str = num_str[::-1]

    # try forward
    elif idx+1 < len(arr) and arr[idx+1].isdigit():
        curr = idx+1
        while curr < len(arr) and arr[curr].isdigit():
            num_str += arr[curr]
            curr += 1

    return int(num_str)
            

def process(schematic):
    symbol_parts = []
    for i in range(len(schematic)):
        for j in range(len(schematic[i])):
            curr = schematic[i][j]
            if curr != "." and not curr.isdigit():
                # you found a symbol, now parse the parts
                parts_on_symbol = []
                for x in range(i-1, i+2):
                    if x in range(0, len(schematic)):
                        # for the top and bottom row,
                        # since we read across the row, the numbers in the three positions might overlap
                        # pull all the possible numbers from the row and take the biggest
                        if x != i:
                            possible_parts = []
                            for y in range(j-1, j+2):
                                if y in range(0, len(schematic[x])):
                                    possible_parts.append(parse_number(schematic[x], y))
                            if possible_parts[1] == 0:
                                parts_on_symbol.extend(possible_parts)
                            else:
                                parts_on_symbol.append(max(possible_parts))
                        else:
                            for y in range(j-1, j+2):
                                if y in range(0, len(schematic[x])):
                                    parts_on_symbol.append(parse_number(schematic[x], y))
                symbol_parts.append([p for p in parts_on_symbol if p != 0])
    return symbol_parts

def part1(valid_parts):
    return sum(valid_parts)

def part2(valid_parts):
    if len(valid_parts) == 2:
        return valid_parts[0] * valid_parts[1]
    else:
        return 0

schematic = parse_input()
parts = process(schematic)
print(sum([part1(ps) for ps in parts]))
print(sum([part2(ps) for ps in parts]))
