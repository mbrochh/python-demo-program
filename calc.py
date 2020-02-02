# 4. Imports & Namespacing
import sys
from math import add, substract

# 2. Functions & Classes
class Calculator:
    def calculate(self, method, val1, val2):
        # 3. Control Flow Statements
        if method == 'add':
            return add(val1, val2)
        if method == 'substract':
            return substract(val1, val2)


if __name__ == '__main__':
    # 1. Variables & Data Types
    method = sys.argv[1]
    val1 = int(sys.argv[2])
    val2 = int(sys.argv[3])

    calc = Calculator()
    result = calc.calculate(method, val1, val2)
    print(result)
