def loan_repayment_scheduler():
    print_separator()
    print("LOAN REPAYMENT SCHEDULER")
    loan_amount = float(input("Enter loan principal: "))
    interest_rate = float(input("Enter annual interest rate (%): "))
    num_months = int(input("Enter loan tenure in months: "))

    if loan_amount <= 0 or interest_rate < 0 or num_months <= 0:
        print("Enter a positive principal and tenure, and a non-negative rate.")
        print("Returning to the main menu.")
        return 0.0

    emi, m_rate = compute_monthly_emi(loan_amount, interest_rate, num_months)
    outstanding_bal = loan_amount
    payment_schedule = []

    for month_idx in range(1, num_months + 1):
        interest_component = round(outstanding_bal * m_rate, 2)
        principal_component = round(emi - interest_component, 2)
        actual_emi = emi

        if month_idx == num_months or principal_component >= outstanding_bal:
            principal_component = outstanding_bal
            actual_emi = round(interest_component + principal_component, 2)

        outstanding_bal = round(outstanding_bal - principal_component, 2)
        if outstanding_bal < 0:
            outstanding_bal = 0.0

        payment_schedule.append({
            "month": month_idx,
            "emi": actual_emi,
            "interest": interest_component,
            "principal": principal_component,
            "balance": outstanding_bal
        })

        if outstanding_bal == 0:
            break

    print_separator()
    print(f"{'Month':<7}{'EMI':>13}{'Interest':>15}{'Principal paid':>16}{'Balance':>18}")
    print_separator()
    
    for item in payment_schedule:
        print(f"{item['month']:<7}{item['emi']:>13.2f}{item['interest']:>15.2f}"
              f"{item['principal']:>16.2f}{item['balance']:>18.2f}")

    total_outflow = sum(item["emi"] for item in payment_schedule)
    total_interest_paid = sum(item["interest"] for item in payment_schedule)

    print_separator()
    print("Loan summary")
    print(f"Loan principal:     {loan_amount:.2f}")
    print(f"Annual rate:        {interest_rate:.2f}%")
    print(f"Tenure:             {num_months} month(s)")
    print(f"Monthly EMI:        {emi:.2f}")
    print(f"Total payment:      {total_outflow:.2f}")
    print(f"Total interest:     {total_interest_paid:.2f}")

    return emi
