
import string

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

def remove_stop_words(text):
    final_word_list = []
    for word in text:
        if word not in STOP_WORDS:
            final_word_list.append(word)
            print(final_word_list)

def remove_punctuation(text):
    for character in text:
        if character in string.punctuation:
            text = text.replace(character, "")
            word_list = text.split()
            return word_list

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file."""

    with open (file) as file:
        text = file.read()
        lowercase = text.lower()
        # list_items = lowercase.split()
        unpunctuated = remove_punctuation(lowercase)
        remove_stop_words(unpunctuated)



print_word_freq("seneca_falls.txt")

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
