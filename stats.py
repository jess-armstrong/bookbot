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
