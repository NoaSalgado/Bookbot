def main():
    book = get_book_text("./books/frankenstein.txt") 
    num_words = get_num_words(book)
    characters = count_characters(book)
    report = (
        "--- Begin report of books/frankenstein.txt ---\n"
        f'{num_words} words found in the document \n \n'
    )
    
    for character, times in characters.items():
        report += f'The {character} character was found {times} times \n'
    
    report += "--- End report ---"
    print(report)

def get_book_text(path):
    with open(path) as file:
        return file.read()

def get_num_words(file):
    return len(file.split())

def count_characters(file):
    characters = dict()
    for character in file.lower():
        if character in characters:
            characters[character] += 1
        elif character.isalpha():
            characters[character] = 1
    return dict(sorted(characters.items()))

main()