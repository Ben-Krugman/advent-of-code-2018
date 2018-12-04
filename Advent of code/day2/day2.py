from collections import Counter

input = open("day2input.txt", 'r')
inputList = input.read().strip().splitlines()
input.close()

pair = 0 
third = 0  
for x in inputList:
     c = Counter(x)
     
     #c.items() returns a tuple of a letter and a number. The letter is a letter in the word and the number
     #is how many times it shows up. What we are doing here is looping through the keys and on each key
     #we check if the value is equal to either 2 or 3. If it is then we check if the length of thhe
     #new list we made is greater than 0. The reason we do this is because if the length was 0 then there would
     #be no tuple where the value is equal to 2 or 3. 
     if len([k for k,v in c.items() if v == 2]) > 0:
          pair += 1
     if len([k for k,v in c.items() if v == 3]) > 0:
          third += 1

answer = pair*third
print("answer: " + str(answer))