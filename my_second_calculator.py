import operator
SIGNS = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.div}


def calculator():
    first_number = int(raw_input("Please choose your first number: "))
    op = raw_input("What do you want to do? +, -, /, or *: ")
    second_number = int(raw_input("Please choose your second number: "))
    print "The answer is :", SIGNS[op](first_number, second_number)

if __name__ == "__main__":
    calculator()
