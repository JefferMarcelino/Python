from random import randint

print('Random multiplication')
print('-' * 30)

for c in range(1, 500):
    random_number = randint(1, 9999)
    print('{} x {} = {}'.format(c, random_number, c*random_number))
