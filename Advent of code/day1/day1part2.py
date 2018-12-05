import itertools

input = [int(x) for x in open("day1input.txt").readlines()]
print(input)
frequency = 0
seen = {0}
for num in itertools.cycle(input):
      frequency += num
      if frequency in seen:
            print(frequency)
            break
      seen.add(frequency)