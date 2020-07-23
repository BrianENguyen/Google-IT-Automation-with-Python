'''
1.

Fill in the blanks of this code to print out the numbers 1 through 7.
'''

number = 1
while number <= 7:
    print(number, end=" ")
    number +=1

'''
2.

The show_letters function should print out each letter of
a word on a separate line.
Fill in the blanks to make that happen.
'''
def show_letters(word):
    for letter in word:
	print(letter)

show_letters("Hello")
# Should print one line per letter


'''
3.

Complete the function digits(n) that returns how many digits the number has.
For example: 25 has 2 digits and 144 has 3 digits. Tip: you can figure out the
digits of a number by dividing it by
10 once per digit until there are no digits left.
'''
def digits(n):
	count = 0
	if n == 0:
	  return 1
	while (count < len(str(n))):
		count += 1
	return count
	
print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1


'''
4.

This function prints out a multiplication table
(where each number is the result of multiplying the first
number of its row by the number at the top of its column).
Fill in the blanks so that calling multiplication_table(1, 3)
will print out:
'''

def multiplication_table(start, stop):
	for x in range(start, stop + 1):
		for y in range(start, stop+ 1):
			print(str(x*y), end=" ")
		print()

multiplication_table(1, 3)
# Should print the multiplication table shown above
