months = ('jan', 'feb', 'march', 'april', 'may', 'june', 'july', 'aug', 'sep', 'oct', 'nov', 'dec')

sales = (20000,45000,78000,97000,12000,45000,65000,54000,10000,30000,70000,90000)

print(max(sales))
index = sales.index(max(sales))
print(months[index])

print(min(sales))
index = sales.index(min(sales))
print(months[index])