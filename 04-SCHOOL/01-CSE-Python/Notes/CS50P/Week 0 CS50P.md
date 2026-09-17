---
type: note
tags: [programming, cs50p]
timeline: now
---

# Python CS50 Week 0 Notes

## Functions

---

- Functions are verbs or actiosn that hte computer or computer language will already know how to perform.
- In ```hello.py``` program, the ```print``` function knows how to print to the terminal window.
- The ```print``` function takes arguments. In this case, ```"hello, world"``` = argument.

## Bugs

---

- Bugs are natural part of coding, These mistakes, problems for you to solve.
- Error messages can often inform you of your mistakes and provide clues on how to fix them. However, there will be many times when the interpreter is not this helpful.

## Strings and Parameters

- A string, known as a ```str``` in Python, is a sequence of text.

## Formatting Strings

- ```# Ask the user for their name  name = input("What's your name? ")  print(f"hello, {name}")```
- notice the ```f``` in ```print(f"hello, {name}")```. This ```f``` is a special indicator for Python to treat this string a special way, different than previous approaches we have illustrated in this lecture. Expect that you will be using this style of string quite frequently in this course.

### More on Strings

- You should never expect your user to cooperate as intended. Therefore, you will need to ensure that the input of your user is corrected or checked.
- It turns out that bilt into strings is the ability to remove whitespace from a string.
- by utilizing the ```strip``` method on ```name```(for example, ```name = name.strip()```), you will remove any whitespace from the left and right of the user's input. You can modify your code to be:

``` python
# Ask the user for their name
name = input("What's your name? ")

# remove whitespace from the string
name = name.strip()

# Print the output
print(f"hello, {name}")
```

- Rerunning this program, regardless of how many spaces you type before or after the name, it will strip off all the whtitespace.
- Using the ```title``` method, it would title case the user's name:

``` python
# Ask the user for their name
name = input("What's your name?)

# Print the output
print(f"hello, {name}")
```

- You can learn more about strings in Python's documentation on [str](https://docs.python.org/3/library/stdtypes.html#str) 

## Integers or int

- in Python, an interger is referred to as an ```int```.
- in the world of mathematics, we are familiar with +,-,*,/, and % operators. That last operator ```%``` or modulo operator may not be very gamiliar to you.
- You don't have to use the text editor window to run Python code. Down in your terminal, you can run ```Python``` alone. You will be presented with ```>>>``` in the terminal window. You can then run live, interactive code. You could type ```1+1```, and it will run that calculation. This mode will not commonly be used during this course. 
- Opening up VS Code again, we can type ```code calculator.py``` in the terminaL. tHIS WILL CREATE A NEW FILE IN WHICH WE WILL CREATE OUR OWN CALCULATOR.
- first we can declare a few variables.

``` Python
x = 1
y = 2

z = x + y

print(z)
```

- Naturally, when we run ```python calculator.py``` we get the result in the terminal window of ```3```. We can make this more interactive using the ```input``` funtion.

``` python
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
```

- Running this program, we discover that the output is incorrect as ```12```. Why might this be?
- Prior, we have seen how the ```+``` sign concatenates 'to join or merge two or more sequences end-to-end to create a single, larger sequence' two strings. Because your input from your keyboard on your computer comes into the interpreter as text, it is treated as a string. We, therefore, need to convert thsi input from a string to an integer. We can do so as follows:

``` python
x = input("What's x? ")
y = input("What's y? ")

z = int(x) + int(y)

print(z)
```

- The result is now correct. The use of ```int(x)``` is called "casting" where a value is temporarily changed from one type of variable (in this case, a string) to another (here, an integer).
- We can further improve our program as follows:

``` python
x = int(input("What's x? "))
y = int(input("What's y? "))

pring(x + y)
```

- This illustrates that you can run functions on functions. The inner function is run first, and then the outer one is run. First, the ```input``` function is run. Then, the ```int``` function.
- You can learn more in Pythnon's documentation of [int](https://docs.python.org/3/library/functions.html#int)

## Readability Wins

- When deciding on your approach to a coding task, remember that one could make a reasonable argument for many approaches to the same problem.
- Regardless of what approach you take to a programming task, remember that your code must be readable. You should use comments to give yourself and others clues about what your code is doing. Further, you should create code in a way that is readable.

## Float Basics

- A floating point valueis a real number that hasa decimal point in it, such as ```0.52```.
- You can change your code to support floats as flollows:

``` python
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + Y)
```

- This change allows your user to enter ```1.2``` and ```3.4``` to present a total of ```4.6```.
- Let's imagine, however, that you want to round the total to the nearest integer. Looking at the Python documentation for ```round```, you'll see that the available arguments are ```round(number[, ndigits])```. Those square brackets indicate that something optional can be specified by the programmer. Therefore, you could do ```roudn(n) to round a digit to its nearest ineger. Alternatively,  you could code as follows:

``` python
# Get the user's input
x = float(input("What's x?" ))
y = float(input("What's y? "))

# Create a rounded result
z = round(x+y)

# Print the formatted result
print(f"{z:,}")
```

- Though quite cryptic, that ```print(f"{z:,}")``` creates a scenario where the outputted ```z``` will include commas where the result could look like ```1,000``` or ```2,500```.

## More on Floats

- How can we round floating point values? First, modify your code as follows:

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = round(x / y)

# Print the result
print(z)
```

- When inputting ```2``` as x and ```3``` as y, the result z is ```0.6666666```, seemingly goiing on to infinity as we might expect.
- Let's imagine that we want to round this down. We could modify our code as follows:

``` python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result and round
z = round(x / y, 2)

# Print the result
print(z)
```

- As we might expect, thi will round the result to the nearest two decimal places.
- We could also us an ```fstring``` to format the output as follows:

```python
# Get the user's input
x = float(input("What's x? "))
y = float(input("What's y? "))

# Calculate the result
z = x / y

# Print the result
print(f"{z:.2f}")
```

- This cryptic ```f-string``` cdoe displays the same as our prior rounding strategy.

## Def

- Wouldn't it be nice to create our own functions?
- Let's brin back our final code of hello.py