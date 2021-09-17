# -*- coding: utf-8 -*-

# Problem
# https://www.urionlinejudge.com.br/judge/en/problems/view/1430

from sys import stdin

notes = {"W":1,"H":1/2,"Q":1/4,"E":1/8,"S":1/16,"T":1/32,"X":1/64}

def addNumbers(measure):
    tot = 0
    for note in measure:
        tot += int(notes[note])
    return tot

strArr = [str(x) for x in stdin.readline().split("/")]
for measure in strArr[1:-1]:
    print(addNumbers(measure))
