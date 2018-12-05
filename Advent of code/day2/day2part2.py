import itertools

input = open("day2input.txt", 'r')
inputList = input.read().strip().splitlines()
input.close()

for i in inputList:
      for j in inputList:
            different = 0
            for idx, val in enumerate(i):
                  if val != j[idx]:
                        different += 1
            if different == 1:
                  ans = [val for idx, val in enumerate(i) if j[idx] == val]
                  print("part 2:", ''.join(ans))