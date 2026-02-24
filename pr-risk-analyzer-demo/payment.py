def process_payment(amount):
    print("Processing payment...")

    discount = 0
    if amount > 100:
        discount = amount * 0.1
    if amount > 500:
        discount = amount * 0.2

    final_amount = amount - discount

    fee = 0
    if final_amount > 1000:
        fee = final_amount * 0.05
    elif final_amount > 500:
        fee = final_amount * 0.03
    else:
        fee = final_amount * 0.01

    total = final_amount + fee

    print("Total:", total)
    return total
