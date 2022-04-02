hourly_fee = int(input("Enter the hourly fee in euros:"))
working_hours_per_week = int(input("Enter working hours per week:"))
salary_per_week = hourly_fee * working_hours_per_week

if working_hours_per_week >= 40:
    salary_payment = salary_per_week * 2
    print("Salary payment :", salary_payment)

else :
    salary_payment = salary_per_week
    print("Salary payment :", salary_payment)

