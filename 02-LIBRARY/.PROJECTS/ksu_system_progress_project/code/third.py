from add_tax import add_tax


def bill_calculator(x, y, z):

    v = add_tax(x, y)
    tax_amount = v - x

    tip_amount = x * z  # total * decimal tip percentage = tip amount
    total = tip_amount + tax_amount + x

    final = f"Subtotal: ${x:.2f} \n Tax Amount: ${tax_amount:.2f} \n Tip Total: ${tip_amount:.2f} \n Total: ${total:.2f}"

    return final
