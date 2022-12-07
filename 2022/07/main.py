import sys


class FSObject():

    def get_size(self):
        raise NotImplementedError()


class Directory(FSObject):

    def __init__(self, name: str, parent=None):
        self.name = name
        self.children = []
        self.parent = parent
        self.type = "dir"

    def get_size(self):
        return sum([c.get_size() for c in self.children])

    def add_file(self, file):
        self.children.append(file)

    def get_dirs(self):
        return [f for f in self.children if f.type == "dir"]


class File(FSObject):
    
    def __init__(self, name: str, size: int, parent):
        self.name = name
        self.size = size
        self.parent = parent
        self.type = "file"

    def get_size(self):
        return self.size


def parse_input():
    root = None
    with open("in.txt") as f:
        current_dir = None
        for line in f:
            if line[0] == "$":
                match line[2:4]:
                    case "cd":
                        dir_name = line[5:-1]
                        if dir_name == "/":
                            root = Directory(dir_name)
                            current_dir = root
                        elif dir_name == "..":
                            current_dir = current_dir.parent
                        else:
                            new_dir = Directory(dir_name, current_dir)
                            current_dir.add_file(new_dir)
                            current_dir = new_dir
                    case "ls":
                        pass
                    case _:
                        raise Exception
            else:  # we must be in ls output here
                match line.split():
                    case ["dir", dir_name]:
                        pass  # we don't need to do anything with a dir
                    case [size_str, file_name]:
                        size = int(size_str)
                        current_dir.add_file(File(file_name, size, current_dir))
                    case _:
                        print(line.split())
                        raise Exception

    return root


def part1(fs):
    dir_queue = [fs]

    total_valid_size = 0
    while len(dir_queue) > 0:
        curr = dir_queue.pop(0)

        curr_size = curr.get_size()
        if curr_size <= 100000:
            total_valid_size += curr_size

        children = curr.get_dirs()
        dir_queue.extend(children)

    return total_valid_size


def part2(fs):
    current_size = fs.get_size()
    unused_space = 70000000 - current_size
    to_delete = 30000000 - unused_space

    dir_queue = [fs]
    size_to_delete = sys.maxsize
    while len(dir_queue) > 0:
        curr = dir_queue.pop(0)

        curr_size = curr.get_size()
        if curr_size >= to_delete and curr_size < size_to_delete:
            size_to_delete = curr_size

        children = curr.get_dirs()
        dir_queue.extend(children)

    return size_to_delete


def main():
    fs = parse_input()
    print(part1(fs))
    print(part2(fs))


main()
