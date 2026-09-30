def run_app():
    while True:
        print_separator()
        print("FINANCIAL CREDIT ASSESSMENT AND DEPOSIT AMORTIZATION SYSTEM")
        print("1. Fixed Deposit Estimator")
        print("2. Loan Repayment Scheduler")
        print("3. Credit Eligibility Assessor")
        print("4. Exit")
        print_separator()
        
        user_selection = input("Enter your choice (1-4): ").strip()

        if user_selection == "1":
            fixed_deposit_estimator()
        elif user_selection == "2":
            loan_repayment_scheduler()
        elif user_selection == "3":
            credit_eligibility_assessor()
        elif user_selection == "4":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid menu choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    run_app()

