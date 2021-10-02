# https://www.urionlinejudge.com.br/judge/en/problems/view/1430
notes = {"W":1,"H":1/2,"Q":1/4,"E":1/8,"S":1/16,"T":1/32,"X":1/64}

while True:
    list_measure = input().split("/")
    if list_measure[0] == "*":
        break
    correct = 0
    for measure in list_measure:
        time = 0
        for note in measure:
            time += notes[note]
        if time == 1:
            correct += 1
    print(correct)
