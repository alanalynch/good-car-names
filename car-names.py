#!/usr/bin/env python

def car_name(query):
    freqs = {
        '0': 60,
        '1': -74,
        '2': 6,
        '3': 55,
        '4': 35,
        '5': 74,
        '6': 6,
        '7': -58,
        '8': -67,
        '9': -37,
        'a': -14,
        'b': -5,
        'c': 27,
        'd': -21,
        'e': -45,
        'f': 5,
        'g': 27,
        'h': -44,
        'i': -21,
        'j': 64,
        'k': 32,
        'l': 12,
        'm': 19,
        'n': -46,
        'o': -80,
        'p': -27,
        'q': 40,
        'r': 8,
        's': 15,
        't': -18,
        'u': -68,
        'v': 41,
        'w': -20,
        'x': 126,
        'y': -90,
        'z': 83
    }

    average = [freqs[c] for c in query.lower() if c in freqs.keys()]
    return str(sum(average)/len(average))

if __name__=='__main__':
    test = raw_input("What do you think makes a good car name? ")
    print car_name(test) + ": fine, I suppose" if int(car_name(test)) >= 0 else car_name(test) + ": garbage"
