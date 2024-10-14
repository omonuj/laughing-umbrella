def is_palindrome(string):

	left = 0
	right = len(string) - 1
	
	while left < right:
		if string[left] != string[right]:
			return False
		left += 1
		right -= 1
		
	return True

test_string1 = "madam"
test_string2 = "hello"
test_string3 = "racecar"

print(f'Is "{test_string1}" a palindrome? {is_palindrome(test_string1)}')
print(f'Is "{test_string2}" a palindrome? {is_palindrome(test_string2)}')
print(f'Is "{test_string3}" a palindrome? {is_palindrome(test_string3)}')
