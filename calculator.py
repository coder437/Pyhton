operand_one = int(input())
operand_two = int(input())
operator = input()
def calculation():
    if operator == "+":
        print(operand_one+operand_two)
    elif operator == "-":
        print(operand_one-operand_two)
    elif operator == "*":
        print(operand_one*operand_two)
    elif operator == "/":
        print(operand_one/operand_two)
    else:
        print("please try again")

while True:
    calculation()




