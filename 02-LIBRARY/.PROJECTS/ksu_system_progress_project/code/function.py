def add_this(a, b):  # def is the custom function label generator
    return a + b  # we use def to create function add_this using (a+b) as the argument


# then we tell this to return the result of a + b the value of the argument

no = add_this(5, 3)
print(no)
# a and b in the very first def line are the parameters - placeholder names for the function to expect.
# 5 and 3 (in add_this(5,3) line 7) are the arguments - the actual values you hand it when you call the it.
# return a + b doesn't "tell this to return the result" in the abstract - it hands the computed value back to twherever the function was called from, which is why no = add_this(5, 3) can capture it into no.
