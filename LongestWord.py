# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 22:12:06 2015
@author: davidvillero
"""
import collections as Coll


class node:
    def __init__(self, l=None, isTerm=False):
        self.children={}
        self.l=l
        self.isTerm=isTerm
        
    
class Trie:
    def __init__(self):
        self.root=node('')
        
     
    def __contains__(self, word):
        current=self.root
        for l in word:
            if l not in current.children:
                return False
            current=current.children[l]
        return current.isTerm
        
    def insert(self, word):
        """
        This Fucntion inserts word in prefix tree.
        """
        current=self.root
        for l in word:
            if l not in current.children:
                current.children[l]=node(l)
            current=current.children[l]
        current.isTerm=True
    

    
    def Prefixes_from_Word(self, word):
        """
        This fucntion recieves a word and returns all prefixes that appear
        in the given list (list must be sorted).
        """
        prefix=''
        prefixes=[]
        current=self.root
        for l in word:
            if l not in current.children:
                return prefixes
            current=current.children[l]
            prefix+=l
            if current.isTerm:
                prefixes.append(prefix)
        return prefixes
        
def longestCompWord(words):
    """
    This function receives a list of words, (assuming that the list is already sorted)
    it then scans the list and inserts each word into a prefix Tree. 
    It then pops each word and checks for prefixes in the word in order to be selected as the
    longest word. Once all words with prefixes (compound words) are selected the
    function checks for the longest compound word.
    """
    trie=Trie()
    queue=Coll.deque()
    for word in words:
        prefixes=trie.Prefixes_from_Word(word)
        for prefix in prefixes:
            queue.append( (word, word[len(prefix):]) )#append words and prefixes to queue
        trie.insert(word)
        
    longestCompWord=''
    maxLength=0
    while queue:
        word, suffix = queue.popleft()
        if suffix in trie and len(word)>maxLength:# check for prefix and longest word in queue
            longestCompWord=word
            maxLength=len(word)
        else:                                     #add word-prefix pair to tree
            prefixes=trie.Prefixes_from_Word(suffix)
            for prefix in prefixes:
                queue.append((word,suffix[len(prefix):]))
                
    return longestCompWord
    
if __name__ == '__main__':
    FILE=raw_input("Please enter the name of the file: ")
    words = open(FILE).read().split()
    longestword=longestCompWord(words)
    print "The longest compound word in the list is: ", longestword
