# coding=utf-8

from __future__ import unicode_literals
from prompt_toolkit import prompt

def main():
    text = prompt("> ")
    print('You entered:', text)

if __name__ == '__main__':
    main()