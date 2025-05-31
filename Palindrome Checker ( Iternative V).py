def is_palindrome_ilterbative(word):
    word = word.lower().replace(" ", "")
    return word == word[::-1]

# Example usage
user_input = input("Enter a word: ")
if is_palindrome_interative(user_input):
    print("\u2705 It's a palindrome!")
else:
    print("\u274C Not a palindrome.")
