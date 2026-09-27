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
