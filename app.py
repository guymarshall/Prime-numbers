import math

def is_prime(number):
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    user_input = int(input("Enter a positive integer: "))
    print("Prime numbers:")

    for i in range(user_input + 1):
        if is_prime(i):
            print(i)

if __name__ == "__main__":
    main()

# int primeNumberCount = 0;
# int number = 2;
# while (primeNumberCount < userInput) {
#     boolean isPrime = isPrimeNumber(number);
#     if (isPrime) {
#         primeNumberCount++;
#         System.out.printf("%d: %d%n", primeNumberCount, number);
#     }
#     number++;
# }