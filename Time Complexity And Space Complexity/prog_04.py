def calculate_total_sales(sales):
    total = 0

    for amount in sales:
        total += amount

    return total


daily_sales = [1200, 1500, 900, 2000, 1750]

print("Total Sales:", calculate_total_sales(daily_sales))
#time complexity 
print("Time Complexity : o(n)")
print("Space Complexity : o(1)")

def find_duplicates(numbers):
    duplicates = []

    for first_index in range(len(numbers)):
        for second_index in range(first_index + 1, len(numbers)):
            if numbers[first_index] == numbers[second_index]:
                if numbers[first_index] not in duplicates:
                    duplicates.append(numbers[first_index])

    return duplicates


values = [10, 20, 30, 20, 40, 10, 50]

print("Duplicate Values:", find_duplicates(values))
#time complexity
print("Time Complexity : o(n^2)")
print("Space Complexity : o(n)")