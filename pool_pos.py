SEPARATOR = "---------------------------"

PRICE_ADULT = 5
PRICE_CHILD = 4
PRICE_FAMILY_A = 16
PRICE_FAMILY_B = 16

FAMILY_A_ADULTS = 2
FAMILY_A_CHILDREN = 2
FAMILY_B_ADULTS = 1
FAMILY_B_CHILDREN = 3

ERR_INVALID_INT = "Error: Please enter a valid integer using digits."


def get_integer_input(prompt):
    while True:
        value = input(prompt)
        if '.' in value:
            print(ERR_INVALID_INT)
            continue
        try:
            return int(value)
        except ValueError:
            print(ERR_INVALID_INT)


def get_validated_input(prompt, min_value, error_msg):
    while True:
        value = get_integer_input(prompt)
        if value >= min_value:
            return value
        print(error_msg)


def calculate_cheapest(adults, children):
    best_cost = float('inf')
    best_receipt = []

    for fa in range(adults // FAMILY_A_ADULTS + 1):
        for fb in range(adults - FAMILY_A_ADULTS * fa + 1):
            rem_adults = adults - FAMILY_A_ADULTS * fa - FAMILY_B_ADULTS * fb
            rem_children = children - FAMILY_A_CHILDREN * fa - FAMILY_B_CHILDREN * fb

            if rem_children < 0:
                break  # Larger fb only increases child usage — no point continuing

            cost = (PRICE_FAMILY_A * fa + PRICE_FAMILY_B * fb
                    + PRICE_ADULT * rem_adults + PRICE_CHILD * rem_children)

            if cost < best_cost:
                best_cost = cost
                best_receipt = [
                    (qty, name, unit * qty)
                    for qty, name, unit in [
                        (fa,          "Family Pass A", PRICE_FAMILY_A),
                        (fb,          "Family Pass B", PRICE_FAMILY_B),
                        (rem_adults,  "Adult",         PRICE_ADULT),
                        (rem_children,"Child",         PRICE_CHILD),
                    ]
                    if qty > 0
                ]

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
        if input("\nPress Enter to exit or type any key to start a new sale: ") == "":
            break

        adults = get_validated_input(
            "Enter number of adults: ", 1,
            "Error: At least one adult is required for supervision."
        )
        children = get_validated_input(
            "Enter number of children: ", 0,
            "Error: Number of children cannot be negative."
        )

        total, receipt = calculate_cheapest(adults, children)
        print_receipt(receipt, total)


if __name__ == "__main__":
    main()
