def count_words_in_string(string):
    words = string.split()
    return len(words)


def get_num_of_each_unique_characters(text):
    character_counts = {}
    for character in text:
        char = character.lower()
        if char in character_counts:
            character_counts[char] += 1
        else:
            character_counts[char] = 1
    return character_counts
