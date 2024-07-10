def karatsuba(x, y):
    # Base case for the recursion (single-digit multiplication)
    if x < 10 or y < 10:
        return x * y
    
    # Calculates the size of the numbers
    n = max(len(str(x)), len(str(y)))
    m = n // 2   # // integer division

    # Splits x and y
    high1, low1 = divmod(x, 10**m)
    high2, low2 = divmod(y, 10**m)

    # Step 1: Compute the products of the lower halves
    z0 = karatsuba(low1, low2)
    print(f"Step 1: {low1} * {low2} = {z0}")

    # Step 2: Compute the products of the higher values
    z2 = karatsuba(high1, high2)
    print(f"Step 2: {high1} * {high2} = {z2}")

    # Step 3: Compute the products of the sums of the halves and deduct z0 and z2
    z1 = karatsuba((low1 + high1),(low2 + high2))  - z2 - z0
    print(f"Step 3: ({low1} + {high1}) * ({low2} + {high2}) - {z2} - {z0} = {z1}")

    # Combine the results
    result = (z2 * 10**(2 * m)) + (z1 * 10**m) + z0
    print(f"Combine: ({z2} * 10**(2 * {m})) + ({z1} * 10**({m})) + {z0} = {result}")

    return result

# Example usage
x = 3141592653589793238462643383279502884197169399375105820974944592
y = 2718281828459045235360287471352662497757247093699959574966967627
print(f"Multiplication of {x} and {y} using Karatsuba Algorithm:")
karatsuba(x, y)