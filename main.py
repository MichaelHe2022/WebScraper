"""
This program reads an online text file and uses string manipulation of patterns
to extract bank names and their corresponding APY values and stores them
in a dictionary.
"""

# Extracts and reads the file downloaded.
# The file starts out as a list of one element. List is converted into a string.

x = open("c:\\Users\\hemic\\Documents\\osa_info1-1.txt","r")
xx = x.readlines()
string = "".join(xx)

# Extracting the bank names requires finding patterns of repeated code before and after
# the bank name in the text file and printing the text that lies between these patterns.
# This for loop finds all the indexes where the pattern before the bank names occur
# and stores all of them into one list.

bank_beginning_indexes = []
for i in range(len(string)):
	if string[i:i+13] == "class=\"name\">":
		bank_beginning_indexes = bank_beginning_indexes + [i+13]
print(bank_beginning_indexes)



# This for loop finds all the indexes where the pattern after the bank name occurs
# and stores all of them into another list.

bank_ending_indexes = []
for i in range(len(string)):
	if string[i:i+10] == "</a><span>":
		bank_ending_indexes = bank_ending_indexes + [i]
print(bank_ending_indexes)

# Creates a new list of bank names.
# This for loop goes through the lists of beginning indexes and ending indexes
# from the other lists and prints everything every character that occurs between
# these indexes, thus producing the bank names. 

bank_names = []
for i in range(len(bank_beginning_indexes)):
	bank_names = bank_names + [string[bank_beginning_indexes[i]:bank_ending_indexes[i]]]
print(bank_names)


# This for loop finds all the indexes where the pattern before the APY values occur
# and stores all of them into one list.

apy_beginning_indexes = []
for i in range(len(string)):
	if string[i:i+18] == "class=\"apy\"><span>":
		apy_beginning_indexes = apy_beginning_indexes + [i+18]
print(apy_beginning_indexes)


# Creates a new list of APY.
# This for loop goes through the list of beginning APY indexes and prints the next 5
# characters after these indexes. Since all APY values are rounded to the nearest tenth
# and therefore are all 5 characters, finding the indexes of patterns that occur after
# the APY value is not necessary.
apy_values = []
for i in range(len(apy_beginning_indexes)):
	apy_values = apy_values + [string[apy_beginning_indexes[i]:apy_beginning_indexes[i] + 5]]

# Creates a dictionary of key-value pairs between bank names and their corresponding APY values.

bank_dictionary = {}
for i in range(len(bank_names)):
	bank_dictionary[bank_names[i]] = apy_values[i]