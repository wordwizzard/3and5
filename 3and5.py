limit = 100
i = 1

for i in range(limit):
    if (i % 3 == 0) & (i % 5 != 0):
        print('fizz')
    elif (i % 5 == 0) & (i % 3 != 0):
        print('buzz')
    elif (i % 3 == 0) & (i % 5 == 0) & (i != 0):
        print('fizzbuzz')
    else:
        print(i)

