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
