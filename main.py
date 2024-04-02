def read_book(file_path):
    with open(file_path, 'r') as file:
        book = file.read()
        return book

def count_of_words(book):
    words = book.split()
    return len(words)
def count_of_letters(book):
    letter_dict = {}
    for lines in book:
        lines = lines.lower()
        for letter in lines:
            if letter.isalpha():
                if letter in letter_dict:
                    letter_dict[letter] += 1
                else:
                    letter_dict[letter] = 1
    return letter_dict

def make_report_and_print(book, words, letters):
    print(f"--- Begin report of {book} ---")
    print(f"{words} words found in the document\n")
    letters = dict(sorted(letters.items(), key=lambda item: item[1], reverse=True))

    for letter, count in letters.items():
        print(f"The {letter} character was found {count} times")
    print(f"--- End report ---")
def main():
    file_path = ""
    readed_book = read_book(file_path)
    dict_of_letters = count_of_letters(readed_book)
    words = count_of_words(readed_book)
    make_report_and_print(file_path, words, dict_of_letters)

if __name__ == '__main__':
    main()
