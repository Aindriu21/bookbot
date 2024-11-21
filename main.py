def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_char_dict(text)
    sorted_chars_list = sort_chars(chars_dict)

    print(f"--- Begin report of {book_path} --")
    print(f"{num_words} word found in the document")
    print()

    for item in sorted_chars_list:
        if not item["char"].isalpha():
            continue
        print(f"The '{item['char']}' character was foun {item['num']} times")

    print("--- End report ---")


def get_num_words(text):
    word_count = 0
    words = text.split()
    for word in words:
        word_count += 1

    return word_count


def sort_on(d):
    return d["num"]


def sort_chars(characters_dict):
    sorted_chars = []
    for ch in characters_dict:
        sorted_chars.append({"char": ch, "num": characters_dict[ch]})
    sorted_chars.sort(reverse=True, key=sort_on)
    return sorted_chars


def get_char_dict(text):
    char_count = {}
    for char in text:
        low_char = char.lower()
        if low_char in char_count:
            char_count[low_char] += 1
        else:
            char_count[low_char] = 1

    return char_count


def get_book_text(path):
    with open(path) as f:
        return f.read()
    

main()