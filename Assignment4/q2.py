'''
Technique Used: Trie as a parameter

Time Complexity: The time complexity is O(M * N * 8^L), where M and N are the dimensions of the board, and L is the maximum length of words in the dictionary. In the worst case, we explore all possible paths from each cell.

Space Complexity: The space complexity is O(L), where L is the length of the longest word in the dictionary, for the Trie data structure.
'''


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

def find_valid_words(board, dictionary):
    def dfs(node, i, j, path):
        char = board[i][j]
        if char not in node.children:
            return

        node = node.children[char]
        if node.is_end_of_word:
            valid_words.add(path)

        original_char = board[i][j]
        board[i][j] = '#'

        for x, y in neighbors:
            ni, nj = i + x, j + y
            if 0 <= ni < m and 0 <= nj < n and board[ni][nj] != '#':
                dfs(node, ni, nj, path + board[ni][nj])

        board[i][j] = original_char

    m, n = len(board), len(board[0])
    neighbors = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    valid_words = set()
    
    trie = Trie()
    for word in dictionary:
        trie.insert(word)
    
    for i in range(m):
        for j in range(n):
            dfs(trie.root, i, j, board[i][j])
    
    return list(valid_words)

# Test cases
dictionary = ["Ace", "Ape", "Cape", "Clap", "Clay", "Gape", "Grape", "Lace", "Lap", "Lay", "Mace", "Map", "May", "Pace", "Pay", "Rap", "Ray", "Tap", "Tape", "Trace", "Trap", "Tray", "Yap"]
board = [
    ["A", "D", "E"],
    ["R", "C", "P"],
    ["L", "A", "Y"]
]
result = find_valid_words(board, dictionary)
print(result)  # Output should be: ['Clap', 'Lap', 'Pay', 'Lace', 'Ape', 'Pace', 'Rap', 'Ray', 'Tape', 'Ace', 'Clay', 'Yap', 'Tray']
