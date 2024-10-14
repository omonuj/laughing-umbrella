import re
from collections import Counter

def most_occured_element(word):

    arr = re.findall(r'[0-9]', word)

    maxm = 0
    max_element = 0
    c = Counter(arr)

    for index in list(c.keys()):
        if c[index] >= maxm:
            maxm = c[index]
            max_element = index
    return max_element

if __name__ == '__main__':
    word = 'geek55of55gee4ksabc3dr2x'
    #print(most_occured_element(word))

    'Valid' if re.fullmatch(r'\d{5}', '02215') else 'Invalid'