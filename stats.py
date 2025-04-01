def count_words(book_text):
    words = book_text.split()
    num_words = len(words)
    return num_words

def count_chars(book_text):
    book_text = book_text.lower()
    char_count = {}
    for char in book_text:
        if char in char_count:
            char_count[char] += 1 
        else:
            char_count[char] = 1
    return char_count

def sort_char_counts(char_count_dict):
    char_list = [{'character': char, 'count': count} for char, count in char_count_dict.items()]

    char_list.sort(key=lambda x: x['count'], reverse=True)
    return char_list
