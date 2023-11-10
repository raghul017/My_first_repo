def generate_fibonacci(limit):
    fibonacci_sequence = [0, 1]

    while True:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        if next_fibonacci > limit:
            break
        fibonacci_sequence.append(next_fibonacci)

    return fibonacci_sequence

def main():
    limit = 1000
    fibonacci_numbers = generate_fibonacci(limit)

    print(f"Fibonacci numbers up to {limit}:")
    for num in fibonacci_numbers:
        print(num, end=" ")

if __name__ == "__main__":
    main()
