# Week 1: Python Fundamentals

## Project Overview

This repository documents my first week of learning Python programming. The project contains implementation of basic to intermediate Python concepts including variables, data types, operators, conditional statements, loops, and a final calculator project.

## Learning Objectives

By the end of week 1, I aimed to understand:
- Python syntax and basic program structure
- How to handle user input and display output
- Different types of operators and their usage
- Decision making using conditional statements
- Iteration using for and while loops
- Building interactive command-line applications

## Topics Covered

### 1. Variables and Data Types

Python supports multiple data types including integers, floats, strings, and booleans. Variables are dynamically typed, meaning type is determined at runtime based on assigned value.

Key concepts learned:
- Variable naming conventions (lowercase with underscores)
- Type inference in Python
- Type conversion using int(), float(), str(), bool()
- Checking types using type() function

### 2. Input and Output

Input handling:
- input() function always returns string data
- Need explicit type conversion for numeric input
- Case-insensitive input processing using .lower() or .upper()

Output formatting:
- print() function for displaying output
- f-strings for embedding variables in strings (Python 3.6+)
- String concatenation using + operator
- sep and end parameters in print()

### 3. Arithmetic Operators

Python provides seven arithmetic operators:

| Operator | Name | Example | Result |
|----------|------|---------|---------|
| + | Addition | 10 + 3 | 13 |
| - | Subtraction | 10 - 3 | 7 |
| * | Multiplication | 10 * 3 | 30 |
| / | Division | 10 / 3 | 3.333 |
| % | Modulus (remainder) | 10 % 3 | 1 |
| ** | Exponentiation | 10 ** 3 | 1000 |
| // | Floor division | 10 // 3 | 3 |

Important notes:
- Division (/) always returns float
- Modulus (%) works with integers and floats
- Floor division (//) returns integer rounded down
- Division by zero causes ZeroDivisionError

### 4. Comparison Operators

Comparison operators return boolean values (True/False):

- > : Greater than
- < : Less than  
- == : Equal to
- != : Not equal to
- >= : Greater than or equal to
- <= : Less than or equal to

These are commonly used in conditional statements and loops.

### 5. Logical Operators

Logical operators combine boolean expressions:

- **and** : Returns True only if both conditions are True
- **or** : Returns True if at least one condition is True
- **not** : Reverses the boolean value

Truth table for 'and':
| A | B | A and B |
|---|---|---------|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | F |

Truth table for 'or':
| A | B | A or B |
|---|---|--------|
| T | T | T |
| T | F | T |
| F | T | T |
| F | F | F |

### 6. Conditional Statements

**if statement:** Executes block if condition is True
**elif statement:** Additional conditions after if
**else statement:** Executes when all conditions are False

Nested conditions:
- Conditional statements can be placed inside other conditional statements
- Each level requires proper indentation (usually 4 spaces)
- Helps implement complex decision trees

Practical applications implemented:
- Traffic light system (stop, ready, go logic)
- Movie ticket pricing based on age and ID verification
- Age group categorization (adults, teens, children)

### 7. For Loops

For loops are used when the number of iterations is known in advance.

**Syntax:** `for variable in iterable:`

**Iterables commonly used:**
- Lists: `[1, 2, 3, 4, 5]`
- Strings: `"hello"`
- Range objects: `range(start, stop, step)`

**range() function parameters:**
- start: Beginning value (inclusive, default 0)
- stop: Ending value (exclusive, required)
- step: Increment value (default 1)

**Applications implemented:**
- Calculating average of scores list
- Generating even and odd numbers
- Sum of first 50 natural numbers
- Counting vowels in strings
- Finding minimum and maximum in lists
- Creating multiplication tables
- Reversing strings
- Counting even/odd numbers in lists
- Searching elements with break statement

### 8. While Loops

While loops are used when the number of iterations is unknown and depends on a condition.

**Syntax:** `while condition:`

**Key characteristics:**
- Condition checked before each iteration
- Loop continues until condition becomes False
- Must update loop variables to avoid infinite loops
- break statement can exit loop prematurely

**Applications implemented:**
- Sum of first n numbers
- Countdown timers
- Password validation (repeat until correct)
- Number doubling until reaching limit
- Factorial calculation
- Counting digits in a number
- Age validation with range checking
- Shopping list builder with break condition

**Common pitfalls and solutions:**
- Forgetting to update counter causes infinite loop
- Always ensure condition will eventually become False
- Use break for early termination when needed

## Final Project: Interactive Calculator

The week concludes with a comprehensive calculator application that integrates all learned concepts.

### Features

**Arithmetic Operations Module:**
- Addition, subtraction, multiplication
- Division with zero validation
- Modulus operation
- Exponentiation (power calculation)

**Pi Calculations Module:**
- Pi value from math module
- Pi multiplication by user input
- Circle circumference (2πr)
- Circle area (πr²)

**User Interface Features:**
- Menu-driven navigation
- Input validation for menu choices
- Division by zero error handling
- Continue/exit option after each operation
- Formatted output with visual separators

### Technical Implementation Details

**Module Import:** Uses Python's math module for pi constant

**Data Types:** 
- Float for all numeric calculations (supports decimals)
- String for menu interaction
- Boolean for loop control

**Error Handling:**
- Checks for division by zero before performing operation
- Validates menu choice input
- Handles invalid input with error message

**Loop Structure:**
- Outer while loop keeps calculator running
- Inner if-elif-else handles menu choices
- Break statements exit loops when user chooses

## Learning Outcomes

After completing week 1, I have demonstrated ability to:

1. Write Python scripts with proper syntax and indentation
2. Accept and process user input with appropriate type conversion
3. Perform arithmetic, comparison, and logical operations
4. Implement decision making using if-elif-else structures
5. Create nested conditions for complex logic
6. Use for loops with lists, strings, and range objects
7. Use while loops for condition-based iteration
8. Control loop flow using break statements
9. Build interactive command-line applications
10. Handle common errors like division by zero
11. Import and use standard library modules

## Programs Developed

Total 21 practice programs were implemented:

**Day 1 Programs (3):**
1. Age and price input system
2. Student status boolean converter

**Day 2 Programs (18):**
3. Arithmetic operations with all 7 operators
4. Comparison operations demo
5. Logical operations demo
6. Traffic light system
7. Movie ticket system with nested conditions
8. Average score calculator
9. Even numbers generator (for loop)
10. Odd numbers generator (for loop)
11. Sum of first 50 natural numbers
12. Vowel counter in strings
13. Largest number finder in list
14. Smallest number finder in list
15. Multiplication table generator
16. String reverser
17. Even/odd counter in list
18. Number searcher with break
19. Password validator (while loop)
20. Shopping list builder
21. Interactive calculator (final project)

## Technical Specifications

- **Programming Language:** Python 3.x
- **Total Lines of Code:** Approximately 425
- **External Modules:** math (standard library only)
- **Concepts Covered:** 8 major topics
- **Practice Programs:** 21
- **Development Time:** 8-10 hours

## Common Errors and Solutions

**Error 1: TypeError when concatenating string and int**
- Cause: input() always returns string
- Solution: Use int() or float() to convert

**Error 2: Infinite loop in while**
- Cause: Loop variable not updated
- Solution: Ensure counter increments or condition changes

**Error 3: ZeroDivisionError**
- Cause: Attempting division by zero
- Solution: Check divisor before division

**Error 4: IndentationError**
- Cause: Inconsistent or missing indentation
- Solution: Use consistent 4 spaces for each indentation level

**Error 5: NameError for undefined variable**
- Cause: Variable used before assignment
- Solution: Initialize variable before use

## How to Run

1. Ensure Python 3.x is installed on your system
2. Download or clone the repository containing week1_python.py
3. Open terminal or command prompt
4. Navigate to the file directory
5. Execute: `python week1_python.py`
6. Follow interactive prompts

## Next Steps (Week 2)

The following topics are planned for week 2:
- Functions (definition, parameters, return values)
- List methods (append, remove, pop, sort, reverse)
- Dictionary operations (key-value pairs)
- Tuple properties and usage
- Set operations
- String methods (split, join, replace, strip)
- File I/O (reading and writing files)
- Exception handling with try-except blocks

## Repository Contents

- `week1_python.py` - Complete implementation of all week 1 concepts and final project
- `README.md` - This documentation file

## Usage Guidelines

This code is for educational purposes. It demonstrates learning progression and can be used as:
- Reference for Python beginners
- Teaching material for basic concepts
- Practice exercises for loops and conditions
- Template for calculator implementation

## Version Information

- **Version:** 1.0
- **Release Date:** Week 1 completion
- **Python Compatibility:** 3.6 and above

## Author: Hamis_Mehmood

Week 1 Python Learning Project

## License

Educational use permitted. Code may be freely used for learning purposes.
