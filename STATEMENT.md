# Financial Credit Assessment and Deposit Amortization System

---

# 1. Problem Statement

Modern banking involves several financial calculations such as fixed deposit returns, loan repayment planning, and assessment of a customer's ability to handle additional debt. Performing these calculations manually can be time-consuming and may lead to calculation errors. Therefore, there is a need for a simple and user-friendly software system that can automate these basic financial estimations.

The **Financial Credit Assessment and Deposit Amortization System** is a Python-based application designed to provide three important financial services: fixed deposit estimation, loan repayment scheduling, and credit eligibility assessment. The system accepts financial information from the user, performs the required calculations using predefined formulas and conditions, and displays the results in a clear and structured format.

The **Fixed Deposit Estimator** calculates the maturity value and interest earned on a deposit using both **simple interest and compound interest** methods. The applicable annual interest rate is selected according to the deposit amount, while compound interest is calculated using quarterly compounding.

The **Loan Repayment Scheduler** calculates the **monthly Equated Monthly Instalment (EMI)** based on the loan principal, annual interest rate, and tenure. It also generates a month-wise repayment schedule showing the EMI, interest component, principal component, and remaining loan balance.

The **Credit Eligibility Assessor** evaluates a user's ability to take an additional loan by calculating the **Debt-to-Income (DTI) ratio**. Based on predefined DTI limits, the system classifies the application as approved, approved with caution, or not approved, along with an associated risk level.

The project demonstrates the practical application of fundamental programming concepts such as **functions, conditional statements, loops, arithmetic operations, lists, dictionaries, formatted input/output, input validation, and modular program design**.

---

# 2. Scope of the Project

The scope of this project is to develop a basic financial estimation and credit assessment tool capable of performing common personal banking calculations. The system is primarily designed for **financial estimation and educational purposes**, with an emphasis on automating calculations that may otherwise be performed manually.

The major areas covered by the project include:

* **Fixed Deposit Estimation**

  * Accepts the deposit principal and investment duration from the user.
  * Automatically selects an interest-rate slab based on the deposit amount.
  * Calculates maturity values using both simple and compound interest.
  * Uses quarterly compounding for compound-interest calculations.
  * Displays year-wise maturity values.
  * Shows the difference between simple-interest and compound-interest returns.
  * Provides a final summary of maturity values and interest earned.

* **Loan Repayment Scheduling**

  * Accepts the loan amount, annual interest rate, and loan tenure.
  * Calculates the monthly EMI using the standard EMI formula.
  * Separates each EMI into interest and principal components.
  * Calculates the outstanding loan balance after each payment.
  * Generates a complete month-wise repayment schedule.
  * Calculates the total payment and total interest paid over the loan tenure.

* **Credit Eligibility Assessment**

  * Accepts monthly income, existing monthly debt obligations, and proposed loan EMI.
  * Calculates total monthly financial commitments.
  * Determines the Debt-to-Income (DTI) ratio.
  * Uses predefined DTI thresholds to classify the applicant.
  * Provides both an approval decision and a risk classification.

* **Input Validation and User Interaction**

  * Validates important numerical inputs before performing calculations.
  * Prevents invalid values such as negative debt, zero income, or non-positive loan tenure.
  * Provides an interactive menu for selecting different modules.
  * Allows users to perform multiple operations without restarting the program.
  * Provides an exit option to terminate the application.

The current scope is limited to **financial estimation and educational simulation**. The application does not connect to real bank accounts, credit bureaus, banking databases, or real-time interest-rate systems. The approval and risk classifications are based only on the predefined rules implemented in the program and should not be considered an actual banking or lending decision.

---

# 3. Target Users

The system is primarily intended for individuals who want to perform basic financial calculations and understand the effect of deposits, loans, and debt obligations on their finances. Since the application is simple and menu-driven, users do not require advanced technical knowledge to operate it.

The major target users include:

* **Banking Customers:**
  Individuals can use the system to estimate fixed deposit returns, understand loan repayment amounts, and evaluate their approximate borrowing capacity.

* **Loan Applicants:**
  Users planning to take a loan can calculate their expected EMI and understand how their existing debt and proposed EMI affect their DTI ratio.

* **Fixed Deposit Investors:**
  Customers can compare simple-interest and compound-interest returns and observe how their deposit value changes over multiple years.

* **Students and Learners:**
  The project can be used as an educational example to understand how programming concepts can be applied to real-world banking and financial problems.

* **Beginner Programmers:**
  The application demonstrates the practical implementation of Python concepts such as functions, loops, conditional statements, lists, dictionaries, calculations, and formatted output.

* **Financial Planning Beginners:**
  Users with limited financial knowledge can use the structured outputs to gain a basic understanding of interest, EMI, loan repayment, and Debt-to-Income ratios.

The system is particularly suitable for **personal financial estimation and learning purposes**, rather than professional banking operations or official credit approval.

---

# 4. High-Level Features

The system consists of three major financial modules along with a central menu-driven interface. Each module performs a specific financial task and presents the results in a structured and easy-to-understand format.

## 1. Fixed Deposit Estimator

The Fixed Deposit Estimator helps users understand the potential growth of their deposited amount over a selected period.

* Accepts deposit principal and duration in years.
* Automatically determines the applicable interest-rate slab.
* Supports three predefined deposit slabs:

  * Below ₹1,00,000 → 5.50%
  * ₹1,00,000 to ₹4,99,999.99 → 6.25%
  * ₹5,00,000 and above → 7.00%
* Calculates **simple-interest maturity**.
* Calculates **compound-interest maturity**.
* Uses quarterly compounding for compound-interest calculations.
* Displays year-wise maturity values.
* Calculates the difference between simple and compound returns.
* Displays final maturity amount and total interest earned.

## 2. Loan Repayment Scheduler

The Loan Repayment Scheduler provides a detailed breakdown of how a loan is repaid throughout its tenure.

* Accepts loan principal, annual interest rate, and tenure in months.
* Calculates the monthly EMI using the standard EMI formula.
* Calculates monthly interest based on the outstanding loan balance.
* Determines the principal amount paid from each EMI.
* Updates the outstanding balance after every payment.
* Generates a month-by-month repayment table.
* Displays:

  * Month number
  * EMI
  * Interest paid
  * Principal paid
  * Remaining balance
* Calculates the total amount paid over the loan period.
* Calculates the total interest paid.
* Adjusts the final payment when necessary to ensure that the remaining loan balance becomes zero.

## 3. Credit Eligibility Assessor

The Credit Eligibility Assessor provides a basic assessment of whether a user can handle an additional loan obligation.

* Accepts monthly income.
* Accepts existing monthly debt obligations.
* Accepts the EMI of the proposed loan.
* Calculates total monthly obligations.
* Calculates the Debt-to-Income (DTI) ratio.
* Classifies applications according to predefined DTI limits:

  * **Up to 30%:** Approved – Low Risk
  * **Above 30% to 40%:** Approved – Moderate Risk
  * **Above 40% to 50%:** Approved with Caution – High Risk
  * **Above 50%:** Not Approved – Very High Risk
* Displays the applicant's complete financial summary.
* Provides an educational estimate rather than an actual banking decision.

## 4. Menu-Driven and Modular Interface

The application provides a central menu that allows users to access different financial modules without restarting the program.

* Provides a simple numbered menu interface.
* Offers four options:

  * Fixed Deposit Estimator
  * Loan Repayment Scheduler
  * Credit Eligibility Assessor
  * Exit
* Uses separate functions for each major operation.
* Allows repeated calculations through a continuous loop.
* Handles invalid menu selections.
* Uses formatted tables and summaries for better readability.
* Performs basic input validation.
* Demonstrates modular, structured, and reusable Python programming practices.
