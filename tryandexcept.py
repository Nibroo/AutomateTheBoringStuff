def div42by(divideBy):
        try:
                return 42 / divideBy
        except ZeroDivisionError:
                print('Why divide by 0?')

print(div42by(2))
print(div42by(12))
print(div42by(0))
print(div42by(1))


print('How many sims you have?')
numSim = input()

try:
        if int(numSim) < 4:
            print('You do not have all of them')
        else:
            print('Whoa!')

except ValueError:
        print('Please insert a valid number')
