# coding=utf8
from __future__ import unicode_literals
from prompt_toolkit import prompt
from prompt_toolkit.history import InMemoryHistory
from pygments.lexers import SqlLexer

def main():
    history = InMemoryHistory()

    while True:
        text = prompt('> ', lexer=SqlLexer, history=history)
        print('You entered:', text)
        if text.lower() == 'exit':
            # 退出
            break
    print('GoodBye!')

if __name__ == '__main__':
    main()