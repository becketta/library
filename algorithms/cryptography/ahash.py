# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 20:02:48 2016

@author: Aaron Beckett
"""
import random
import string

def ahash(data, space = 1024):
    """A custom hash function!"""
    
    def get_bits(string):
        """Return the first 16 bits of a string."""
        for i,char in enumerate(string):
            yield ord(char), i
            
    if not data:
        return 0
            
    h = space
    cursor = get_bits(data)
    try:
        while True:
            chunk, pos = next(cursor)
            h += chunk
            temp = (pos << 11) ^ h
            h = (h << 16) ^ temp
            h += h >> 11
    except StopIteration:
        h ^= h << 3;
        h += h >> 5;
        h ^= h << 4;
        h += h >> 17;
        h ^= h << 25;
        h += h >> 6;
    
    return h % space
    
def test_ahash(trials = 100000, data_len = 128, table_size = 1024):
    
    random.seed()
    
    record = [0] * table_size
    for _ in range(trials):
        s = []
        for _ in range(random.randrange(data_len)):
            s.append(random.choice(string.ascii_letters))
        record[ahash(''.join(s), table_size)] += 1
        
    return record