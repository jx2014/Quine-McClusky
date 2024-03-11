# Python Script for SOP Minimization

## Description
This script simplifies Sum of Products (SOP) expressions using the Quine-McCluskey algorithm and identifies essential prime implicants. It outputs a minimized boolean expression along with tables that show the process of finding prime implicants and essential prime implicants.

## Features
- Input SOP expressions directly from the user.
- Outputs the process tables for identifying prime and essential prime implicants.
- Simplifies the boolean expression and presents it in a readable format.

## How to Run

### Prerequisites
- Python 3.12 installed on your system.

### Instructions
1. Open a terminal or command prompt.
2. Navigate to the directory containing this script.
3. Run the script using Python by entering the following command: Quine-McClusky.py
4. Follow the prompts in the script:
- Enter the SOP expression when prompted (e.g., `0 2 8 9 11 10 15`).
- Enter the variables used in your SOP expression (e.g., `WXYZ` for four variables).

## Example Input and Output
```plaintext
Connected to pydev debugger (build 233.13763.11)
Enter SOP:
Example: 0 2 8 9 11 10 15: 0 2 4 6 7 8 10 11 12 13 14 16 18 19 29 30
Enter Variables: Example: ABCDEFG or WXYZ: VWXYZ
                w(j)                    j              pattern             adjacent
                   0                 [0]                00000                    ✓
                   1                 [2]                00010                    ✓
                                     [4]                00100                    ✓
                                     [8]                01000                    ✓
                                    [16]                10000                    ✓
                   2                 [6]                00110                    ✓
                                    [10]                01010                    ✓
                                    [12]                01100                    ✓
                                    [18]                10010                    ✓
                   3                 [7]                00111                    ✓
                                    [11]                01011                    ✓
                                    [13]                01101                    ✓
                                    [14]                01110                    ✓
                                    [19]                10011                    ✓
                   4                [29]                11101                    ✓
                                    [30]                11110                    ✓
                w(j)                    j              pattern             adjacent
                   0              [0, 2]                000_0                    ✓
                                  [0, 4]                00_00                    ✓
                                  [0, 8]                0_000                    ✓
                                 [0, 16]                _0000                    ✓
                   1              [2, 6]                00_10                    ✓
                                 [2, 10]                0_010                    ✓
                                 [2, 18]                _0010                    ✓
                                  [4, 6]                001_0                    ✓
                                 [4, 12]                0_100                    ✓
                                 [8, 10]                010_0                    ✓
                                 [8, 12]                01_00                    ✓
                                [16, 18]                100_0                    ✓
                   2              [6, 7]                0011_                     
                                 [6, 14]                0_110                    ✓
                                [10, 11]                0101_                     
                                [10, 14]                01_10                    ✓
                                [12, 13]                0110_                     
                                [12, 14]                011_0                    ✓
                                [18, 19]                1001_                     
                   3            [13, 29]                _1101                     
                                [14, 30]                _1110                     
                w(j)                    j              pattern             adjacent
                   0        [0, 2, 4, 6]                00__0                    ✓
                           [0, 2, 8, 10]                0_0_0                    ✓
                          [0, 2, 16, 18]                _00_0                     
                           [0, 4, 8, 12]                0__00                    ✓
                   1      [2, 6, 10, 14]                0__10                    ✓
                          [4, 6, 12, 14]                0_1_0                    ✓
                         [8, 10, 12, 14]                01__0                    ✓
                w(j)                    j              pattern             adjacent
                   0[0, 2, 4, 6, 8, 10, 12, 14]                0___0                     


Minterm| col_0 | col_1 | col_2 | col_3 | col_4 | col_5 | col_6 | col_7 | 
     0 |       |       |       |       |       |       |   x   |   x   |
     2 |       |       |       |       |       |       |   x   |   x   |
     4 |       |       |       |       |       |       |       |   x   |
     6 |   x   |       |       |       |       |       |       |   x   |
     7 |   x   |       |       |       |       |       |       |       |
     8 |       |       |       |       |       |       |       |   x   |
    10 |       |   x   |       |       |       |       |       |   x   |
    11 |       |   x   |       |       |       |       |       |       |
    12 |       |       |   x   |       |       |       |       |   x   |
    13 |       |       |   x   |       |   x   |       |       |       |
    14 |       |       |       |       |       |   x   |       |   x   |
    16 |       |       |       |       |       |       |   x   |       |
    18 |       |       |       |   x   |       |       |   x   |       |
    19 |       |       |       |   x   |       |       |       |       |
    29 |       |       |       |       |   x   |       |       |       |
    30 |       |       |       |       |       |   x   |       |       |


F = V'W'XY + V'WX'Y + VW'X'Y + WXY'Z + WXYZ' + W'X'Z' + V'Z' 
...Good bye...
```

## Contributing
Feel free to fork the repository and submit pull requests with any optimizations or enhancements.

## License
This project is open source and available under the [MIT License](LICENSE.md).


