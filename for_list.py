spam = list(range(0, 100, 2))
print(spam)

supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
for i in range(len(supplies)):
    print('Index ' + str(i) + ' in supplies is: ' + supplies[i])

cat = ['fat', 'orange', 'loud']
size = cat[0]
color = cat[1]
disposition = cat[2]
print(size, color, disposition)


# Multiple Assignment Trick
cat = ['fat', 'orange', 'loud']
size, color, disposition = cat
print(size, color, disposition)

# Swapping Variables
a = 'AAA'
b = 'BBB'
a, b = b, a
print(a, b)

# Augmented Assignment Operators
spam = 42
spam += 1
print(spam)
