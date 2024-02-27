
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


def find_weight(x: str) -> int:
    weight = 0
    for n in range(len(x)):
        weight = weight + (1 if x[n] == "1" else 0)
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
    def __init__(self):
        self.groups = {}
        self.weight_list = []

    def add_item(self, weight: int, j: list[int], pattern: str, check_mark: bool):
        if weight not in self.groups:
            self.groups[weight] = []
            self.weight_list.append(weight)
        self.groups[weight].append({'j': j, 'pattern': pattern, 'check_mark': check_mark})

    def compare_adjacent_group(self):
        for i, w in enumerate(self.weight_list):
            base_weight_group = self.weight_list[i]
            try:
                target_weight_group = self.weight_list[i+1]
            except IndexError:
                # reached the end of list
                continue

            for base in self.groups[base_weight_group]:
                for target in self.groups[target_weight_group]:
                    compare_minterms(base['pattern'], target['pattern'])


# initialize
match0 = WeightTable()
for item in sop:
    sop_pattern = bin2str(item)
    sop_weight = find_weight(sop_pattern)
    match0.add_item(sop_weight, [item], sop_pattern, False)

print(match0)












