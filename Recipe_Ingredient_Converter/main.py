from unit_converter import cups_to_millileters, teaspoons_to_millileters

def main():
    try:
        quantity = float(input("Enter the quantity of the ingredient: "))
        unit = input("Enter the unit to convert from (cups or teaspoons): ").lower()
        if unit == "cups":
            print(f"{quantity} cups is {cups_to_millileters(quantity)} millileters.")
        elif unit == "teaspoons":
            print(f"{quantity} teaspoons is {teaspoons_to_millileters(quantity)} millileters.")
    except ValueError:
        print("Please enter a valid numeric quantity.")

if __name__ == "__main__":
    main()