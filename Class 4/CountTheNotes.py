# Taking total amount as input from user
total_amount = int(input("Please Enter Amount for Withdrawal: "))

# Calculating the number of notes of different denominations
hundred_notes = total_amount // 100
fifty_notes = (total_amount % 100) // 50
ten_notes = ((total_amount % 100) % 50) // 10

print("Notes of 100 currency:", hundred_notes)
print("Notes of 50 currency:", fifty_notes)
print("Notes of 10 currency:", ten_notes)
