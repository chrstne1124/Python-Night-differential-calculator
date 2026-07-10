# Employee Pay Calculator

## Overview

This is a simple Python program that calculates an employee's total pay based on the number of hours worked and their hourly rate. It also takes into account overtime, holiday pay, and night shift differential.

The program asks the user for the required information and then calculates the final salary using a function called `computepay()`.

---

## Features

- Calculates regular pay
- Automatically computes overtime pay for hours worked over 40
- Adds a holiday premium if the employee worked on a holiday
- Applies a night shift differential when applicable
- Easy to use through user input

---

## How It Works

1. Enter the number of hours worked.
2. Enter the hourly rate.
3. Indicate whether the employee worked a night shift (`y` or `n`).
4. Indicate whether the employee worked on a holiday (`y` or `n`).
5. The program displays the total pay.

---

## Pay Rules

### Regular Pay
- Employees are paid their normal hourly rate for up to 40 hours.

### Overtime
- Any hours worked beyond 40 are paid at **1.5 times** the regular hourly rate.

### Holiday Pay
- Employees receive an additional **30% of their hourly rate** for every hour worked on a holiday.

### Night Shift
- After all other calculations are completed, employees working a night shift receive an additional **15%** on their total pay.

---

## Example

```
Enter Hours: 45
Enter Rate: 20
Night shift? (y/n): y
Holiday? (y/n): n

Pay: 1092.5
```

---

## Requirements

- Python 3.x

Run the program using:

```bash
python filename.py
```

Replace `filename.py` with the name of your Python file.

---

## Notes

This project was created as a simple exercise to practice:

- Functions
- Conditional statements (`if` and `else`)
- User input
- Boolean values
- Basic arithmetic operations in Python

It is intended for learning purposes and can be expanded by adding features such as tax deductions, bonuses, or different overtime rates.
