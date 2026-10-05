def generate_suggestions(
    income,
    expenses,
    total_expense,
    balance
):

    suggestions = []

    if income <= 0:

        suggestions.append(
            "⚠️ Monthly income could not be identified."
        )

        return suggestions

    if balance < 0:

        suggestions.append(
            "⚠️ Your expenses are higher than your income. "
            "Try reducing non-essential expenses first."
        )

    elif balance == 0:

        suggestions.append(
            "⚠️ Your entire income is being used. "
            "Try creating a small monthly savings target."
        )

    else:

        suggested_saving = balance * 0.60

        suggestions.append(
            f"💰 Based on your current balance, "
            f"you could consider setting aside around "
            f"₹{suggested_saving:,.2f} as planned savings."
        )

    # Find highest expense
    if expenses:

        highest_category = max(
            expenses,
            key=expenses.get
        )

        highest_amount = expenses[highest_category]

        percentage = (highest_amount / income) * 100

        if percentage > 25:

            suggestions.append(
                f"📌 {highest_category.title()} is taking about "
                f"{percentage:.1f}% of your income. "
                f"Consider setting a monthly limit for this category."
            )

        else:

            suggestions.append(
                f"📊 Your highest expense category is "
                f"{highest_category.title()} "
                f"(₹{highest_amount:,.2f})."
            )

    if balance > 0:

        suggestions.append(
            "🎯 Try maintaining an emergency fund "
            "before increasing discretionary spending."
        )

    return suggestions
