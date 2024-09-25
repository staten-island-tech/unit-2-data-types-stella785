def find_factors(n):
    if n <= 0:
        return "Enter a positive whole number"

    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

number = int(input("Enter a number: "))
result = find_factors(number)

print(result)