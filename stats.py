
def get_num_words(text):
    words = text.split()
    return len(words)

def count_char(text):
    freq = {}
    for c in text:
        c = c.lower()
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    return freq

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list