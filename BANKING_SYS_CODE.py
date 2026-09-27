def print_separator():
    print("-" * 78)


def determine_deposit_slab(amount):
    if amount < 100000:
        return 5.50, "Below 100000"
    if amount < 500000:
        return 6.25, "100000 to 499999.99"
    return 7.00, "500000 and above"


def fixed_deposit_estimator():
    print_separator()
    print("FIXED DEPOSIT ESTIMATOR")
    print("Illustrative annual-rate slabs: below 100000 = 5.50%, "
          "100000-499999.99 = 6.25%, 500000 and above = 7.00%")

    principal = float(input("Enter deposit principal: "))
    duration_yrs = int(input("Enter deposit term in whole years: "))

    if principal <= 0 or duration_yrs <= 0:
        print("Principal and term must be positive. Returning to the main menu.")
        return 0.0, 0.0

    annual_rate, slab_name = determine_deposit_slab(principal)
    compound_freq = 4
    
    print(f"Selected rate band: {slab_name}")
    print(f"Annual interest rate: {annual_rate:.2f}%")
    print("Compounding frequency: quarterly")
    
    print_separator()
    print(f"{'Year':<8}{'Simple maturity':>20}{'Compound maturity':>22}{'Difference':>20}")
    print_separator()

    final_simple_val = 0.0
    final_compound_val = 0.0

    for yr in range(1, duration_yrs + 1):
        simple_yield = principal + (principal * annual_rate * yr / 100)
        compound_yield = principal * (1 + annual_rate / (100 * compound_freq)) ** (compound_freq * yr)
        delta = compound_yield - simple_yield

        print(f"{yr:<8}{simple_yield:>20.2f}{compound_yield:>22.2f}{delta:>20.2f}")
        final_simple_val = simple_yield
        final_compound_val = compound_yield

    simple_interest = final_simple_val - principal
    compound_interest = final_compound_val - principal
    
    print_separator()
    print("Final term summary")
    print(f"Simple-interest maturity:   {final_simple_val:.2f}")
    print(f"Simple interest earned:     {simple_interest:.2f}")
    print(f"Compound-interest maturity: {final_compound_val:.2f}")
    print(f"Compound interest earned:   {compound_interest:.2f}")
    print(f"Maturity difference:        {final_compound_val - final_simple_val:.2f}")

    return final_simple_val, final_compound_val


def compute_monthly_emi(principal, annual_rate, tenure_months):
    monthly_rate = annual_rate / (12 * 100)
    if monthly_rate == 0:
        emi_val = principal / tenure_months

    else:
        emi_val = (principal * monthly_rate * (1 + monthly_rate) ** tenure_months) / ((1 + monthly_rate) ** tenure_months - 1)
    return round(emi_val, 2), monthly_rate


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


def credit_eligibility_assessor():
    

