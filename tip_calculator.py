def calculate_tip(bill_amount, tip_percent):
    return round(bill_amount * tip_percent / 100, 2)


def split_bill(total, num_people):
    return round(total / num_people, 2)


if __name__ == "__main__":
    bill = float(input("Bill amount: $"))
    tip = float(input("Tip percentage: "))
    people = int(input("Number of people: "))

    tip_amount = calculate_tip(bill, tip)
    total = round(bill + tip_amount, 2)
    per_person = split_bill(total, people)

    print(f"\nTip: ${tip_amount}")
    print(f"Total: ${total}")
    print(f"Per person: ${per_person}")
