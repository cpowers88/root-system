---
type: note
timeline: reference
tags: [school, cse-1321, python, fall-2026]
course: CSE 1321
created: 2026-08-27
---

# cse_notes_mod_1a
## Syntax

## Python Syntax
### What are comments?
- When you write code, sometimes it is important to leave some written messages to:
	- Explain or document what your code is doing
	- Leave a message to yourself or another
	- Explain or document how to use your code
	- Leave a placeholder code or To Do
- Comments are not executed by the computer and are completely ignored.
- In Python we use Single-line and Multi-line comments
	- **Single line** simply starts with a single "#" character making the line un-executable.
	- **Multi-line** are denoted by ['''] or ["""] before and after the comment with the same un-executable result.

### What are indentations?
- In Python, indentations are CRUCIAL.
- Indentations are used to group lines of code and to establish a hierarchy.
- Think of them like bullet points in Python.

## Brief introduction to Types
- **Data Types** are used to distinguish between characters and numbers
	- Strings, this type is used to represent character or text values. To let the program know we are using a string we enclose it with single ' or ".
	- Numbers, this type is used to perform math operations, we can define a numeric data type by simply writing the number itself.
		- So with these rules we see 3.14 isn't the same as "3.14", with the latter being in string format.

## How to start writing code
- Most programming languages start with **Skeleton Code**.
	- Skeleton code/programs are the smallest program you can write.
	- The code is the bare minimum for a program to successfully run, therefore it does nothing.
	- It just defines the entry/starting point of the program
- In Python, we do not have a formal Skeleton Code or Program. Instead we start writing functional code from the first line in our program.
- We **highly encourage** you to follow the following sample code as a template anytime writing code in Python.

## What is program flow?
- Like cooking a recipe or a set of instructions on how to tie a knot, it is important to know the order of execution of each step.
- Understanding the order of operation in programming is critical, if you disregard this your program will not work as expected or it could potentially crash.

### coding
- In Python code is executed line by line starting with line 1.
- The sample with the 'container' is an exception as containers are not executable code.

## Variables
- A **variable*8 is a name for a location in memory used to hold a data value.
- The most basic way of saving or storing data or the most basic way you can tell the computer to remember something.
- Think of it like a box:
	- You can store something inside of it.
	- You can always find that "something" by finding and opening that box.
	- You can always change and replace what you store inside of it.
- In Python we create variables by declaring it's identifier → then define a starting value
	- In Python, you must initialize a variable with a value.
- **Identifier** is the name you give to a variable.
	- You use this identifier to:
		- Create the variable
		- Read or recall the variable.
		- Update the variable
	- **Variable naming rules**
		- it must start with a letter or an (_), **it cannot** start with a number or a non-alphabetic character.
		- It cannot contain any blank or white-spaces
		- to name variable we use camelCaseNotation, TitleCaseNotation, snake_case_notation, Kebab-case-notation, to get around the no spaces allowed rule.
- It is good practice to give your variables meaningful names, this makes it easier to remember and for others to understand.
	- Be meaningful
	- Reflect the data they will store
	- Its name should "self-document" your code.
- Avoid extremely long names, python keywords and small variable names.
- In Python to create a variable we declare its identifier and assign a value by using the **Assignment Operator** (=).

## Output
- In python we use the print() function to produce an output, it is used to output he result of some calculation, or it can be used to debug your code.
- The print value by default will print whatever value you specify between the parentheses. It will also add a new line after if it finished printing the value.
	- Think of this as when it is done printing it will hit the 'enter' key, moving the type cursor to the line below, this behavior is what we call a print new line.
- If you choose to do so you can choose to end the print statement a certain way, to do this type ' , end = ""', you can add a string for the computer to add to the same line.

## Input Function
- Whenever we use the input function the computer will do 3 things.
	- Print a prompt that you will define when using the input function.
	- Wait for an answer. At this point he program is "frozen" until the user inputs something and presses the enter key.
	- As soon as this happens the computer will grab whatever value the user entered from the terminal.
- To make sure the program remembers a user input you must save inside a variable.

## Basic Math Operations
Addition: + , Subtraction - , Multipication * , Power ** , Division / (float) , Floor Division // (int) , Modulus %

 



