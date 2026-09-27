# BANKING-SYSTEM
# Financial Credit Assessment and Deposit Amortization System

A small Python console app for exploring three everyday banking-style calculations:

- fixed-deposit returns
- loan EMI and repayment schedules
- a simple income-versus-debt credit check

It is designed to be run from the terminal, one feature at a time, through a repeating menu.

## What it can do

### 1. Fixed Deposit Estimator

Enter a deposit amount and a term in whole years. The app chooses an illustrative interest rate from the deposit amount and shows both simple-interest and quarterly compound-interest values for every year in the term.

| Deposit amount | Annual rate used |
|---:|---:|
| Below 100000 | 5.50% |
| 100000 to 499999.99 | 6.25% |
| 500000 and above | 7.00% |

### 2. Loan Repayment Scheduler

Enter the loan amount, annual interest rate, and loan term in months. The app calculates the monthly EMI and prints a month-by-month breakdown of interest paid, principal paid, and remaining balance.
It also handles a 0% interest loan without using the normal EMI formula.

### 3. Credit Eligibility Assessor
Enter monthly income, current monthly debt, and the requested loan EMI. The app calculates the debt-to-income (DTI) percentage and returns a simple result:

| DTI | Result |
|---:|---|
| Up to 30% | Approved - Low risk |
| 30.01% to 40% | Approved - Moderate risk |
| 40.01% to 50% | Approved with caution - High risk |
| Above 50% | Not approved - Very high risk |

## Running the program

1. Make sure Python 3 is installed.
2. Open a terminal in this folder.
3. Run:

```bash
python financial_credit_assessment.py
```

Choose a menu number, enter the requested values, and choose `4` when you are finished.

## A quick example
