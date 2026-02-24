def process_payment(amount):
    print("Processing payment...")

    if amount > 500:
        discount = amount * 0.1
    else:
        discount = 0

    final_amount = amount - discount

    # Complex logic
    if final_amount > 1000:
        fee = final_amount * 0.05
    elif final_amount > 500:
        fee = final_amount * 0.03
    else:
        fee = final_amount * 0.01

    total = final_amount + fee

    print("Total payment:", total)

    return total
