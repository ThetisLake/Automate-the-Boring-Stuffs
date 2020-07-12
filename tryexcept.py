def div2By (divideBy):
    try:
        return 42/divideBy
    except ZeroDivisionError:
        print('Error: You tried to divide by zero.')

print(div2By(2))
print(div2By(12))
print(div2By(0))
print(div2By(1))

print('How many cats do you have?')

numCats = input()

try:
    if int(numCats) >=4:
        print('That is a lot of cats.')
    else:
        print('That is not that many cats.')

except ValueError:
    print('You did not enter a number.')
