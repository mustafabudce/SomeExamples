from datetime import date
vehicle_inspection_date = date(year=2021, month=4, day=5)
current_date = date(year=2022, month=4, day=7)

difference = current_date - vehicle_inspection_date
day = difference.days
year = 365
maintenance_date = year - day
if maintenance_date < 0:
    maintenance_date = maintenance_date * -1
    print(f"The maintenance date has passed {maintenance_date} days!")

else:
    print(f"Remaining time is {maintenance_date} day ")

