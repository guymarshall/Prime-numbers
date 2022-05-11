import sqlite3

conn = sqlite3.connect("prime_numbers.db")

c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS prime_numbers (
    input integer,
    prime integer
)""")

# c.execute(f"""INSERT INTO prime_numbers VALUES (
#     :first,
#     :last,
#     :pay
# )""", {"first": emp_2.first, "last": emp_2.last, "pay": emp_2.pay})

# conn.commit()

c.execute("SELECT * FROM prime_numbers")

print(c.fetchall())

conn.commit()

conn.close()