text = input("Enter a string: ")
# Optional: Remove spaces and make lowercase for general palindrome check
text_clean = text.replace(" ", "").lower()
if text_clean == text_clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
