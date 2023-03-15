"""
Ahmed Hashim
03-12-2023
KAnagrams:
Two strings are considered to be “k-anagrams” if they can be made into anagrams by changing at most k characters in one of the strings. Given two strings and an integer k, determine if they are k-anagrams.

Time complexity: O(n)

The space complexity: O(n)




Technique: Hashing technique 

Time Spent:
roughly 50 minutes

Approach:


1) Check if the lengths of the two input strings, s1 and s2, are equal. If not, return False as they can't be k-anagrams.

2) Create two dictionaries to store the frequency of each character in s1 and s2.

3)Traverse s1 and s2 and update their respective frequency dictionaries.

4) Traverse one of the frequency dictionaries, and for each character in the dictionary:

a. If the character is not in the other frequency dictionary, add its frequency to a counter 'count'.

b. If the character is in both frequency dictionaries, calculate the absolute difference between their frequencies, and add it to 'count'.

c. If 'count' exceeds k, return False, as the strings are not k-anagrams.

5) If the function has not returned False at this point, it means the two strings are k-anagrams of each other, and we can return True.
"""
def k_anagrams(s1, s2, k):
    if len(s1) != len(s2):
        return False
    
    freq1, freq2 = {}, {}
    count = 0
    for letter in s1:
        freq1[letter] = freq1.get(letter, 0) + 1
    for letter in s2:
        freq2[letter] = freq2.get(letter, 0) + 1
    
    for letter in freq1:
        if letter not in freq2:
            count += freq1[letter]
        else:
            count += abs(freq1[letter] - freq2[letter])
        
        if count > k:
            return False
    
    return True

#Test Cases
assert k_anagrams("apple", "peach", 1) == False
assert k_anagrams("apple", "peach", 2) == True
assert k_anagrams("cat", "dog", 3) == True
assert k_anagrams("debit curd", "bad credit", 1) == True
assert k_anagrams("baseball", "basketball", 2) == False


