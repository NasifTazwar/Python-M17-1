# Take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
biology = int(input("biology: "))
history = int(input("history: "))
geography = int(input("geography: "))
art = int(input("art: "))

# Let's calculate the percentage of marks
total_marks = biology + history + geography + art
print("Sum of biology, history, geography, and art: ", total_marks)

percentage = (total_marks / 400) * 100
print("Percentage Mark = ", percentage)

# Find the highest and lowest marks
highest_marks = max(biology, history, geography, art)
lowest_marks = min(biology, history, geography, art)

print("Highest Marks = ", highest_marks)
print("Lowest Marks = ", lowest_marks)
