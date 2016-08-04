# -*- coding: utf-8 -*-
"""
Created on Sun Jun 26 15:23:43 2016

@author: Aaron Beckett
"""

def invert(digest):
    """
    Return original message used to make given digest from hash
    
    Original hash:
        digest[i] = ( (129 * message[i]) XOR message[i-1]) % 256
        
    message[-1] = 0 (used for the first element in the message)
    """
    
    message = [None] * 17
    message[0] = 0
    
    for i,el in enumerate(digest):
        message[i+1] = ((el ^ message[i]) * 129) % 256
        
    return message[1:]