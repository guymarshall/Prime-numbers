import math
import sqlite3

def is_prime_number(number):
    for i in range(2, math.ceil(math.sqrt(number)) + 1):
        if number % i == 0:
            return False
    return True

def main():
    user_input = int(input("Enter a positive integer: "))
    print("Prime numbers:")

    # for i in range(user_input + 1):
    #     if is_prime(i):
    #         print(i)

    conn = sqlite3.connect("prime_numbers.db")

    c = conn.cursor()

    c.execute("""CREATE TABLE IF NOT EXISTS prime_numbers (
        input integer,
        prime integer
    )""")

    prime_number_count = 0
    number = 2
    while prime_number_count < user_input:
        is_prime = is_prime_number(number)
        if is_prime:
            prime_number_count += 1
            # print(f"{prime_number_count}: {number}")
            c.execute("""INSERT INTO prime_numbers VALUES (
                :input,
                :prime
            )""", {"input": prime_number_count, "prime": number})
        number += 1

    conn.commit()

    # c.execute("SELECT * FROM prime_numbers")

    # print(c.fetchall())

    # conn.commit()

    conn.close()

if __name__ == "__main__":
    main()