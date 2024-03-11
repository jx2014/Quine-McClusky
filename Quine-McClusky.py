import sys
from typing import List

if sys.version_info < (3,12):
    print("This script requires Python 3.12 or higher")
    sys.exit(1)


def bin2str(x: int, bit_count: int):
    """
    :param x: int var to be converted into binary
    :param bit_count: int var for number of bits
    :return: string representation of binary x, with padded 0s
    """
    return bin(x)[2:].zfill(bit_count)


def find_weight(x: str) -> int:
    weight = 0
    for n in range(len(x)):
        weight = weight + (1 if x[n] == "1" else 0)
    return weight


class WeightTable:
    def __init__(self):
        self.groups = {}
        self.num_match_groups = 0
        self.prime_implicants = []
        self.pi_binary_representation = {}

    @property
    def valid_groups(self):
        return len(self.groups)

    @property
    def num_of_prime_implicants(self):
        return len(self.prime_implicants)

    def add_item(self, weight: int, j: List[int], pattern: str, check_mark: bool):
        if weight not in self.groups:
            self.groups[weight] = []
        else:
            # do not add duplicate minterms
            for entry in self.groups[weight]:
                if entry.get('j') == j:
                    return
        self.groups[weight].append({'j': j, 'pattern': pattern, 'check_mark': check_mark})
        self.prime_implicants.append(j)
        self.pi_binary_representation[str(j)] = pattern

    def compare_adjacent_group(self):
        weight_list = list(self.groups.keys())
        self.num_match_groups += 1
        for i, weight in enumerate(weight_list):
            base_weight_group = self.groups.get(weight)
            try:
                target_weight_num = weight_list[i + 1]
                target_weight_group = self.groups.get(target_weight_num)
            except IndexError:
                # reach the end of list
                return None

            for base in base_weight_group:
                for target in target_weight_group:
                    compare_result = self.compare_minterms(base['pattern'], target['pattern'])
                    yield self.process_result(base, target, compare_result)

    # find Prime Implicants and remove it
    def remove_prime_implicants(self, j: List[int]):
        if j in self.prime_implicants:
            self.prime_implicants.remove(j)
            self.pi_binary_representation.pop(str(j))

    def process_result(self, base: dict, target: dict, compare_result: str) -> tuple[
        int | None, List[int] | None, str | None, bool | None]:
        weight, j, pattern, check_mark = None, None, None, None
        if compare_result:
            pattern = compare_result
            weight = find_weight(compare_result)
            self.remove_prime_implicants(base.get('j'))
            self.remove_prime_implicants(target.get('j'))
            j = base.get('j') + target.get('j')
            j.sort()
            base['check_mark'] = True
            target['check_mark'] = True
            check_mark = False
        return weight, j, pattern, check_mark

    @staticmethod
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

    def print_table(self):
        print("{: >20} {: >20} {: >20} {: >20}".format("w(j)", "j", "pattern", "adjacent"))
        for weight, terms in self.groups.items():
            print("{: >20}".format(weight), end='')
            for i, term in enumerate(terms):
                j = str(term.get('j'))
                check_mark = '✓' if term.get('check_mark') else ' '
                if i > 0:
                    print("{: >20}".format(' '), end='')
                print("{: >20} {: >20} {: >20}".format(j, term.get('pattern'), check_mark))


def print_prime_implicant_table(list_of_prime_implicants: List[List[int]]):
    all_minterms = sorted(set(sum(list_of_prime_implicants, [])))
    table_title = "\n\nMinterm| " + " | ".join(f"col_{i}" for i in range((len(list_of_prime_implicants)))) + " | "
    print(table_title)
    for minterm in all_minterms:
        print("%6d |" % minterm, end="")
        for col, lst in enumerate(list_of_prime_implicants, 1):
            if minterm in lst:
                print("   x   |", end="")
            else:
                print("       |", end="")
        print("")

def find_essential_pis(list_of_prime_implicants: List[List[int]]) -> tuple[List[int]]:
    essential_pi = []
    for n, pi in enumerate(list_of_prime_implicants):
        for minterm in pi:
            if minterm not in [x for sublist in list_of_prime_implicants[0:n] + list_of_prime_implicants[n+1:] for x in sublist]:
                essential_pi.append(pi)
                break
    return essential_pi

if __name__ == "__main__":

    #sop = [0, 2, 8, 9, 11, 10, 15]
    sop = input("Enter SOP:\nExample: 0 2 8 9 11 10 15: ")
    sop = sop.split(' ')
    sop = [int(n) for n in sop if n != '']
    sop.sort()
    #variables = "abcd"
    varialbes = input("Enter Variables: Example: ABCDEFG or WXYZ: ")
    variables = varialbes.upper().split(' ')[0]
    num_of_bits = len(variables)

    # Verify number of bits are enough to cover SOPs.
    if 2**num_of_bits < sop[-1]:
        print("Maximum SOP term () exceed the number of variables entered." % sop[-1])
        sys.exit()

    # initialize
    t = 0
    match_tables = {t: WeightTable()}
    prime_implicants = []
    essential_pi = []
    prime_implicants_binary = {}

    for item in sop:
        sop_pattern = bin2str(item, num_of_bits)
        sop_weight = find_weight(sop_pattern)
        match_tables[t].add_item(sop_weight, [item], sop_pattern, False)

    while True:
        a_new_table = WeightTable()
        for w, j, p, c in match_tables[t].compare_adjacent_group():
            if j is None:
                continue
            a_new_table.add_item(w, j, p, c)
        match_tables[t].print_table()
        prime_implicants += match_tables[t].prime_implicants
        prime_implicants_binary.update(match_tables[t].pi_binary_representation)
        if a_new_table.valid_groups == 0:
            break
        t += 1
        match_tables[t] = a_new_table

    print_prime_implicant_table(prime_implicants)
    essentail_prime_implicant = find_essential_pis(prime_implicants)


    boolean_representation = []
    for epi in essentail_prime_implicant:
        boolean_expression = ""
        m = prime_implicants_binary.get(str(epi))
        for n, var in enumerate(variables):
            if m[n] == '1':
                boolean_expression += var
            if m[n] == '0':
                boolean_expression += "%s'" % var
            if m[n] == '_':
                continue
        boolean_representation.append(boolean_expression)

    print("\n")
    print('F = %s ' % ' + '.join(boolean_representation))
    print("...Good bye...")
