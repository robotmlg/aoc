from functools import reduce
from math import ceil


class Bits:

    def __init__(self, filename: str):
        self.bits = []
        self.current_bit = 0

        self.f = open(filename)

    def __del__(self):
        self.f.close()

    def get_int(self, n):
        return self.bits_to_int(self.get_bits(n))

    def get_bits(self, n):
        end = self.current_bit + n
        if end > len(self.bits):
            self._get_chars(ceil(n / 4))

        out_bits = self.bits[self.current_bit:end]
        self.current_bit = end
        return out_bits

    def _get_chars(self, n):
        chars = self.f.read(n)
        binary = int(chars, base=16)
        total_width = n * 4
        format_string = f"{{0:0{total_width}b}}"
        bits = [int(c) for c in list(format_string.format(binary))]
        self.bits.extend(bits)

    @staticmethod
    def bits_to_int(b: list) -> int:
        return int("0b" + "".join([str(d) for d in b]), base=2)


class Packet:

    def __init__(self, version: int):
        self.version = version
        self.subpackets = []

    @property
    def version_sum(self) -> int:
        return self.version + sum([p.version_sum for p in self.subpackets])

    @property
    def subpacket_values(self):
        return [p.value for p in self.subpackets]


class LiteralPacket(Packet):

    def __init__(self, version: int, bits: Bits):
        super().__init__(version)

        literal_bits = []
        self.segment_count = 0

        while True:
            self.segment_count += 1
            flag = bits.get_int(1)
            literal_bits.extend(bits.get_bits(4))
            if flag == 0:
                break

        self.value = Bits.bits_to_int(literal_bits)

    @property
    def length(self):
        return 6 + 5 * self.segment_count


class OperatorPacket(Packet):

    def __init__(self, version: int, bits: Bits):
        super().__init__(version)
        length_type_id = bits.get_int(1)

        if length_type_id == 1:
            self.header_length = 11
            self.subpacket_count = bits.get_int(self.header_length)

            for i in range(self.subpacket_count):
                self.subpackets.append(PacketFactory(bits).get_packet())
        else:  # length_type_id == 0
            self.header_length = 15
            subpacket_length = bits.get_int(self.header_length)
            length_parsed = 0

            while length_parsed < subpacket_length:
                new_packet = PacketFactory(bits).get_packet()
                self.subpackets.append(new_packet)
                length_parsed += new_packet.length

    @property
    def length(self):
        return 7 + self.header_length + sum([s.length for s in self.subpackets])


class SumPacket(OperatorPacket):
    @property
    def value(self):
        return sum(self.subpacket_values)


class ProductPacket(OperatorPacket):
    @property
    def value(self):
        return int(reduce(lambda x, y: x * y, self.subpacket_values, 1))


class MinPacket(OperatorPacket):
    @property
    def value(self):
        return min(self.subpacket_values)


class MaxPacket(OperatorPacket):
    @property
    def value(self):
        return max(self.subpacket_values)


class GreaterThanPacket(OperatorPacket):
    @property
    def value(self):
        return 1 if self.subpackets[0].value > self.subpackets[1].value else 0


class LessThanPacket(OperatorPacket):
    @property
    def value(self):
        return 1 if self.subpackets[0].value < self.subpackets[1].value else 0


class EqualToPacket(OperatorPacket):
    @property
    def value(self):
        return 1 if self.subpackets[0].value == self.subpackets[1].value else 0


class PacketFactory:

    def __init__(self, bits: Bits):
        self.bits = bits

    def get_packet(self):
        version = self.bits.get_int(3)
        type_id = self.bits.get_int(3)

        if type_id == 4:
            return LiteralPacket(version, self.bits)
        elif type_id == 0:
            return SumPacket(version, self.bits)
        elif type_id == 1:
            return ProductPacket(version, self.bits)
        elif type_id == 2:
            return MinPacket(version, self.bits)
        elif type_id == 3:
            return MaxPacket(version, self.bits)
        elif type_id == 5:
            return GreaterThanPacket(version, self.bits)
        elif type_id == 6:
            return LessThanPacket(version, self.bits)
        elif type_id == 7:
            return EqualToPacket(version, self.bits)
        else:
            raise Exception


if __name__ == "__main__":
    packet = PacketFactory(Bits("day16.txt")).get_packet()
    print(packet.version_sum)
    print(packet.value)
