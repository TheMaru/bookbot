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


def sort_on(items):
    return items["num"]


def generate_sorted_list_of_characters(character_dict):
    list_of_characters = []
    for character, num in character_dict.items():
        list_of_characters.append({"char": character, "num": num})

    list_of_characters.sort(reverse=True, key=sort_on)

    return list_of_characters
