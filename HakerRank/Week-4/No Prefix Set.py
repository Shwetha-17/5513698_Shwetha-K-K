#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'noPrefix' function below.
#
# The function accepts STRING_ARRAY words as parameter.
#

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

def noPrefix(words):
    root = TrieNode()
    for word in words:
        node = root
        for i, ch in enumerate(word):
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
            if node.isEnd:
                print("BAD SET")
                print(word)
                return
        if node.children:
            print("BAD SET")
            print(word)
            return
        node.isEnd = True
    print("GOOD SET")
if __name__ == '__main__':
    n = int(input().strip())

    words = []

    for _ in range(n):
        words_item = input()
        words.append(words_item)

    noPrefix(words)
