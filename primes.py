import time
from os import system, name
primes = []
clear = lambda: system('cls' if name == 'nt' else 'clear')

def writeLog(primeList, timeTaken, mode):
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

if calcType == '2':
    clear()
    startNum = input('Enter starting number (default=1): ')
    if not startNum or not startNum.isdigit():
        startNum = 1
    startNum = int(startNum)
    print(f'Starting number is {startNum}')

    endNum = input('\nEnter an ending number (must be higher than starting number): ')
    while not endNum.isdigit() or int(endNum) <= startNum:
        clear()
        endNum = input('\nInvalid number.\n\nEnter an ending number (must be higher than starting number): ')
    endNum = int(endNum)
    print(f'Ending number is {endNum}')
    endNum += 1

    startTime = time.time()

    for candidate in range(startNum, endNum):
        isPrime = True
        for divisor in range(startNum+1, candidate-1):
            if candidate % divisor == 0:
                isPrime = False
                break
        
        if isPrime:
            primes.append(candidate)

    endTime = time.time()

    timeTaken = round((endTime - startTime), 5)

    clear()
    print(f'Primes found: {len(primes)}')
    print(f'Time taken: {timeTaken} seconds.')

    conf = input('\nCreate logfile? (y/n): ')
    while conf not in {'y', 'n'}:
        clear()
        conf = input(('Invalid entry.\n\nCreate logfile? (y/n): '))

    if conf == 'y':
        writeLog(primes, timeTaken, f'Mode selected: Search for primes through a range\nStarting number: {startNum}\nEnding number: {endNum-1}\n')
else:
    clear()
    amtOfPrimes = input('Enter amount of primes to find (must be 1 or greater): ')
    while not amtOfPrimes.isdigit() or int(amtOfPrimes) < 1:
        clear()
        amtOfPrimes = input('\n\nInvalid input.\nEnter amount of primes to find (must be 1 or greater): ')
    amtOfPrimes = int(amtOfPrimes)

    candidate = 0
    startTime = time.time()

    while len(primes) < amtOfPrimes:
        candidate += 1
        isPrime = True
        for divisor in range(2, candidate-1):
            if candidate % divisor == 0:
                isPrime = False
                break
        
        if isPrime:
            primes.append(candidate)
    
    endTime = time.time()

    timeTaken = round((endTime - startTime), 5)

    clear()
    print(f'Time taken: {timeTaken} seconds.')
    print(f'Primes requested: {amtOfPrimes}\nPrimes found: {len(primes)}')

    conf = input('\nCreate logfile? (y/n): ')
    while conf not in {'y', 'n'}:
        clear()
        conf = input(('Invalid entry.\n\nCreate logfile? (y/n): '))

    if conf == 'y':
        writeLog(primes, timeTaken, f'Mode selected: Find set number of primes\nPrimes requested: {amtOfPrimes}\nPrimes found: {len(primes)}\n')