# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 14:23:14 2020
Lasted Edited on 11/14/20
@author: Dalia 
"""

#This function ciphers the string given by the user
def cipher(text):
    
    result = ""
    s = ord(text[0])
    
   # transverse the plain text
    for i in text:
        result += chr((ord(i) + s))
    return result

#This function deciphers the string given by the user. 
def decipher(text):
    
    result2 = ""
    s = int(ord(text[0])/2)
    
    for i in text:
        result2 += chr((ord(i) - s))
    return result2

#This function does the action of receiving the input and printing the output
def main():
    
    #Ask for user input of sentence
    sentence = input("Enter a sentence to cipher and decipher: ")
    
    #calls cipher function and prints output
    csentence = cipher(sentence)
    print("This is your sentence ciphered: ", csentence)
    
    #calls decipher function and prints output
    #takes the output of the cipher function and uses it as input
    dsentence = decipher(csentence)
    print("This is your sentence deciphered: ", dsentence)
    
    
main()
