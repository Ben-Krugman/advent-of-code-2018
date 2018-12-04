from collections import Counter

input = open("day2input.txt", 'r')
inputList = input.read().strip().splitlines()
input.close()

pair = 0 
third = 0  
for x in inputList:
     c = Counter(x)
     #This iterates through the key and value of c.items() and checks if any of them show up 2 times. 
     #Then we get the length of this and see if its greater than 0 to see if it exists
     if len([k for k,v in c.items() if v == 2]) > 0:
          pair += 1
     if len([k for k,v in c.items() if v == 3]) > 0:
          third += 1

answer = pair*third
print("answer: " + str(answer))