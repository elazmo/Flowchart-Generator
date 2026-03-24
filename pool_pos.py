SEPARATOR = "---------------------------"


def get_integer_input(prompt):
    """Prompt user for input and validate it is a whole integer."""
    while True:
        value = input(prompt)
        if '.' in value:
            print("Error: Please enter a valid integer using digits.")
            continue
        try:
            return int(value)
        except ValueError:
            print("Error: Please enter a valid integer using digits.")


def calculate_cheapest(adults, children):
    """Return (total_cost, receipt_lines) using the cheapest ticket combination."""
    best_cost = float('inf')
    best_receipt = []

    # Try every valid combination of Family Pass A and Family Pass B
    for fa in range(adults // 2 + 1):
        for fb in range((adults - 2 * fa) + 1):
            rem_adults = adults - 2 * fa - fb
            rem_children = children - 2 * fa - 3 * fb

            if rem_children < 0:
                continue  # Not enough children to fill these passes

            cost = 16 * fa + 16 * fb + 5 * rem_adults + 4 * rem_children

            if cost < best_cost:
                best_cost = cost
                receipt = []
                if fa > 0:
                    receipt.append((fa, "Family Pass A", 16 * fa))
                if fb > 0:
                    receipt.append((fb, "Family Pass B", 16 * fb))
                if rem_adults > 0:
                    receipt.append((rem_adults, "Adult", 5 * rem_adults))
                if rem_children > 0:
                    receipt.append((rem_children, "Child", 4 * rem_children))
                best_receipt = receipt

    return best_cost, best_receipt


def print_receipt(receipt, total):
    print("\nReceipt:")
    for qty, name, price in receipt:
        label = f"{qty}x {name}"
        print(f"{label:<20}: ${price:5.2f}")
    print(SEPARATOR)
    print(f"{'TOTAL':<20}: ${total:5.2f}")


def main():
    print("--- Codetown Public Pool POS ---")

    while True:
        start = input("\nPress Enter to exit or type any key to start a new sale: ")
        if start == "":
            break

        # Validate adults
        while True:
            adults = get_integer_input("Enter number of adults: ")
            if adults < 1:
                print("Error: At least one adult is required for supervision.")
            else:
                break

        # Validate children
        while True:
            children = get_integer_input("Enter number of children: ")
            if children < 0:
                print("Error: Number of children cannot be negative.")
            else:
                break

        total, receipt = calculate_cheapest(adults, children)
        print_receipt(receipt, total)


if __name__ == "__main__":
    main()
