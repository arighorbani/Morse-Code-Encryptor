# -*- coding: utf-8 -*-
"""
Created on Tue Jan  7 16:36:04 2020

@author: arigh
"""

morse_code_dict = {"A":".-", "B":"-...", "C":"-.-.", "D":"-..", "E":".", "F":"..-.",
                   "G":"--.", "H":"....", "I":"..", "J":".---", "K":"-.-", "L":".-..", "M":"--",
                   "N":"-.", "O":"---", "P":".--.", "Q":"--.-", "R":".-.", "S":"...", "T":"-",
                   "U":"..-", "V":"...-", "W":".--", "X":"-..-", "Y":"-.--", "Z":"--..",
                   "1":".----", "2":"..---", "3":"...--", "4":"....-", "5":".....", "6":"-....",
                   "7":"--...", "8":"---..", "9":"----.", "0":"-----"}





def encrypt(morse_code_dict):

    morse_code_current = ""

    morse_code_current = input("Please enter all of the letters and numbers you want to have encrypted. Enter the letters in uppercase." + '\n')

    for digit in morse_code_current:
        if digit in morse_code_dict.keys():
            print(morse_code_dict[digit])
            print(" ")

    print("Thank you! We'll now be bringing you back to the menu for further translation, or to exit.")
    choice()

    return

def choice():
    input_tracker = ""


    input_tracker = input("Enter your choice now." + '\n')

    if input_tracker == "E":
        encrypt(morse_code_dict)
    elif input_tracker == "Q":
        exit()
    else:
        print("Please enter a character corresponding to the options shown initially." + '\n')
        choice()

print("Welcome to the encryptor! Here, whatever letters you enter will be translated into morse code.")
print("Please enter 'E' if you want to encrypt a series of characters.")
print("Enter 'Q' to exit the program.")

choice()