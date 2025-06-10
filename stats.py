def get_num_words(text):
    words = text.split();
    return len(words)

def get_chars_dict(text):
    char_dict = {}
    lowercase = text.lower()
    for char in lowercase:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict["num"]

def sort_dict(chars_dict):
    sorted_list = []
    for c in chars_dict:
        if c.isalpha():
            entry = {
                "char": c,
                "num": chars_dict[c]
            }
            sorted_list.append(entry)
    sorted_list.sort(reverse = True, key=sort_on)
    return sorted_list
