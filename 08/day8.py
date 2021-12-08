
"""
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg
"""


class Row:

    def __init__(self, data: str):
        pattern_str, output_str = data.split("|")
        self.patterns = self._get_input_sorted(pattern_str)
        self.outputs = self._get_input_sorted(output_str)
        self.digit_patterns = [''] * 10

        # put in the known patterns
        self.digit_patterns[1] = self._get_pattern_length(2)
        self.digit_patterns[7] = self._get_pattern_length(3)
        self.digit_patterns[4] = self._get_pattern_length(4)
        self.digit_patterns[8] = self._get_pattern_length(7)

        segment_map = {}
        a_candidates = [c for c in self.digit_patterns[7]
                        if c not in self.digit_patterns[1]]
        assert len(a_candidates) == 1
        segment_map["a"] = a_candidates[0]

        nine_without_bottom = self._segment_add(self.digit_patterns[7],
                                                self.digit_patterns[4])
        nine_candidates = [p for p in self.patterns
                           if len(p) == 6 and len(self._string_difference(p, nine_without_bottom)) == 1]
        assert len(nine_candidates) == 1
        self.digit_patterns[9] = nine_candidates[0]
        segment_map["e"] = self._string_difference(self.digit_patterns[8],
                                                        self.digit_patterns[9])
        segment_map["g"] = self._string_difference(self.digit_patterns[9],
                                                        nine_without_bottom)

        four_arm = self._string_difference(self.digit_patterns[4],
                                           self.digit_patterns[1])
        zero_without_b = self._string_difference(self.digit_patterns[8],
                                                 four_arm)
        zero_candidates = [p for p in self.patterns
                           if len(p) == 6 and
                        len(self._string_difference(p, zero_without_b)) == 1]
        assert len(zero_candidates) == 1
        self.digit_patterns[0] = zero_candidates[0]
        segment_map["b"] = self._string_difference(self.digit_patterns[0],
                                                        zero_without_b)

        six_candidates = [p for p in self.patterns
                          if len(p) == 6 and p not in [self.digit_patterns[0],
                                                       self.digit_patterns[9]]]
        assert len(six_candidates) == 1
        self.digit_patterns[6] = six_candidates[0]

        segment_map["c"] = self._string_difference(self.digit_patterns[8],
                                                        self.digit_patterns[6])
        segment_map["d"] = self._string_difference(self.digit_patterns[8],
                                                        self.digit_patterns[0])
        segment_map["f"] = self._string_difference(self.digit_patterns[1],
                                                        segment_map["c"])

        self.digit_patterns[2] = self._segment_add(segment_map["a"],
                                                   segment_map["c"],
                                                   segment_map["d"],
                                                   segment_map["e"],
                                                   segment_map["g"])
        self.digit_patterns[3] = self._segment_add(segment_map["a"],
                                                   segment_map["c"],
                                                   segment_map["d"],
                                                   segment_map["f"],
                                                   segment_map["g"])
        self.digit_patterns[5] = self._segment_add(segment_map["a"],
                                                   segment_map["b"],
                                                   segment_map["d"],
                                                   segment_map["f"],
                                                   segment_map["g"])

    def count_output_digits(self, *segments):
        return len([o for o in self.outputs if len(o) in segments])

    def get_output(self) -> int:
        output = 0
        digit_map = {self.digit_patterns[i]: str(i)
                     for i in range(len(self.digit_patterns))}
        return int("".join([digit_map[o] for o in self.outputs]))

    def _get_input_sorted(self, input):
        return list(map(
                lambda s : "".join(sorted(s)),
                [p.strip() for p in input.strip().split(" ")]))

    def _string_difference(self, a, b):
        return "".join([c for c in a if c not in b])

    def _segment_add(self, *segments):
        return "".join(sorted(set("".join(segments))))

    def _get_pattern_length(self, length):
        return [p for p in self.patterns if len(p) == length][0]


def day8A():
    count = 0
    with open("day8.txt") as f:
        for line in f:
            count += Row(line).count_output_digits(2, 3, 4, 7)
    return count


def day8B():
    rows_sum = 0
    with open("day8.txt") as f:
        for line in f:
            rows_sum += Row(line).get_output()
    return rows_sum


if __name__ == "__main__":
    print(day8A())
    print(day8B())
