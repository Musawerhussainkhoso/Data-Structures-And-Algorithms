#find the highest salary
salaries = [45000, 62000, 58000, 75000, 51000]

max_salary = salaries[0]
for salary in salaries:
    if salary > max_salary:
        max_salary = salary

print("Highest salary:", max_salary)
#time complexity 
print("Time Complexity : o(n)")
print("Space Complexity : o(1)")