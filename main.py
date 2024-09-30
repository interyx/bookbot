import sys


def count_words(text):
    words = text.split()
    return len(words)


def count_characters(text):
    letters = {}
    lowered_text = text.lower()
    for word in lowered_text:
        for letter in word:
            if letter.isalpha():
                if letter not in letters:
                    letters[letter] = 0
                letters[letter] += 1
    return letters


def print_report(filepath, words, letters):
    print(f"--- Beginning report of {filepath} ---")
    print(f"{words} words found in the document\n")
    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---")


def main():
    words = 0
    letters = {}
    filepath = "invalid"
    if sys.argv[1:]:
        filepath = sys.argv[1]
    if filepath == "invalid":
        print("Invalid filename")
        sys.exit()
    try:
        with open(filepath, encoding="utf-8") as f:
            file_contents = f.read()
            words = count_words(file_contents)
            letters = count_characters(file_contents)
        letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
        print_report(filepath, words, letters)
    except IOError as e:
        print("Could not read file")
        print(e)


if __name__ == "__main__":
    main()
