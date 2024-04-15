#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import string

if __name__ == '__main__':
    lower_chars = string.ascii_lowercase
    upper_chars = string.ascii_uppercase
    digit_chars = string.digits
    symbol_chars = string.punctuation
    all_chars = lower_chars + upper_chars + digit_chars + symbol_chars
    print(lower_chars)
    print(upper_chars)
    print(digit_chars)
    print(symbol_chars)
    print(all_chars)
