import calendar

# Function to print all months of the year
def print_year_calendar(year):
    for month in range(1, 13):  # Loop through all months from 1 to 12
        print(calendar.month(year, month))  # Print the calendar for each month

# Input the year from the user
year = int(input("Enter the year: "))

# Print the calendar for each month of the given year
print_year_calendar(year)
