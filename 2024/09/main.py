
def parse(file="input.txt"):
    data = []
    prev_state = "FILE"
    state = "FILE"
    file_idx = 0
    with open(file, "r") as f:
        while True:
            char = f.read(1)
            if not char or not char.isdigit():
                break
            cnt = int(char)

            prev_state = state
            match state:
                case "FILE":
                    data.extend([file_idx] * cnt)
                    state = "FREE"
                case "FREE":
                    data.extend([None] * cnt)
                    state = "FILE"
                    file_idx += 1
                case _:
                    raise Exception()
    return data

def compact(data_in):
    data = list(data_in)
    for i in range(len(data) - 1, -1, -1):
        print(f"moving index {i}")
        if data[i] is None:
            continue
        first_free_idx = data.index(None)
        if first_free_idx > i:
            continue
        data[first_free_idx] = data[i]
        data[i] = None

    return data


def checksum(data):
    return sum([
        i * v
        for i, v in enumerate(data)
        if v is not None
    ])

data = parse()
compacted = compact(data)
print(checksum(compacted))

