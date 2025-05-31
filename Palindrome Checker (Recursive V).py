def is_palindrome_recursive(word):
    word = word.lower().replace(" ", "")
    if len(word) <= 1:
        return True
    if word[0] != word[-1]:
        return False
    return is_palindrome_recursive(word[1:-1])

user_input = input("Enter a word: ")
if is_palindrome_recursive(user_input):
    print("\u2705 It's a palindrome!")
else:
    print("\u274C Not a palindrome.")
