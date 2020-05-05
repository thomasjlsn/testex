#!/usr/bin/env python3

import re
import readline
import sys

header = (
    'Testex: Python3 RegEx tester\n\n'
    'Use "?" to see the string you are testing\n'
    'Use "set" to change the string you are testing\n'
    'Use "quit" to quit\n'
)

Interrupt = (EOFError, KeyboardInterrupt)


def hilight(matches):
    for match in matches:
        try:
            prefix, match, suffix = t.partition(match)
        except:
            print(f'\033[31msyntax error\033[0m')
            return
        print(''.join([
            prefix, f'\033[30;43m{match}\033[0m', suffix
        ]))


def set_string(t):
    try:
        r = input(r'string? ')
        if r != '':
            return r
        return t
    except Interrupt:
        exit(1)


if __name__ == '__main__':
    print(header)
    try:
        t = ''
        try:
            t = sys.argv[1]
        except IndexError:
            t = set_string(t)

        while True:
            r = input(r'> ')
            if r == '':
                continue
            if r == 'set':
                t = set_string(t)
                continue
            if r == '?':
                print(f'string: {t}')
                continue
            if r == 'quit':
                exit(0)

            try:
                matches = re.findall(r, t)
            except:
                print(f'\033[31msyntax error\033[0m')
                continue

            if not matches:
                print(f'\033[31mno match\033[0m')
                continue

            hilight(matches)

    except Interrupt:
        exit(1)
