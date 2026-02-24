def format_currency(amount):
    return "$" + str(amount)


def calculate_tax(amount):
    return amount * 0.18


def generate_invoice(amount):
    tax = calculate_tax(amount)
    total = amount + tax
    return total
