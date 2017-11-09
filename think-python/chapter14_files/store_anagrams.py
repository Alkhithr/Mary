# If you download my solution to Example 12-2 from http://thinkpython2.com/code/anagram_sets.py,
# you'll see that it creates a dictionary that maps from a sorted string of letters to the list of words that can be spelled with those letters.
# For example, 'opst' maps to the list ['opts', 'post', 'pots', 'spot', 'stop', 'tops'].
#
# Write a module that imports anagram_sets and provides two new functions:
# store_anagrams should store the anagram dictionary in a “shelf”;
# read_anagrams should look up a word and return a list of its anagrams.
# Solution: http://thinkpython2.com/code/anagram_db.py
from anagram_sets import *
import dbm
import os
import pickle

anagram_db = 'store_anagram'


def store_anagrams(d):

    anagrams = return_anagram_sets_in_order(d)
    dout = dbm.open(anagram_db, 'n')
    for anagram in anagrams:
        dout[anagram] = pickle.dumps(anagrams)
    return anagrams


def read_anagrams(word):
    din = dbm.open(anagram_db, 'r')
    return pickle.loads(din[word])


if __name__ == '__main__':
    # assert store_anagrams()
    # assert read_anagrams()

    if os.path.exists(anagram_db):
        os.remove(anagram_db)

    d = dict()
    d['opts'] = ['opts', 'post', 'pots', 'spot', 'stop', 'tops']
    stored_anagrams = store_anagrams(d)
    print(stored_anagrams)

    print('opts', read_anagrams('opts'))
    print(read_anagrams('post'))
    print(read_anagrams('tops'))
