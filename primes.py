import time
from os import system, name
primes = []
clear = lambda: system('cls' if name == 'nt' else 'clear') # OS-agnostic clear function

def writeLog(primeList, timeTaken, mode): # function to write out logfile, if called
    with open('log.txt', 'w') as f:
        f.write(f'Log was generated on {time.asctime()}\n')
        f.write(mode)
        f.write(f'Time taken: {timeTaken} seconds')
        f.write('\nPrime numbers found:\n')
        for p in primeList:
            f.write(f'\n{p}')

calcType = input('1. Find a set number of primes\n2. Search for primes in a range of numbers\n\nEnter choice: ')
while calcType not in {'1', '2'}:
    clear()
    calcType = input('Invalid input.\n1. Find a set number of primes\n2. Search for primes in a range of numbers\n\nEnter choice: ')

if calcType == '2': # if searching through range for primes
    clear()
    startNum = input('Enter starting number (default=1): ') # grab starting number and ensure it's valid
    if not startNum or not startNum.isdigit():
        startNum = 1
    startNum = int(startNum)
    print(f'Starting number is {startNum}')

    endNum = input('\nEnter an ending number (must be higher than starting number): ') #grab ending number and ensure it's valid
    while not endNum.isdigit() or int(endNum) <= startNum:
        clear()
        endNum = input('\nInvalid number.\n\nEnter an ending number (must be higher than starting number): ')
    endNum = int(endNum)
    print(f'Ending number is {endNum}')
    endNum += 1

    startTime = time.time() # grab start time right before primes are calculated to give accurate time

    for candidate in range(startNum, endNum): # calculate primes until end of specified range is reached
        isPrime = True
        for divisor in range(startNum+1, candidate-1):
            if candidate % divisor == 0:
                isPrime = False
                break # to increase efficiency, break nested loop if candidate is divisible by anything
        
        if isPrime:
            primes.append(candidate)

    endTime = time.time() # grab end time right after prime calculation is finished

    timeTaken = round((endTime - startTime), 5) # rounds time taken to calculate primes to 5 decimals

    clear()
    print(f'Primes found: {len(primes)}')
    print(f'Time taken: {timeTaken} seconds.')

    conf = input('\nCreate logfile? (y/n): ')
    while conf not in {'y', 'n'}:
        clear()
        conf = input(('Invalid entry.\n\nCreate logfile? (y/n): '))

    if conf == 'y': # pass text & values to logfile writer
        writeLog(primes, timeTaken, f'Mode selected: Search for primes through a range\nStarting number: {startNum}\nEnding number: {endNum-1}\n')
else: # if finding specific number of primes
    clear()
    amtOfPrimes = input('Enter amount of primes to find (must be 1 or greater): ') # grab amount of primes and ensure it's valid
    while not amtOfPrimes.isdigit() or int(amtOfPrimes) < 1:
        clear()
        amtOfPrimes = input('\n\nInvalid input.\nEnter amount of primes to find (must be 1 or greater): ')
    amtOfPrimes = int(amtOfPrimes)

    candidate = 0 # initialize candidate number BEFORE grabbing start time
    startTime = time.time() # grab start time right before primes are calculated to give accurate time

    while len(primes) < amtOfPrimes: # calculate primes until specified number of primes is reached
        candidate += 1 # increment candidate number
        isPrime = True
        for divisor in range(2, candidate-1):
            if candidate % divisor == 0:
                isPrime = False
                break # to increase efficiency, break nested loop if candidate is divisible by anything
        
        if isPrime:
            primes.append(candidate)
    
    endTime = time.time() # grab end time right after prime calculation is finished

    timeTaken = round((endTime - startTime), 5) # rounds time taken to calculate primes to 5 decimals

    clear()
    print(f'Time taken: {timeTaken} seconds.')
    print(f'Primes requested: {amtOfPrimes}\nPrimes found: {len(primes)}')

    conf = input('\nCreate logfile? (y/n): ')
    while conf not in {'y', 'n'}:
        clear()
        conf = input(('Invalid entry.\n\nCreate logfile? (y/n): '))

    if conf == 'y': # pass text & values to logfile writer
        writeLog(primes, timeTaken, f'Mode selected: Find set number of primes\nPrimes requested: {amtOfPrimes}\nPrimes found: {len(primes)}\n')