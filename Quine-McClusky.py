
sop = [0, 2, 8, 9, 11, 10, 15]
sop.sort()
variables = "abcd"
num_of_bits = len(variables)
match_group = []


def bin2str(x: int):
    """
    :param x: int var to be converted into binary
    :return: string representation of binary x, with padded 0s
    """
    return bin(x)[2:].zfill(num_of_bits)


def find_weight(x):
    weight = 0
    while x > 0:
        weight = weight + (x & 1)
        x = x >> 1
    return weight


def compare_minterms(x: str, y: str) -> str | None:
    """
        Compares two given minterms and return a string representation of the result.
        If the two minterms have one bit difference, return a string with "_" inplace of the different bit.
        If more than two bits are different, return None.

        Example:
            x is "0010"
            y is "1010"
            returns "_010"
    """
    n = 0
    diff_bit = 0
    output = ""
    while n < num_of_bits:
        if x[n] == y[n]:
            output = output + x[n]
        else:
            diff_bit = diff_bit + 1
            output = output + "_"
        n = n + 1
    return output if diff_bit <= 1 else None


class WeightTable:
    def __init__(self, weight):
        self.groups = {}
        self.weight_list = []

    def add_item(self, weight, j, pattern):
        if weight not in self.groups:
            self.groups[weight] = []
            self.weight_list.append(weight)
        self.groups[weight].append({'j':[j], 'pattern': pattern})

    def compare_adjacent_group(self):
        for base_weight in self.weight_list[:-1]:
            self.groups






