from abc import ABC, abstractmethod


class Node:
    def __init__(self, space):
        self.space = space
        self.next = None
        self.prev = None


class Disk:


    def __init__(self):
        self.head = None
        self.tail = None

    def print(self):
        curr = self.head
        idx = 0
        while curr is not None:
            print(f"idx {idx} val {curr.space.name} len {curr.space.len}")
            idx += curr.space.len
            curr = curr.next
        print("end")

    def add_space(self, space):
        new_node = Node(space)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def first_free_node(self, size=1, before=None):
        curr = self.head
        while curr is not None and curr != before and (not curr.space.free or curr.space.len < size):
            curr = curr.next
        if curr == before:
            return None
        return curr

    def compact(self):
        curr = self.tail
        while curr != self.head:
            while not curr.space.free:
                free_node = self.first_free_node()
                if free_node is None:
                    break
                
                # insert the last block in the list
                new_node = Node(curr.space.get_last_block())
                new_node.next = free_node
                new_node.prev = free_node.prev
                free_node.prev.next = new_node
                free_node.prev = new_node

                
                free_node.space.len -= 1
                if free_node.space.len == 0:
                    tmp = free_node.prev
                    tmp.next = free_node.next

            curr = curr.prev

    def defrag(self):
        curr = self.tail
        while curr != self.head:
            next_node = curr.prev
            while not curr.space.free and not curr.space.checked:
                curr.space.checked = True
                free_node = self.first_free_node(curr.space.len, before=curr)
                if free_node is None:
                    break

                # we found a gap! first, extract curr from the list
                # and replace with a space
                new_node = Node(Free(curr.space.len))
                new_node.next = curr.next
                new_node.prev = curr.prev
                curr.prev.next = new_node
                if curr.next:
                    curr.next.prev = new_node

                # now, put target into the target spot
                curr.next = free_node
                curr.prev = free_node.prev
                free_node.prev.next = curr
                free_node.prev = curr
                
                free_node.space.len -= curr.space.len
                if free_node.space.len == 0:
                    tmp = free_node.prev
                    tmp.next = free_node.next
                    free_node.next.prev = tmp

            curr = next_node

    def checksum(self):
        curr = self.head
        checksum = 0
        idx = 0
        while curr is not None:
            checksum += curr.space.checksum(idx)
            idx += curr.space.len
            curr = curr.next

        return checksum


class Space(ABC):
    
    def __init__(self, name, free, size):
        self.name = name
        self.free = free
        self.len = size
        self.checked = False

    @abstractmethod
    def checksum(self, position):
        pass


class File(Space):
    def __init__(self, name, size):
        super().__init__(name, False, size)

    def get_last_block(self):
        self.len -= 1
        if self.len == 0:
            self.free = True
        return File(self.name, 1)

    def checksum(self, position):
        return sum([i * int(self.name) for i in range(position, position + self.len)])


class Free(Space):
    def __init__(self, size):
        super().__init__(None, True, size)

    def checksum(self, position):
        return 0


def parse(file="input.txt"):
    prev_state = "FILE"
    state = "FILE"
    file_idx = 0
    disk = Disk()
    with open(file, "r") as f:
        while True:
            char = f.read(1)
            if not char or not char.isdigit():
                break
            cnt = int(char)

            prev_state = state
            match state:
                case "FILE":
                    disk.add_space(File(file_idx, cnt))
                    state = "FREE"
                case "FREE":
                    if cnt != 0:
                        disk.add_space(Free(cnt))
                    state = "FILE"
                    file_idx += 1
                case _:
                    raise Exception()
    return disk


def part1():
    disk = parse()
    disk.compact()
    return disk.checksum()


def part2():
    disk = parse()
    disk.defrag()
    return disk.checksum()

print(part1())
print(part2())

