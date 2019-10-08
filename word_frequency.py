
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

def remove_stop_words(list):
    unstopped = []
    for word in list:
        if word not in STOP_WORDS:
            unstopped.append(word)
    return unstopped

def count(words):
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] +=1
        else:
            word_count[word] = 1
    return word_count

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open (file) as file:
        text = file.read()
        lowercase = text.lower()
        unpunctuated = remove_punctuation(lowercase)
        nonstop = remove_stop_words(unpunctuated)
        counted_words = count(nonstop)
        print(counted_words)

print_word_freq('seneca_falls.txt')
# print_word_freq('emancipation_proclamation.txt')

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
