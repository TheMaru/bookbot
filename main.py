from stats import count_words_in_string, get_num_of_each_unique_characters


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content


def main():
    frankenstein_content = get_book_text("./books/frankenstein.txt")
    amount_words = count_words_in_string(frankenstein_content)
    character_counts = get_num_of_each_unique_characters(frankenstein_content)
    print(f"Found {amount_words} total words")
    print(character_counts)


main()
