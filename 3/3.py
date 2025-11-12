# 3. Vowel Counter
# This task focuses on string iteration and using membership operators.
# The Task: Write a program that asks the user to input a sentence. Then, loop through every character in
# the string.
# Count how many vowels (a, e, i, o, u) are in the string.
# Count how many consonants are in the string.
# Ignore spaces and punctuation.
# Print the final vowel and consonant counts. (Hint: a vowels string like "aeiouAEIOU" might be helpful).

word = input("Enter a sentence: ")
vowels = "aeiouAEIOU"

v_words = []
c_words = []

for i in word:
    if i in vowels:
        v_words.append(i)
    else:
        c_words.append(i)

print(f"Vowels : {len(v_words)}")
print(f"Consonents : {len(c_words)} ")


