#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'funWithAnagrams' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY text as parameter.
#
def checkAnagrams(word, arr):
    for x in text:
        if (sorted(word) == sorted(x)):
            return True
    return False

def funWithAnagrams(text):
    # Write your code here
    limit = len(text)

    anagram_list = list(text)
    sorted_words = []
    count = 0
    for i in range(0, limit):
        sorted_words.append(''.join(sorted(text[i])))
        if (text[i+1:] and checkAnagrams(text[i], text[i+1:])):
            anagram_list.pop
            count += 1
    anagram_dict = dict(zip(anagram_list, sorted_words))
    
    output = {}
    
    for key, value in anagram_dict.items():
        if value not in output:
            output[value] = [key] 
        else:
            output[value].append(key)
            
    answer = list(output.values())
    output_list = []
    for i in answer:
        output_list.append(i[0])
    return(sorted(output_list))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    text_count = int(input().strip())

    text = []

    for _ in range(text_count):
        text_item = input()
        text.append(text_item)

    result = funWithAnagrams(text)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
