
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def remove_punctuation(text):
    for character in text:
        if character in string.punctuation or character is '--':
            text = text.replace(character, '')
            word_list = text.split()
            return word_list

def remove_stop_words(array):
    for word in array:
        if word in STOP_WORDS:
            array.remove(word)
            return array

# def count(words):
#     word_count_list = []
#     for word in words:
#         if word not in word_count_list:
#             word_count_list.append(word, 1)
#         else:
#             word_count_list.

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open (file) as file:
        text = file.read()
        lowercase = text.lower()
        unpunctuated = remove_punctuation(lowercase)
        nonstop = remove_stop_words(unpunctuated)
        print(nonstop)



print_word_freq('seneca_falls.txt')

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
