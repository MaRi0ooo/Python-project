import datetime
birth_day = int(input("Day of birth: "))
birth_month = int(input("Month of birth: "))
birth_year = int(input("Year of birth: "))
day = int(datetime.date.today().day)
month = int(datetime.date.today().month)
year = int(datetime.date.today().year)
# Step 3
if month > birth_month:
    age = year - birth_year
else:
    age = (year - birth_year) - 1
# Step 4
a = age
b = abs(month - birth_month)
c = abs(day - birth_day)
print(f"Your age: {a} years, {b} months, {c} days")
