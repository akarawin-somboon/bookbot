def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    
    # Convert dictionary to list
    chars_list = convert_dict_to_list(chars_dict)
    
    # Sort the list
    chars_list.sort(reverse=True, key=sort_on)
    
    # Now print the report...
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    # Print each character's count
    for char in chars_list:
        print(f"The '{char['name']}' character was found {char['num']} times")
    
    print("--- End report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

def sort_on(dict):
    return dict["num"]

def convert_dict_to_list(char_dict):
    chars_list = []
    for char in char_dict:
        if char.isalpha():
            char_info = {"name": char, "num": char_dict[char]}
            chars_list.append(char_info)
    return chars_list


main()