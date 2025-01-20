expenses = [
    2200, # Jan
    2350, # Feb
    2600, # Mar
    2130, # Apr
    2190, # May
]

# In deb how many dollars you spent extra, compared to feb?
answer1 = expenses[1] - expenses[0]
print(answer1)

# Find out total expense in first 3months of the year
answer2 = 0
months_in_quarter = 3
for i in range(3):
    answer2 += expenses[months_in_quarter]
print(answer2)

# Find out if you spent exactly $2000 in any month
if 2000 in expenses:
    print(True)
else:
    print(False)

# Add expense for Jun as $1980
expenses.append(1980)
print("June expense ->",expenses[5])

# Add refund amount of $200 in the month of April
old_april_expense = expenses[3]
updated_april_expense = old_april_expense + 200
expenses[3] = updated_april_expense
print("Updated April's expense ->", expenses[3])