from percent_of import percent_of


def add_tax(a, b):

    c = percent_of(a, b)

    c = c + a
    return c
