# -*- coding: utf-8 -*-

# Problem
# https://www.urionlinejudge.com.br/judge/en/problems/view/1430

from sys import stdin

notes = {"W":1,"H":1/2,"Q":1/4,"E":1/8,"S":1/16,"T":1/32,"X":1/64}


def addNumbers(measure):
    tot = 0
    for note in measure:
        tot += float(notes[note])
    return tot

def returnAmount(arr):
    amount = 0
    for measure in arr[1:-1]:
        if (addNumbers(measure) == 1):
            amount+=1
    return amount

    
strArr = [str(x) for x in stdin.readline().strip("\n").split("/")]
try:
    print(returnAmount(strArr))
except:
    print("")