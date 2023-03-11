"""
Ahmed Hashim
02-17-2023
ReverseVowels:
Given a string, reverse the order of the vowels in the string.

Time complexity: O(n), where n is the length of the input string.
We iterate over the string only once, and each character is processed in constant time.

Space complexity: O(n), where n is the length of the input string.
The space used by the new string variable we create is proportional to the length of the input string.

Technique: 
Two Pointer Techniques - Forward/backward two-pointer

Time Spent:
roughly 35 minutes

Approach:

1) Convert the input string to a list of characters to make it mutable.

2)Create a set of vowels for quick look-up.

3)Initialize two pointers, one pointing to the start of the string (left) and the other pointing to the end of the string (right).

4) While the left pointer is less than the right pointer:
Advance the left pointer until a vowel is found.
Advance the right pointer until a vowel is found.
Swap the vowels found by the left and right pointers.
Move the pointers inward.

5)Convert the list of characters back to a string and return it.

"""




def reverse_vowels(input_string):
    string_list = list(input_string)
    vowels = set('aeiouAEIOU')

    left, right = 0, len(string_list) - 1

    while left < right:
        while left < right and string_list[left] not in vowels:
            left += 1

        while left < right and string_list[right] not in vowels:
            right -= 1

        string_list[left], string_list[right] = string_list[right], string_list[left]

        left += 1
        right -= 1

    return ''.join(string_list)

'''
# I just did that to test teh function on the way that i'm alwats test it with even in the middle of the interview
    
    output = ''.join(string_list)
    print(output)
    return output
reverse_vowels("Uber Career Prep")
'''

# test cases
assert reverse_vowels("Uber Career Prep") == "eber Ceraer PrUp"
assert reverse_vowels("xyz") == "xyz"
assert reverse_vowels("flamingo") == "flominga"
assert reverse_vowels("gobbledygook") == "gobblodygeok"
assert reverse_vowels("hello world") == "hollo werld"

