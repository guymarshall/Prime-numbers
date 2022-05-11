import sqlite3

conn = sqlite3.connect("prime_numbers.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS prime_numbers (
    input integer,
    prime integer
)""")

# c.execute("""INSERT INTO prime_numbers VALUES (
#     "Corey",
#     "Schafer",
#     50000
# )""")

# emp_1 = Employee("Steve", "Jobs", 100000)
# emp_2 = Employee("John", "Doe", 24000)

# c.execute("""INSERT INTO prime_numbers VALUES (
#     "Mary",
#     "Schafer",
#     70000
# )""")

# conn.commit()

# c.execute(f"""INSERT INTO prime_numbers VALUES (
#     ?,
#     ?,
#     ?
# )""", (emp_1.first, emp_1.last, emp_1.pay))

# conn.commit()

# c.execute(f"""INSERT INTO prime_numbers VALUES (
#     :first,
#     :last,
#     :pay
# )""", {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})

# conn.commit()

# c.execute("SELECT * FROM prime_numbers WHERE last='Schafer'")

# c.execute("SELECT * FROM prime_numbers WHERE last=':last'", {"last": "Doe"})

c.execute("SELECT * FROM prime_numbers")

print(c.fetchall())

conn.commit()

conn.close()