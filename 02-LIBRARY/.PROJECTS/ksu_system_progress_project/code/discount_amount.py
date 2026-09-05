from percent_of import percent_of


def discount_amount(price, rate):
    da = percent_of(price, rate)
    return da


print(discount_amount(80, 0.25))
