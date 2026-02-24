def calculate_tax(amount):
    return amount * 0.18

def format_currency(amount):
    return "$" + str(amount)

def generate_report(data):
    report = []
    for item in data:
        report.append(str(item))
    return report
