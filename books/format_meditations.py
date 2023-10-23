from functools import reduce
from pathlib import Path
import os

BASE_DIR = Path(os.path.realpath(__file__)).parents[0]

def format():
    f = open(os.path.join(BASE_DIR, "meditations.txt"), "r")
    lines = f.readlines()
    f.close()

    lines = list(filter(lambda x: x != '\n', lines))
    print(len(lines))

    i = 0
    while i < len(lines):
        line = lines[i]
        if line == "\n" or "-" * 70 in line:
            lines.pop(i)
            i -= 1
        if line[:4] == "BOOK" and i != 0:
            lines[i-1] = lines[i-1] + "\n"
        if line[0].islower():
            lines[i-1] = lines[i-1][:-1] + " "
            lines[i-1] += lines[i]
            lines.pop(i)
            i -= 1
        i += 1

    text = reduce(lambda i, c: i + c, lines)
    f = open(os.path.join(BASE_DIR, "meditations_formatted.txt"), "w")
    f.write(text)
    f.close()

def categorize():
    f = open(os.path.join(BASE_DIR, "meditations_formatted.txt"), "r")
    lines = f.readlines()
    f.close()
    books = []
    for line in lines:
        if line[:4] == "BOOK":
            books.append([])
        books[-1].append(line)
    
    try:
        os.mkdir(os.path.join(BASE_DIR, "meditation_books"))
    except:
        pass
    BOOKS_PATH = os.path.join(BASE_DIR, "meditation_books")

    for i, book in enumerate(books):
        f = open(os.path.join(BOOKS_PATH, f"book{i+1}.txt"), "w")
        text = reduce(lambda i, c: i + c, book)
        text = text[:-2]
        f.write(text)
        f.close()


if __name__ == "__main__":
    categorize()
