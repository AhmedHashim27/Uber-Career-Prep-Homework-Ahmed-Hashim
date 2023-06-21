'''
Algorithm:

Split the input string into a list of words using the space as the delimiter.
Push each word onto a stack.
Pop words from the stack and concatenate them into a new string, separated by spaces.
Return the reversed string.
Time complexity: O(n), where n is the length of the input string.
Space complexity: O(n), where n is the length of the input string (to store the words in the stack).
Time 15 min
'''
def reverse_word_order(string):
    words = string.split()
    stack = []
    for word in words:
        stack.append(word)
    reversed_string = ""
    while stack:
        reversed_string += stack.pop()
        if stack:
            reversed_string += " "
    return reversed_string

# Test cases
print(reverse_word_order("Uber Career Prep"))  # Output: "Prep Career Uber"
print(reverse_word_order("Emma lives in Brooklyn, New York."))  # Output: "York. New Brooklyn, in lives Emma"
