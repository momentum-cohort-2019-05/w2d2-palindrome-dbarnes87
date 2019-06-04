persons_phrase = input("Please enter a phrase, a sentence, or multiple sentences.")
all_letters = "abcdefghijklmnopqrstuvwxyz"
found_letters = []
for letter in persons_phrase.lower():
    if letter in all_letters:
        found_letters.append(letter)
# lower_case = persons_phrase.lower()
# remove_space = str(lower_case.replace(" ", ""))
# remove_punctuation = remove_space.translate(None, remove_space.punctuation)

reversed_phrase = found_letters[::-1]

if reversed_phrase == found_letters:
    print("Congrats - this is a palindrome.")
else:
    print("Sorry - this is not a palindrome.")

# print(remove_space)
# print(reversed_phrase)