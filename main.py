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


def print_report(words, letters):
    print("--- Beging report of books/frankenstein.txt ---")
    print(f"{words} words found in the document\n")
    for letter in letters:
        print(f"The '{letter}' character was found {letters[letter]} times")
    print("--- End report ---")


def main():
    words = 0
    letters = {}
    with open("books/frankenstein.txt", encoding="ascii") as f:
        file_contents = f.read()
        words = count_words(file_contents)
        letters = count_characters(file_contents)
    letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))
    print_report(words, letters)


if __name__ == "__main__":
    main()
