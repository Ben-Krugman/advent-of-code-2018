      input = open("day1input.txt", 'r')
      inputList = input.readlines()
      #I found this on google to get rid of the \n 
      #first it splits the value i, in the for loop it splits the value of the array and gets rid of the \n
      # the first value of the split says what to split and the second is the max amount of splits made this is 1
      #the 0 asks for the index 0 of the list which is the stuff before the \n
      inputList = [i.split('\n', 1)[0] for i in inputList]

      def splitString():
            #This whole function checks what the sign is using .find() and then it sets it to a value 
            #then sets the number to a value by replacing the sign with a space.
            if x.find('+') != -1:
                  sign = '+'
            else:
                  sign = '-'
            number = x.replace(sign, "")
            return sign, number

      previousNumber = 0
      #main loop
      for x in inputList:
            sign, number = splitString()
            
            if(sign == '+'):
                  previousNumber =  previousNumber + int(number)
            else:
                  previousNumber = previousNumber - int(number) 
            
      print(previousNumber)
      #no code goes bellow here.
      input.close()