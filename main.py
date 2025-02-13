def main():
    book_path = "books/frankenstein.txt"

    text = get_book_text(book_path)
    # print(text)

    num_words = get_num_words(text)
    # print(f"{num_words} words found in the document")
    
    char_count = get_num_unique_chars(text)
    # print(char_count)

    # report:

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document")
    char_list = []
    for c in char_count:
        char_list.append({"char": c, "num": char_count[c]})
    char_list.sort(reverse=True, key=sort_on)

    for item in char_list:
        if item["char"].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

def sort_on(dict):
    return dict["num"]

def get_num_unique_chars(text):
    lower_text = text.lower()
    store = {}
    for i in range(len(lower_text)):
        ch = lower_text[i]
        if ch in store.keys():
            store[ch]+=1
        else:
            store[ch]=1
    return store

def get_num_words(text):
    words = text.split()
    return len(words)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()