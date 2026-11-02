def add(num1, num2):
    return num1 + num2

def subtruct(num1, num2):
    return num1 - num2

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    choice = input("Add or Subtruct (+ / -): ")

    if choice == "+":
        print(add(num1, num2))
    if choice == "-":
        print(subtruct(num1, num2))
    
    return 0

if "__main__" == __name__:
    main()