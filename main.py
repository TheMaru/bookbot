def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content


def count_words_in_string(string):
    words = string.split()
    return len(words)


def main():
    frankenstein_content = get_book_text("./books/frankenstein.txt")
    amount_words = count_words_in_string(frankenstein_content)
    print(f"Found {amount_words} total words")


main()
