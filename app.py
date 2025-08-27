from calculator import add, sub, mul, div

def read_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    print("Simple Calculator (enter q to quit)")
    while True:
        print("\nChoose operation:")
        print("1) Add  2) Subtract  3) Multiply  4) Divide  5) Quit")
        choice = input("Select 1-5: ").strip()

        if choice in ("5", "q", "Q"):
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4"):
            print("Invalid choice. Try again.")
            continue

        a = read_number("Enter first number: ")
        b = read_number("Enter second number: ")

        if choice == "1":
            result = add(a, b)
        elif choice == "2":
            result = sub(a, b)
        elif choice == "3":
            result = mul(a, b)
        else:
            result = div(a, b)

        print(f"Result: {result}")

if __name__ == "__main__":
    main()
