def parse_input(filename: str):
    with open(filename) as f:
        algorithm = f.readline().strip()
        f.readline()

        image = []
        for line in f.readlines():
            image.append(list(line.strip()))

        return algorithm, image


def enhance(algorithm, image, field=None):
    if field is None:
        field = 0

    def get_pixel(x, y):
        if ((y < 0 or y >= len(image)) or
                (x < 0 or x >= len(image[0]))):
            return field
        return 1 if image[y][x] == "#" else 0

    def get_new_pixel(x, y):
        bits = [
            get_pixel(x - 1, y - 1), get_pixel(x, y - 1), get_pixel(x + 1, y - 1),
            get_pixel(x - 1, y),     get_pixel(x, y),     get_pixel(x + 1, y),
            get_pixel(x - 1, y + 1), get_pixel(x, y + 1), get_pixel(x + 1, y + 1),
        ]
        num = int("0b" + "".join([str(b) for b in bits]), base=2)
        return algorithm[num]

    # new grid needs to be one pixel larger in every direction
    new_image = [["."] * (len(image[0]) + 2) for _ in range(len(image) + 2)]
    for y in range(-1, len(image) + 1):
        for x in range(-1, len(image[0]) + 1):
            new_image[y + 1][x + 1] = get_new_pixel(x, y)

    return new_image, 0 if new_image[0][0] == "." else 1


if __name__ == "__main__":
    algorithm, image = parse_input("day20.txt")
    one_enhance, field = enhance(algorithm, image)
    enhanced, field = enhance(algorithm, one_enhance, field)
    print(sum([sum([1 if pixel == "#" else 0 for pixel in row])
               for row in enhanced]))

    for _ in range(48):
        enhanced, field = enhance(algorithm, enhanced, field)

    print(sum([sum([1 if pixel == "#" else 0 for pixel in row])
               for row in enhanced]))
