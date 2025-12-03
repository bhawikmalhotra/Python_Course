# 2. Even/Odd List Sorter
# This problem involves iterating over a list and making decisions.
# The Task: Given the list numbers = [1, 5, 22, 9, 14, 3, 4, 88, 7]. Create two new empty lists, evens and
# odds. Loop through the numbers list.
# If a number is even, add it to the evens list.
# If a number is odd, add it to the odds list.
# Finally, print both the evens and odds lists.


num = [1, 5, 22, 9, 14, 3, 4, 88, 7]

evens = []
odds = []
for i in num:
    if i % 2 == 0:
        evens.append(i)
    else:
        odds.append(i)

print(evens)
print(odds)