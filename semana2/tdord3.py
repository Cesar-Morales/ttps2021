dictionary = dict()

numbers = [str(x) for x in stdin.readline().strip().split(" ")]
for number in numbers:
  if number in dictionary.keys():
    n = dictionary.get(number)
    dictionary.update({number : n+1})
  else:
    dictionary.update({number : 1})

for number in dictionary.keys():
      stdout.write("\r%s %s\n" % (number, dictionary.get(number)))