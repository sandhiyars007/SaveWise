import re


def analyze_budget(text):

    lines = text.splitlines()

    income = 0
    expenses = {}

    expense_keywords = [
        "rent",
        "food",
        "transport",
        "shopping",
        "bills",
        "electricity",
        "water",
        "internet",
        "education",
        "medical",
        "entertainment",
        "other"
    ]

    for line in lines:

        line = line.strip().lower()

        if not line:
            continue

        numbers = re.findall(r"\d+(?:,\d+)*(?:\.\d+)?", line)

        if not numbers:
            continue

        amount = float(numbers[-1].replace(",", ""))

        # Income detection
        if any(word in line for word in [
            "salary",
            "income",
            "monthly income"
        ]):

            income = amount

        else:

            for category in expense_keywords:

                if category in line:

                    expenses[category] = amount

                    break

    total_expense = sum(expenses.values())

    balance = income - total_expense

    return {
        "income": income,
        "expenses": expenses,
        "total_expense": total_expense,
        "balance": balance
    }
