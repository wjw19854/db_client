# coding=utf-8

from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory

def main():
    history = InMemoryHistory()

    while True:
        text = prompt("> ", history=history)
        print('You entered:', text)
    print('GoodBye!')

if __name__ == '__main__':
    main()