import time
primes = []

startNum = input('Enter starting number (default=1): ')
if not startNum or not startNum.isdigit():
    startNum = 1
startNum = int(startNum)
print(f'Starting number is {startNum}')

endNum = input('Enter an ending number (must be higher than starting number): ')
while not endNum.isdigit() or int(endNum) <= startNum:
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

timeTaken = round((endTime - startTime), 4)

print(f'\n\nPrimes found: {len(primes)}')
print(f'Time taken: {timeTaken} seconds.')

conf = input('Show which primes were found? (y/n): ')
while conf not in {'y', 'n'}:
    conf = input(('\nInvalid entry.\n\nShow which primes were found?'))

if conf == 'y':
    for i in primes:
        print(i)