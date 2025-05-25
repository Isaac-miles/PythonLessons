# Example: Using AI to generate a Fibonacci function

def fibonacci(n):
    """
    Generate Fibonacci sequence up to n terms.
    Returns a list containing the sequence.
    """
    fib_sequence = [0, 1]

    if n <= 0:
        return []
    elif n == 1:
        return [0]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence