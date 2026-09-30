def credit_eligibility_assessor():
    print_separator()
    print("CREDIT ELIGIBILITY ASSESSOR")
    monthly_income = float(input("Enter monthly income: "))
    current_debts = float(input("Enter combined existing monthly debt: "))
    new_emi = float(input("Enter requested loan EMI: "))

    if monthly_income <= 0 or current_debts < 0 or new_emi <= 0:
        print("Income and requested EMI must be positive; debt cannot be negative.")
        print("Returning to the main menu.")
        return

    total_commitments = current_debts + new_emi
    dti_ratio = total_commitments * 100 / monthly_income

    if dti_ratio <= 30:
        status, risk_level = "Approved", "Low risk"
    elif dti_ratio <= 40:
        status, risk_level = "Approved", "Moderate risk"
    elif dti_ratio <= 50:
        status, risk_level = "Approved with caution", "High risk"
    else:
        status, risk_level = "Not approved", "Very high risk"

    assessment_summary = {
        "monthly_income": monthly_income,
        "existing_debt": current_debts,
        "requested_emi": new_emi,
        "total_obligations": total_commitments,
        "dti": dti_ratio,
        "approval": status,
        "risk": risk_level
    }

    print_separator()
    print(f"Monthly income:            {assessment_summary['monthly_income']:.2f}")
    print(f"Existing monthly debt:     {assessment_summary['existing_debt']:.2f}")
    print(f"Requested loan EMI:        {assessment_summary['requested_emi']:.2f}")
    print(f"Total monthly obligations: {assessment_summary['total_obligations']:.2f}")
    print(f"Debt-to-income ratio:      {assessment_summary['dti']:.2f}%")
    print(f"Decision:                  {assessment_summary['approval']}")
    print(f"Risk classification:       {assessment_summary['risk']}")
    print_separator()
    print("This is an educational estimate, not an actual banking decision.")
