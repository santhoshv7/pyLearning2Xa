def rev_str(str):
    rev_str = ""

    for c in str:
        rev_str = c + rev_str


a = input ("Enter the word to find palindrome")
b = rev_str(a)

if a == b:
    print("The given word is a palindrome")
else:
    print("The given word is not a palindrome")
