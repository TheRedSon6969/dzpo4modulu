def is_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False

# использование
print(is_palindrome('лепсспел')) # True
print(is_palindrome('helloworld')) # False

print("omega")