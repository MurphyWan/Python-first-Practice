number = 23
running = True

while running:
  guess = int(input('Enter an integer : '))
  
  if guess == number:
      print('Congratulations, bingo!')  # New block starts here    
      print('(but you do not win any prizes!)')  # New block ends here
      running = False;
  elif guess < number:
      print('No, it is a litter higher than that')
      # you can do whatever you want in a block ...
  else:
      print('No, it is a letter lower than that')
      # you must have guess > number to reach here

else:
    print("the while loop is over.")

print('Done')
