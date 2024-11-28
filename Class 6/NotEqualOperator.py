x = 15
y = 18
z = 18

print(x != y)
print(y != z)

m = "python"
n = "programming"

if m != n:
    print(m, 'and', n, 'are different.')

p = 7
q = 9

if (p == 2) != (q == 9):
    print('Greetings')

number = int(input("Enter a number: "))

if number % 2 != 0:
    print(number, "is not an even number.")

if not (number % 2 == 0):
    print(number, "is an odd number.")
else:
    print(number, "is an even number.")
