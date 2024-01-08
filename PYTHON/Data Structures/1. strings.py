# https://www.w3schools.com/python/python_ref_string.asp

# O(N)
# format() - Formats specified values in a string
name = "World"
print(f"Hello, {name}!") # N
print("Hello, {}".format(name))

# O(min(M, K)) ~ O(N)
# startswith()	Returns true if the string starts with the specified value
# endswith() - Returns true if the string ends with the specified value
test = "abcdef" # M - len of test
print(test.startswith("abc")) # K - len of substring

# O(M * K) ~ O(N^2)
# find() - Searches the string for a specified value and returns the position of where it was found (returns -1 if the value is not found)
# index() - Searches the string for a specified value and returns the position of where it was found (raises an exception if the value is not found)
test = "abcdabcd" # M - len of test
print(test.find("bc")) # K - len of substring

# rfind() - Searches the string for a specified value and returns the last position of where it was found (returns -1 if the value is not found)
# rindex() - Searches the string for a specified value and returns the last position of where it was found (raises an exception if the value is not found)

# O(M * K) ~ O(N^2)
# count() - Returns the number of times a specified value occurs in a string
test = "abcdabcd" # M - len of test
print(test.count("bc")) # K - len of substring

# O(M * K) ~ O(N^2)
# replace() - Returns a string where a specified value is replaced with a specified value
test = "abcdabcd" # M - len of test
print(test.replace("cb", "TTT")) # K - len of replacement, L - len of substring

# O(M * K) ~ O(N^2)
# split() - Splits the string at the specified separator, and returns a list
# splitlines() - Splits the string at line breaks and returns a list
test = "abcdabcd" # M - len of test
print(test.split("bc")) # K - len of substring

# O(N)
# join() - Converts the elements of an iterable into a string
print("++".join(["11", "22", "33"])) # N - len of iterable

# O(N)
# isalpha() - Returns True if all characters in the string are in the alphabet
# isdigit() - Returns True if all characters in the string are digits
# isdecimal() - Returns True if all characters in the string are decimals
# islower() - Returns True if all characters in the string are lower case
# isupper() - Returns True if all characters in the string are upper case
print("abcdabcd".islower()) # N - len of string

# O(N)
# lower() - Converts a string into lower case
# upper() - Converts a string into upper case
# capitalize() - Converts the first character to upper case
# title() - Converts the first character of each word to upper case
print("abcdabcd".upper()) # N - len of string
