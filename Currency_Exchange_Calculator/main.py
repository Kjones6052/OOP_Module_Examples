from currency_converter import usd_to_eur as to_euro, gbp_to_usd as to_usd

def main():
    try:
        amount = float(input("Enter the amount to convert: "))
        currency = input("Enter the currency to convert from (USD or GBP): ").upper()
        if currency == "USD":
            print(f"{amount} USD is {to_euro(amount)} EUR.")
        elif currency == "GBP":
            print(f"{amount} GBP is {to_usd(amount)} USD.")
        else:
            print("Invalid currency. Please enter 'USD' or 'GBP'.")
    except ValueError:
        print("Please enter a valid numerical amount.")

if __name__ == "__main__":
    main()