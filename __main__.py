from pathlib import Path
import os.path
from random import choice
import sqlite3


BASE_DIR = Path(os.path.realpath(__file__)).parents[0]
BOOKS_DIR = os.path.join(BASE_DIR, "books")
MEDITATIONS_PATH = os.path.join(BOOKS_DIR, "meditations_formatted.txt")

MEDITATIONS_FILE = open(MEDITATIONS_PATH, "r")
MEDITATIONS_PARAGRAPHS = MEDITATIONS_FILE.readlines()
MEDITATIONS_FILE.close()
MEDITATIONS_PARAGRAPHS = list(filter(lambda x: x[:4] != "BOOK", MEDITATIONS_PARAGRAPHS))
print(choice(MEDITATIONS_PARAGRAPHS))
