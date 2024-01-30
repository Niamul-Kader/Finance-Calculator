import math
def calculate_investment():
    principal = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    years = int(input("Enter the number of years you plan on investing: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    if interest_type == 'simple':
        interest = principal * (1 + (interest_rate / 100) * years)
    elif interest_type == 'compound':
        interest = principal * math.pow(1 + interest_rate / 100, years)
    else:
        print("Invalid input for interest type. Please enter 'simple' or 'compound'.")
        return

    print(f"\nThe amount you will get back after {years} years at {interest_rate}% {interest_type} interest is: {interest:.2f}")


def calculate_bond():
    
    p = float(input("Enter the present value of the house: "))
    interest_rate = float(input("Enter the interest rate (as a percentage): "))
    n = int(input("Enter the number of months to repay the bond: "))
    i = (interest_rate / 100) / 12
    repayment = (i * p)/ (1 - (1 + i)**(-n))

    print(f"\nThe monthly bond repayment will be: {repayment:.2f}")


print("Menu:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you'll have to pay on a home loan")

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

if user_choice == 'investment':
    calculate_investment()
elif user_choice == 'bond':
    calculate_bond()
else:
    print("Invalid input. Please enter 'investment' or 'bond'.")
