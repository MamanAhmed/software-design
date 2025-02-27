# Example 1 - Common Design Mistakes

# Program Goal, print a list of words delimited by commas

# Solution 1 - What's wrong?
list_of_words = ["hello", "yes", "goodbye", "last"]
print(list_of_words[0] + "," + list_of_words[1] +
      "," + list_of_words[2] + "," + list_of_words[3])

# Code is not flexible to change


# Solution 2
list_of_words = ["hello", "yes", "goodbye", "last"]
to_print = ""

for i in range(4):
    to_print += list_of_words[i]
    if i != 3:
        to_print += ","

print(to_print)


# Still not flexible enough, hardcoded number of elements


# Solution 3
list_of_words = ["hello", "yes", "goodbye", "last"]
print(",".join(list_of_words))

# Acceptable but can be improved


# Solution 4
DELIMETER = ","
list_of_words = ["hello", "yes", "goodbye", "last"]
print(DELIMETER.join(list_of_words))
