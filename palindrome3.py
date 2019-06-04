persons_phrase = input("Please enter a phrase, a sentence, or multiple sentences.")
all_letters = "abcdefghijklmnopqrstuvwxyz"
found_letters = []
for letter in persons_phrase.lower():
    if letter in all_letters:
        found_letters.append(letter)
# print (found_letters)

# if found_letters[0] != found_letters[-1]:
#     print("This is not a palindrome")
# elif found_letters[1] != found_letters[-2]:
#     print("This is not a palindrome")
# elif found_letters[2] != found_letters[-3]:
#     print("This is not a palindrome")
# elif found_letters[3] != found_letters[-4]:
#         print("This is not a palindrome")
# else:
#      print("This is a palindrome")

def palindrome_det(x):
    if len(x) == 0 or len(x) == 1:
        return True
    elif x(0) == x[-1]:
        x = x[1:-1]
        palindrome_det(x)
    else:
        return False

if True:
    print("Congrats - this is a palindrome.")
else:
    print("Sorry - this is not a palindrome.")



