# Get input values
car_price = float(input("Enter car price: "))
down_payment = float(input("Enter down payment: "))  
interest_rate = float(input("Enter annual interest rate (e.g. 0.05 for 5%): "))

# Calculate loan amount  
loan_amount = car_price - down_payment

# Calculate monthly interest rate from annual interest rate 
monthly_interest_rate = interest_rate / 12  

# Calculate number of months for the loan
num_months = 5 * 12   

# Calculate monthly payment
monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate)**(-num_months))

print(f"Monthly Payment: {round(monthly_payment, 2)}")
