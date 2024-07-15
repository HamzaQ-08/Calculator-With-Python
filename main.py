def add(x, y):
  return x + y

def sub(x, y):
  return x - y

def mult(x, y):
  return x * y

def div(x, y):
  return x / y

def sqr(x):
  return x * x

def cube(x):
  return x * x * x

def per(x, y):
  return (x / y) * 100

def main():
  print("Welcome to the calculator")
  print("\nEnter the number according to your choice")
  print("1. ADD")
  print("2. SUBTRACTION")
  print("3. MULTIPLICATION")
  print("4. DIVISION")
  print("5. SQUARE")
  print("6. CUBE")
  print("7. PERCENT")
  print("8. EXIT")

  while True:
      choice = input("\nEnter your choice (1/2/3/4/5/6/7/8): ")
      if choice in ('1', '2', '3', '4', '5', '6', '7', '8'):
          if choice == '1':
              num1 = float(input("\nEnter your first number: "))
              num2 = float(input("\nEnter your second number: "))
              print(f'{num1} + {num2} = {add(num1, num2)}')

          elif choice == '2':
              num1 = float(input("\nEnter your first number: "))
              num2 = float(input("\nEnter your second number: "))
              print(f'{num1} - {num2} = {sub(num1, num2)}')

          elif choice == '3':
              num1 = float(input("\nEnter your first number: "))
              num2 = float(input("\nEnter your second number: "))
              print(f'{num1} * {num2} = {mult(num1, num2)}')

          elif choice == '4':
              num1 = float(input("\nEnter your first number: "))
              num2 = float(input("\nEnter your second number: "))
              print(f'{num1} / {num2} = {div(num1, num2)}')

          elif choice == '5':
              num1 = float(input("\nEnter your number: "))
              print(f'{num1}^2 = {sqr(num1)}')

          elif choice == '6':
              num1 = float(input("\nEnter your number: "))
              print(f'{num1}^3 = {cube(num1)}')

          elif choice == '7':
              num1 = float(input("\nEnter your first number: "))
              num2 = float(input("\nEnter your second number: "))
              print(f'{num1} is {per(num1, num2)}% of {num2}')

          elif choice == '8':
              print("\nThank you for using the calculator. Goodbye!")
              break
      else:
          print("\nInvalid input, please enter a number between 1 and 8.")

if __name__ == "__main__":
  main()
