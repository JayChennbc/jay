# File: average_vowels.py

# You’re curious about the average number of vowels compared to consonants in a paragraph.

# --- 1. Counting Vowels ---
# Write a return function that takes a string as input.
# The function should return a tuple containing:
#     (number of vowels, number of consonants)
# Name this function: counting_vowels_and_consonants()

# Hint: You can use .isalpha() to check if a character is a letter.
def counting_vowels_and_consonants(text):
    vowels = "aeiouAEIOU"
    number_vowels = 0
    number_consonants = 0
    for character in text:
        if character.isalpha():
            if character in vowels:
                number_vowels += 1
            else:                      #not a vowel --> is consonant
                number_consonants += 1
    return (number_vowels, number_consonants)
# #test
# print(counting_vowels_and_consonants(text = "Hello World!"))  #(3, 7)

# --- 2. Average Vowels ---
# Write a return function that takes in a paragraph (string) as input.
# The function should:
#   - Split the paragraph into individual sentences.
#   - Use counting_vowels_and_consonants() to count values for each sentence.
#   - Return a tuple: (number of sentences, average vowels per sentence, average consonants per sentence)
# Name this function: average_vowels_and_consonants()

# Here is your paragraph to analyze. It is a quote from Richard Feynman. 
paragraph = (
    "Fall in love with some activity, and do it! "
    "Nobody ever figures out what life is all about, and it doesn't matter. "
    "Explore the world. "
    "Nearly everything is really interesting if you go into it deeply enough. "
    "Work as hard and as much as you want to on the things you like to do the best. "
    "Don't think about what you want to be, but what you want to do. "
    "Keep up some kind of a minimum with other things so that society doesn't stop you from doing anything at all."
)
def average_vowels_and_consonants(paragraph):
    sentences = paragraph.split('. ') #split at punctuation followed by space
    total_vowels = 0
    total_consonants = 0
    number_sentences = len(sentences) + 1   #last sentence does not have space after punctuation
    
    for sentence in sentences:
        vowels, consonants = counting_vowels_and_consonants(sentence)
        total_vowels += vowels
        total_consonants += consonants
    
    average_vowels = total_vowels / number_sentences
    average_consonants = total_consonants / number_sentences
    return (number_sentences, average_vowels, average_consonants)
# #test
# print(average_vowels_and_consonants(paragraph))    #(7, 19.57, 31.3)
# Write descriptive print statements, with f-strings, that output the average vowels and consonants per sentence of the paragraph. 

def average_vowels_and_consonants_per_sentence(paragraph):
    number_sentences = 0
    punctuation = set('.!?')
    for i in range(len(paragraph)):
        if paragraph[i] in punctuation:
            number_sentences += 1
    total_vowels, total_consonants = counting_vowels_and_consonants(paragraph)
    if number_sentences > 0:
        avgvow = total_vowels / number_sentences
        avgcon = total_consonants / number_sentences
    return (number_sentences, avgvow, avgcon)
result = average_vowels_and_consonants_per_sentence(paragraph)
print(f"Number of sentences: {result[0]}")
print(f"Average vowels per sentence: {result[1]}")
print(f"Average consonants per sentence: {result[2]}")