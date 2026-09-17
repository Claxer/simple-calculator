# My First Work, a Scientific Calculator

## Description

A Python-based scientific calculator that performs a wide variety of mathematical operations through a menu-driven interface. It includes basic arithmetic, scientific functions, trigonometric calculations, logarithms, mathematical constants, and calculation history management.

## Features

### Basic Operations# My First Work, a Scientific Calculator

## Description

A Python-based scientific calculator that performs a wide variety of mathematical operations through a menu-driven interface. It includes basic arithmetic, scientific functions, trigonometric calculations, logarithms, mathematical constants, percentage calculations, number calculations, and calculation history management.

## Features

### Basic Operations

* Addition
* Subtraction
* Multiplication
* Division
* Exponent
* Modulus
* Floor Division

### Scientific Functions

* Square Root
* Percentage
* Factorial
* Cube Root
* Absolute Value
* Reciprocal (1/x)
* Pi (π)
* Euler's Number (e)
* Logarithm (log₁₀)
* Natural Logarithm (ln)
* Sine (sin)
* Cosine (cos)
* Tangent (tan)

### Additional Mathematical Functions

* Average of Multiple Numbers
* Minimum Value
* Maximum Value
* Percentage Increase
* Percentage Decrease
* GCD (Greatest Common Divisor)
* LCM (Least Common Multiple)
* Permutation (nPr)
* Combination (nCr)
* Round Number to a Selected Number of Decimal Places

### History Management

* View History
* Clear History
* Save History to a Text File
* Automatically record completed calculations
* Store different types of calculations in the same history list

## Technologies Used

* Python 3
* Python `math` Module
* Lists
* Text File Handling

## What I Learned

* Variables
* User input
* Menu-driven program design
* `if`, `elif`, and `else` statements
* While loops
* `continue` and `break` statements
* Functions from Python's `math` module
* Basic arithmetic operators
* Exponentiation (`**`)
* Modulus (`%`)
* Floor division (`//`)
* Calculating square roots
* Calculating cube roots
* Calculating factorials
* Calculating percentages
* Finding absolute values
* Calculating reciprocals
* Working with mathematical constants (`math.pi` and `math.e`)
* Calculating logarithms using `math.log10()`
* Calculating natural logarithms using `math.log()`
* Using trigonometric functions:

  * `math.sin()`
  * `math.cos()`
  * `math.tan()`
* Converting degrees to radians using `math.radians()`
* Finding the average of multiple numbers
* Finding minimum and maximum values
* Calculating percentage increases
* Calculating percentage decreases
* Finding the Greatest Common Divisor using `math.gcd()`
* Finding the Least Common Multiple using `math.lcm()`
* Calculating permutations using `math.perm()`
* Calculating combinations using `math.comb()`
* Rounding decimal values using `round()`
* Error handling using `try` and `except`
* `ValueError` exception handling
* Input validation
* Preventing division by zero
* Preventing invalid logarithm calculations
* Checking for negative values
* Checking for invalid factorial values
* Checking whether `r` is greater than `n` in permutations and combinations
* Comparison operators (`==`, `!=`, `<`, `>`, `<=`)
* Membership operator (`in`)
* Type conversion using `float()` and `int()`
* String methods such as `.lower()`
* Lists
* Using `list.append()` to store calculation history
* Using `sum()` to calculate totals
* Using `len()` to count values
* Using `min()` to find the smallest value
* Using `max()` to find the largest value
* Using `for` loops to display stored data
* Writing data to a text file
* File handling using `open()`
* Using different file modes (`"w"`)
* Using `with open()` for safe file handling
* Recording and managing calculation history
* Building a console-based scientific calculator

## How to Run

1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run:

```bash
python calculator.py
```

## Sample Functions

```text
Addition:
5 + 3 = 8

Square Root:
√25 = 5

Factorial:
5! = 120

Cube Root:
∛125 = 5

Percentage:
25% = 0.25

Absolute Value:
|-15| = 15

Reciprocal:
1/4 = 0.25

Pi:
π = 3.141592653589793

Euler's Number:
e = 2.718281828459045

Logarithm:
log(100) = 2

Natural Logarithm:
ln(2.718281828) = 1

Sine:
sin(30°) = 0.5

Cosine:
cos(60°) = 0.5

Tangent:
tan(45°) = 1

Average:
Average of 10, 20, 30 = 20

Minimum Value:
Minimum of 10, 5, 20 = 5

Maximum Value:
Maximum of 10, 5, 20 = 20

Percentage Increase:
100 to 120 = 20%

Percentage Decrease:
100 to 80 = 20%

GCD:
GCD(12, 18) = 6

LCM:
LCM(4, 6) = 12

Permutation:
5P2 = 20

Combination:
5C2 = 10

Round Number:
Round(3.14159, 2) = 3.14
```

## Current Calculator Operations

The calculator currently contains **33 menu options**:

1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponent
6. Modulus
7. Floor Division
8. Square Root
9. Percentage
10. Factorial
11. Cube Root
12. Absolute Value
13. Reciprocal
14. Pi
15. Euler's Number
16. Logarithm
17. Natural Logarithm
18. Sine
19. Cosine
20. Tangent
21. View History
22. Clear History
23. Save History
24. Average
25. Minimum Value
26. Maximum Value
27. Percentage Increase
28. Percentage Decrease
29. GCD
30. LCM
31. Permutation
32. Combination
33. Round Number

## Error Handling

The calculator includes basic error handling to prevent invalid calculations and unexpected program crashes.

Examples include:

* Preventing division by zero
* Preventing modulus by zero
* Preventing floor division by zero
* Preventing square roots of negative numbers
* Preventing factorials of negative numbers
* Preventing factorials of decimal values
* Preventing logarithms of zero or negative numbers
* Checking invalid user input
* Checking negative values where they are not allowed
* Checking when `r` is greater than `n`
* Checking invalid decimal places for rounding

## History System

The calculator keeps track of calculations while the program is running.

The history system allows the user to:

* View previous calculations
* Clear all stored calculations
* Save calculations to `history.txt`
* Automatically add new calculations to the history list

Example:

```text
5.0 + 3.0 = 8.0
√25.0 = 5.0
5! = 120
GCD(12, 18) = 6
5P2 = 20
5C2 = 10
```

## Project Purpose

This project was created as a beginner Python project to practice programming fundamentals and gradually build a more complete scientific calculator.

The project started with basic arithmetic operations and was expanded by adding scientific calculations, trigonometric functions, logarithms, constants, calculation history, file handling, number analysis, percentage calculations, and combinatorial mathematics.

It demonstrates how a simple console program can be improved by continuously adding new features while keeping the original functionality.

## Future Improvements

* Degree/Radian Mode
* Inverse Trigonometric Functions (sin⁻¹, cos⁻¹, tan⁻¹)
* Hyperbolic Functions
* Nth Root Calculator
* Scientific Notation
* Memory Functions (MS, MR, MC, M+, M-)
* Previous Answer (ANS)
* Random Number Generator
* Prime Number Checker
* Number System Converter (Binary, Octal, Hexadecimal)
* Expression Evaluation using Parentheses
* Statistics Calculator
* Graph Plotting
* Update my Graphical User Interface (GUI) of a calculator and add the functions


- Addition
- Subtraction
- Multiplication
- Division
- Exponent
- Modulus
- Floor Division

### Scientific Functions

- Square Root
- Percentage
- Factorial
- Cube Root
- Absolute Value
- Reciprocal (1/x)
- Pi (π)
- Euler's Number (e)
- Logarithm (log₁₀)
- Natural Logarithm (ln)
- Sine (sin)
- Cosine (cos)
- Tangent (tan)

### History Management

- View History
- Clear History
- Save History to a Text File

## Technologies Used

- Python 3
- Python `math` Module

## What I Learned

- Variables
- User input
- Menu-driven program design
- `if`, `elif`, and `else` statements
- While loops
- `continue` and `break` statements
- Functions from Python's `math` module
- Basic arithmetic operators
- Exponentiation (`**`)
- Modulus (`%`)
- Floor division (`//`)
- Calculating square roots
- Calculating cube roots
- Calculating factorials
- Calculating percentages
- Finding absolute values
- Calculating reciprocals
- Working with mathematical constants (`math.pi` and `math.e`)
- Calculating logarithms using `math.log10()`
- Calculating natural logarithms using `math.log()`
- Using trigonometric functions:
  - `math.sin()`
  - `math.cos()`
  - `math.tan()`
- Converting degrees to radians using `math.radians()`
- Rounding decimal values using `round()`
- Error handling using `try` and `except`
- `ValueError` exception handling
- Input validation
- Preventing division by zero
- Preventing invalid logarithm calculations
- Comparison operators (`==`, `!=`, `<`, `>`, `<=`)
- Membership operator (`in`)
- Type conversion using `float()` and `int()`
- String methods such as `.lower()`
- Lists
- Using `list.append()` to store calculation history
- Using `for` loops to display stored data
- Writing data to a text file
- File handling using `open()`
- Using different file modes (`"w"`)
- Using `with open()` for safe file handling
- Recording and managing calculation history
- Building a console-based scientific calculator

## How to Run

1. Clone or download this repository.
2. Open a terminal or command prompt.
3. Navigate to the project folder.
4. Run:

```bash
python calculator.py
```

## Sample Functions

```
Addition:
5 + 3 = 8

Square Root:
√25 = 5

Factorial:
5! = 120

Cube Root:
∛125 = 5

Percentage:
25% = 0.25

Absolute Value:
|-15| = 15

Reciprocal:
1/4 = 0.25

Pi:
π = 3.141592653589793

Euler's Number:
e = 2.718281828459045

Logarithm:
log(100) = 2

Natural Logarithm:
ln(2.718281828) = 1

Sine:
sin(30°) = 0.5

Cosine:
cos(60°) = 0.5

Tangent:
tan(45°) = 1
```

## Future Improvements

- Degree/Radian Mode
- Inverse Trigonometric Functions (sin⁻¹, cos⁻¹, tan⁻¹)
- Hyperbolic Functions
- Nth Root Calculator
- Scientific Notation
- Memory Functions (MS, MR, MC, M+, M-)
- Previous Answer (ANS)
- Random Number Generator
- Prime Number Checker
- GCD and LCM Calculator
- Number System Converter (Binary, Octal, Hexadecimal)
- Expression Evaluation using Parentheses
- Statistics Calculator
- Graph Plotting
- Update my Graphical User Interface (GUI) of a calculator and add the functions.
