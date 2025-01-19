from collections import deque

def is_palindrome(s):
    s = ''.join(char.lower() for char in s if char.isalnum())
    d = deque(s)

    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True

if __name__ == "__main__":
    print("Palindrome Checker")
    user_input = input("Enter a string to check if it's a palindrome: ")
    result = "is a palindrome" if is_palindrome(user_input) else "is not a palindrome"
    print(f"The string '{user_input}' {result}.")
