import random

#Rolls a random number from x to y
def roll_numbers(data):
  arr = data.content.split(" ")      #Split the input message to get the numbers
  if len(arr) == 2:                  #If there is only one number it will start with 0 
    if not arr[1].isdigit():         #Checks if the input is a number
      return("Bitte nur ganze Zahlen angeben")
    else:
      n2 = int(arr[1])+1
      n = random.randrange(0, n2)
      return(f'{str(data.author)[:-5]} hat eine {n} gewürfelt')
  else:
    if not arr[1].isdigit() or not arr[2].isdigit():     #Checks if the inputs are numbers
      return("Bitte nur ganze Zahlen angeben")
    else:
      n1 = int(arr[1])-1
      n2 = int(arr[2])+1
      n = random.randrange(n1, n2)
      return(f'{str(data.author)[:-5]} hat eine {n} gewürfelt')
 
#Rolls a random number fom 1 to 100
def roll_100(data):
    n = random.randrange(0, 101)
    return(f'{str(data.author)[:-5]} hat eine {n} gewürfelt')
        
def throw_coin():
    n = random.choice([1, 2])
    if n == 1:
        return("Die Münze ist auf Kopf gelandet!")
    else:
        return("Die Münze ist auf Zahl gelandet!")
  