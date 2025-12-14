from functools import cache


def parse(name="input.txt"):
    graph = {"out": []}

    with open(name) as f:
        for line in f:
            node, rest = line.strip().split(": ")
            children = rest.split(" ")
            graph[node] = children

    return graph

GRAPH = {}

@cache
def find_paths(start, end):

    if start == end:
        return 1
    else:
        return sum([find_paths(n, end) for n in GRAPH[start]])
 

def part1(graph):
    global GRAPH
    GRAPH = graph
    find_paths.cache_clear()
    return find_paths("you", "out")


def part2(graph):
    global GRAPH
    GRAPH = graph
    find_paths.cache_clear()

    return (
        find_paths("svr", "dac") *
        find_paths("dac", "fft") *
        find_paths("fft", "out")
        ) + (
            find_paths("svr", "fft") *
            find_paths("fft", "dac") *
            find_paths("dac", "out")
        )


graph = parse("ex_input.txt")
assert 5 == part1(graph)
graph = parse("ex_input2.txt")
assert 2 == part2(graph)

graph = parse()
print(part1(graph))
print(part2(graph))
