def is_palindrome(word):

    reversed_str=word[::-1]

    return word==reversed_str

print(is_palindrome ("madam"))