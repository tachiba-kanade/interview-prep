from abc import ABC, abstractmethod

class Loan(ABC):
    @abstractmethod
    def calculate_interest_rate(self):
        pass
    def calculate_max_loan_amount(self):
        pass    

class HomeLoan(Loan):
    # Low Risk 6%
    # Medium Risk 8%
    # High Risk 11%
    # Very High Risk 14%

    def calculate_interest_rate(self, risk_category):
        rates = {
            "Low Risk": 6,
            "Medium Risk": 8,
            "High Risk": 11,
            "Very High Risk": 14
        }
        return rates.get(risk_category, 0)
         

    def calculate_max_loan_amount(self, annual_income, risk_category):
        multipliers = {
            "Low Risk": 0.6,
            "Medium Risk": 0.8,
            "High Risk": 1.1,
            "Very High Risk": 0.2
        }
        return annual_income * multipliers.get(risk_category, 0)    
    
    

class PersonalLoan(Loan):

    # Risk Level Interest Rate
    # Low Risk 8%
    # Medium Risk 11%
    # High Risk 15%
    # Very High Risk 20%
    def calculate_interest_rate(self, risk_category):
        rates = {
            "Low Risk": 8,
            "Medium Risk": 11,
            "High Risk": 15,
            "Very High Risk": 20
        }
        return rates.get(risk_category, 0)

    def calculate_max_loan_amount(self, annual_income, risk_category):
        multipliers = {
            "Low Risk": 0.8,
            "Medium Risk": 0.6,
            "High Risk": 0.4,
            "Very High Risk": 2.5
        }
        return annual_income * multipliers.get(risk_category, 0)
    

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.annual_income = 0

    def get_profile(self):
        return f"Name: {self.name}, Age: {self.age}, Annual Income: {self.annual_income}"

class Customer(Person):
    def __init__(self, name, age, credit_score):
        super().__init__(name, age)
        self.credit_score = 0.0
        self.monthly_expenses = 0.0
        self.existing_loans = 0.0
        self.payment_history_score = 90

    def calculate_credit_score(self):
        base_score = 300
        income_factor = (self.annual_income / 1000) * 5
        expense_penalty = (self.monthly_expenses / self.annual_income) * 200 if self.annual_income > 0 else 0
        debt_penalty = (self.existing_loans / self.annual_income) * 300 if self.annual_income > 0 else 0
        payment_bonus = self.payment_history_score * 3
        credit_score = base_score + income_factor + payment_bonus - expense_penalty - debt_penalty
        self.credit_score = max(300, min(850, credit_score))

        
    def get_risk_category(self):
       
        # Credit Score Range         Risk Level
        # 750 - 850                  Low Risk
        # 650 - 749                  Medium Risk
        # 550 - 649                  High Risk
        # Below 550                  Very High Risk

        if self.credit_score >= 750:
                return "Low Risk"
        elif self.credit_score >= 650 and self.credit_score < 750:
                return "Medium Risk"
        elif self.credit_score >= 550 and self.credit_score < 650:
                return "High Risk"
        else:
                return "Very High Risk"

    def get_profile(self):
        base_profile = super().get_profile()
        return f"{base_profile}, Credit Score: {self.credit_score}"
    
# Expected Output Example
# Customer: Rahul Sharma
# Credit Score: 732
# Risk Category: Medium Risk
# --- Personal Loan Offer ---
# Interest Rate: 11%
# Maximum Loan Amount: ₹480000
# --- Home Loan Offer ---
# Interest Rate: 8%
# Maximum Loan Amount: ₹720000

# Create customer
customer = Customer("Rahul Sharma", 35, 0)
customer.annual_income = 900000
customer.monthly_expenses = 20000
customer.existing_loans = 100000

# Calculate credit score
customer.calculate_credit_score()
risk = customer.get_risk_category()

# Create loans
personal_loan = PersonalLoan()
home_loan = HomeLoan()

# Print output
print(f"Customer: {customer.name}")
print(f"Credit Score: {int(customer.credit_score)}")
print(f"Risk Category: {risk}")

print("--- Personal Loan Offer ---")
print(f"Interest Rate: {personal_loan.calculate_interest_rate(risk)}%")
print(f"Maximum Loan Amount: ₹{int(personal_loan.calculate_max_loan_amount(customer.annual_income, risk))}")

print("--- Home Loan Offer ---")
print(f"Interest Rate: {home_loan.calculate_interest_rate(risk)}%")
print(f"Maximum Loan Amount: ₹{int(home_loan.calculate_max_loan_amount(customer.annual_income, risk))}")