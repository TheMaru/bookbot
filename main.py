from stats import (
    count_words_in_string,
    get_num_of_each_unique_characters,
    generate_sorted_list_of_characters,
)


def get_book_text(filepath):
    with open(filepath) as f:
        file_content = f.read()

    return file_content


def main():
    path = "./books/frankenstein.txt"
    frankenstein_content = get_book_text(path)
    amount_words = count_words_in_string(frankenstein_content)
    character_counts = get_num_of_each_unique_characters(frankenstein_content)
    sorted_char_list = generate_sorted_list_of_characters(character_counts)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {amount_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_list:
        if entry["char"].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print("============= END ===============")


main()
