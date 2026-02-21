# Age calculator program
# get employee name and year of birth
Employee_name= input("Enter your name: ")
Employee_year= 2002

# calculate age
current_year= 2026
current_age= current_year - Employee_year
age_months= current_age * 12
age_days= current_age * 365
age_hours= age_days * 24
age_minutes= age_hours * 60
age_seconds= age_minutes * 60
years_to_60= 60 - current_age

# display the results
print(f"Employee Name: {Employee_name}")
print(f"Age in Years: {current_age}")
print(f"Age in Months: {age_months}")
print(f"Age in Days: {age_days}")
print(f"Age in Hours: {age_hours}")
print(f"Age in Minutes: {age_minutes}")
print(f"Age in Seconds: {age_seconds}")
print(f"Years until 60: {years_to_60}")