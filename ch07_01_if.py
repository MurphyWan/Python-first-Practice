number = 23
guess = int(input('Enter an integer : '))

if guess == number:
    print('Congratulations, bingo!')  # New block starts here    
    print('(but you do not win any prizes!)')  # New block ends here
elif guess < number:
    print('No, it is a litter higher than that')
    # you can do whatever you want in a block ...
else:
    print('No, it is a letter lower than that')
    # you must have guess > number to reach here
print('Done')
# That last statement is always executed, after the if statement is executed
