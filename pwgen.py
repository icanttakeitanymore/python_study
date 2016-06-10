#!/usr/bin/env python3
"""simple password/string generator"""
import random
import sys


def password_generator(value=8):
    """String Generator
    Lenght of string == value.
    """
    alp = []
    alp.extend([chr(x) for x in range(48,58)]) # Числа.
    alp.extend([chr(x) for x in range(65,90)]) # ASCI заглавные.
    alp.extend([chr(x) for x in range(97,122)]) # ASCI строчные.

    password = []
    [password.append(random.choice(alp)) for x in range(value)] # Генератор

    return ''.join(password) # Возвращение строки


if __name__ == "__main__":
    """Run in Shell"""
    try:
        print(password_generator(int(sys.argv[1])))
    except IndexError:
        print(password_generator())
